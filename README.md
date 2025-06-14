# datascav-switch

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/langchain-ecosystem-blueviolet)](https://github.com/langchain-ai/langchain)
[![OpenAI](https://img.shields.io/badge/openai-required-important)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**datascav-switch** is a Python package for intelligent document format conversion, leveraging generative AI (OpenAI) and a scalable architecture. This project is part of a suite of tools for automation, data extraction, and transformation.

---

## Main Features

- PDF to Markdown conversion with layout preservation
- Support for multiple input formats (file, URL, base64, bytes)
- Parallel processing and dynamic logging
- Detailed token tracking
- Native integration with [LangChain](https://github.com/langchain-ai/langchain) and tracing via LangSmith

---

## Installation

```bash
pip install datascav-switch
```

> **Requirements:**
> - Python 3.10+
> - OpenAI API key (`OPENAI_API_KEY`)

---

## Quick Start

```python
from scav_switch.converters.pdf import ScavToMarkdown
scav = ScavToMarkdown(model='gpt-4.1', verbose=True)
markdown = scav.dig('/path/to/file.pdf')
print(markdown)
```

For complete examples and detailed documentation, see the [`docs/`](docs/) folder and the notebooks for each module.

---

## Documentation

- Detailed documentation and usage examples are available in each [`docs/`](docs/) subfolder, including notebooks such as [`docs/conveters/pdf/ScavToMarkdown/ScavToMarkdown.ipynb`](docs/conveters/pdf/ScavToMarkdown/ScavToMarkdown.ipynb).
- Also check the [official LangChain documentation](https://github.com/langchain-ai/langchain) for advanced integration.

---

## License

MIT
