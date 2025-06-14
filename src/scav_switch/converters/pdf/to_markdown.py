"""
Data de escrita: 2025-01-16
Autor: Dayvid Borges

Título: PDF to Markdown Converter with Class Architecture and Parameterized Logging

Descrição:
ScavToMarkdown class to transcribe PDFs into markdown using OpenAI models via LangChain.
Accepts file path, bytes, URL, or base64 string as input, with parameterized logging system
and optimized object-oriented architecture.

Dependências:
- langchain_openai
- langchain_core
- openai
- scav_switch.converters.pdf.common
- concurrent.futures
- tempfile
- base64
- os
- requests
- dotenv
- logging
- tiktoken

Saída:
Returns a markdown string with the detailed PDF transcription via the dig() method.
"""

import base64
import logging
import os
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Optional, Union

import openai
import requests
import tiktoken
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from openai import APITimeoutError

from scav_switch.converters.pdf.common import (pdf_to_image_base64_list,
                                               pdf_to_pages_base64)
from scav_switch.converters.pdf.exceptions import ModelIncompatibilityError

load_dotenv(override=True)


class ScavToMarkdown:
    """
    PDF to Markdown converter with support for multiple input formats
    and parameterized logging system.
    """

    def __init__(
        self,
        model: str = "gpt-4.1",
        temperature: float = 0,
        max_tokens: int = 2048,
        timeout: int = 90,
        max_workers: int = 10,
        verbose: bool = True,
        log_level: str = "INFO",
        callbacks: Optional[list[Callable[..., Any]]] = None,
        logger: logging.Logger = None
    ):
        """
        Initializes the ScavToMarkdown converter.

        Args:
            model: OpenAI model to use
            temperature: Temperature for text generation
            max_tokens: Maximum number of tokens
            timeout: Request timeout
            max_workers: Maximum number of workers for parallel processing
            verbose: Enable/disable logging
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
            callbacks: LangChain callbacks for tracing
            logger: Optional custom logger instance (for dynamic override)
        """
        if model not in ("gpt-4.1", "gpt-4o"):
            raise ModelIncompatibilityError(
                f"Model '{model}' is not compatible. Only 'gpt-4.1' and 'gpt-4o' are supported for PDF to Markdown conversion."
            )

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_workers = max_workers
        self.callbacks = callbacks

        # Logging configuration
        self.verbose = verbose
        if logger is not None:
            self.logger = logger
        else:
            self.logger = self._setup_logger(log_level)
        if not self.verbose:
            self.logger.disabled = True

        # Token tracking attributes
        self.tokens_usage = {
            'input': 0,
            'output': 0,
            'total': 0,
            'details': []  # lista de dicts por página: {'page': n, 'input': x, 'output': y, 'total': z, ...}
        }

        # System prompt
        self.system_prompt = (
            """
            Role: PDF transcription specialist.
            Goal: Perform detailed transcriptions of PDF files, observing the page layout and transcribing with maximum detail and accuracy.
            Instructions: - Use markdown format for the output.
                          - Do not omit information, invent, or misinterpret.
                          - Pay attention to numerical details.
                          - Transcribe the observed layout (tables, bullets, etc.) to markdown format.
            """
        )

        # Model initialization
        self.llm = ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            callbacks=self.callbacks,
            timeout=self.timeout
        )

        self._log(
            'INFO', 'ScavToMarkdown initialized - Project: %s' % os.getenv("LANGSMITH_PROJECT")
        )

    def _setup_logger(self, log_level: str) -> logging.Logger:
        """Configures the logging system with a friendly logger name."""
        logger = logging.getLogger("ScavToMarkdown")
        logger.setLevel(getattr(logging, log_level.upper()))
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    def _log(self, level: str, message: str, *args) -> None:
        """Parameterized logging."""
        if not self.verbose:
            return
        log_method = getattr(self.logger, level.lower(), self.logger.info)
        log_method(message, *args)

    def _get_pdf_bytes(self, source: Union[str, bytes]) -> bytes:
        """
        Receives a file path, bytes, URL, or base64 string and returns the PDF bytes.
        """
        self._log("DEBUG", "Processing input of type: %s", type(source))

        if isinstance(source, bytes):
            self._log("DEBUG", "Input identified as bytes")
            return source

        if isinstance(source, str):
            # Detect base64
            try:
                if source.strip().startswith("data:application/pdf;base64,"):
                    b64_data = source.split(",", 1)[1]
                else:
                    b64_data = source

                pdf_bytes = base64.b64decode(b64_data, validate=True)
                if pdf_bytes[:4] == b"%PDF":
                    self._log("DEBUG", "Input identified as base64")
                    return pdf_bytes
            except (base64.binascii.Error, ValueError):
                pass

            # Check if URL
            if source.startswith('http://') or source.startswith('https://'):
                self._log("DEBUG", "Downloading PDF from URL: %s", source)
                resp = requests.get(source, timeout=self.timeout)
                if resp.status_code != 200:
                    raise ValueError(f"Failed to download PDF from URL: {source}")
                return resp.content

            # Check if file path
            if os.path.isfile(source):
                self._log("DEBUG", "Reading file: %s", source)
                with open(source, 'rb') as f:
                    return f.read()

            raise ValueError("Provided string is not a valid file path, base64, or URL.")

        raise TypeError("Input must be a file path, bytes, URL, or base64 string.")

    def _retry_process_with_pdf(self, pdf_base64: str, page_index: int) -> dict:
        """Processes page using PDF format as fallback."""
        self._log("WARNING", "Trying to process page %s with PDF format", page_index)

        pdf_bytes = base64.b64decode(pdf_base64)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(pdf_bytes)
            tmp_file_path = tmp_file.name

        try:
            with open(tmp_file_path, "rb") as f:
                upload_response = openai.files.create(file=f, purpose="user_data")
        finally:
            os.remove(tmp_file_path)

        llm_retry = init_chat_model(f"openai:{self.model}")

        message = {
            "role": "user",
            "content": [
                {
                    "type": "file",
                    "file": {
                        "file_id": upload_response.id,
                    }
                },
                {
                    "type": "text",
                    "text": "Transcribe the text from the provided image in markdown format, without omitting any text."
                }
            ],
        }

        response = llm_retry.invoke([SystemMessage(content=self.system_prompt), message])
        result = getattr(response, "content", str(response))
        formatted_result = result.replace('```markdown', '').replace('```', '')

        # Token counting (input: prompt + file, output: result)
        prompt_text = (
            self.system_prompt + "\n" + "Transcribe the text from the provided image in markdown format, without omitting any text."
        )

        input_tokens = self._count_tokens(prompt_text)
        output_tokens = self._count_tokens(formatted_result)
        total_tokens = input_tokens + output_tokens

        self.tokens_usage['input'] += input_tokens
        self.tokens_usage['output'] += output_tokens
        self.tokens_usage['total'] += total_tokens
        self.tokens_usage['details'].append({
            'page': page_index,
            'input': input_tokens,
            'output': output_tokens,
            'total': total_tokens,
            'fallback_pdf': True
        })

        self._log("DEBUG", "Page %s processed successfully", page_index)

        return {
            'page': page_index,
            'data': formatted_result
        }

    def _count_tokens(self, text: str, encoding_name: str = "cl100k_base") -> int:
        """Count tokens in a string using tiktoken."""
        enc = tiktoken.get_encoding(encoding_name)
        return len(enc.encode(text))

    def _process_image(self, data: dict, pages_base64: list) -> dict:
        """Processes a single image page."""
        page_num = data.get("pagina")
        self._log("DEBUG", "Processing page: %s", page_num)

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(
                content=[
                    {"type": "text", "text": "Transcribe the text from the provided image in markdown format, without omitting any text."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{data.get('data')}"
                        }
                    },
                ]
            )
        ]

        try:
            response = self.llm.invoke(messages)
        except APITimeoutError:
            self._log("WARNING", "Timeout on page %s - Trying with PDF", page_num)
            pdf_base64 = pages_base64[page_num]
            return self._retry_process_with_pdf(pdf_base64, page_num)

        result = getattr(response, "content", str(response))
        formatted_result = result.replace('```markdown', '').replace('```', '')

        # Token counting (input: prompt + image, output: result)
        prompt_text = (
            self.system_prompt + "\n" + "Transcribe the text from the provided image in markdown format, without omitting any text."
        )

        input_tokens = self._count_tokens(prompt_text)
        output_tokens = self._count_tokens(formatted_result)
        total_tokens = input_tokens + output_tokens

        self.tokens_usage['input'] += input_tokens
        self.tokens_usage['output'] += output_tokens
        self.tokens_usage['total'] += total_tokens
        self.tokens_usage['details'].append({
            'page': page_num,
            'input': input_tokens,
            'output': output_tokens,
            'total': total_tokens
        })

        self._log("DEBUG", "Page %s processed successfully", page_num)

        return {
            'page': page_num,
            'data': formatted_result
        }

    def dig(self, pdf_input: Union[str, bytes]) -> str:
        """
        Main method to transcribe PDF to markdown.

        Args:
            pdf_input: PDF input (file_path, bytes, URL, or base64)

        Returns:
            Markdown string with the PDF transcription
        """
        self._log("INFO", "Starting PDF to Markdown conversion process")

        try:
            pdf_bytes = self._get_pdf_bytes(pdf_input)
            self._log("INFO", "PDF loaded successfully - %d bytes", len(pdf_bytes))
        except Exception as e:
            self._log("ERROR", "Error getting PDF bytes: %s", e)
            raise RuntimeError(f"Error getting PDF bytes: {e}") from e

        temp_pdf_path = None
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(pdf_bytes)
                temp_pdf_path = tmp_file.name

            self._log("DEBUG", "Temporary file created: %s", temp_pdf_path)

            # Extract images and pages
            img_b64_list = pdf_to_image_base64_list(temp_pdf_path)
            pages_base64 = pdf_to_pages_base64(temp_pdf_path)

            self._log("INFO", "Extracted %d pages from PDF", len(img_b64_list))

        finally:
            # Clean up temporary file
            if temp_pdf_path and os.path.exists(temp_pdf_path):
                try:
                    os.remove(temp_pdf_path)
                    self._log("DEBUG", "Temporary file removed")
                except OSError as e:
                    self._log("WARNING", "Error removing temporary file: %s", e)

        # Prepare page data
        pages = [
            {'pagina': index, 'data': bytes64}
            for index, bytes64 in enumerate(img_b64_list)
        ]

        self._log("INFO", "Starting parallel processing with %d workers", self.max_workers)

        # Parallel processing
        transcribed_pages = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self._process_image, page, pages_base64)
                for page in pages
            ]

            for future in as_completed(futures):
                try:
                    result = future.result()
                    transcribed_pages.append(result)
                    self._log(
                        "DEBUG", "Page %s transcribed", result.get('page', result.get('pagina'))
                    )
                except Exception as e:
                    self._log("ERROR", "Error processing page: %s", e)

        # Sort pages and concatenate result
        transcribed_pages.sort(key=lambda x: x.get('page', x.get('pagina')))

        transcription = ''
        for page in transcribed_pages:
            transcription += page['data'] + '\n'

        self._log("INFO", "Conversion completed - %d characters generated", len(transcription))

        return transcription


# Compatibility function to maintain previous API

def pdf_to_markdown(
    pdf_input: Union[str, bytes],
    callbacks: Optional[list[Callable[..., Any]]] = None
) -> str:
    """
    Compatibility function to maintain the previous API.
    """
    converter = ScavToMarkdown(callbacks=callbacks)
    return converter.dig(pdf_input)
