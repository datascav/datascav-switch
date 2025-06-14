import base64
from typing import List

import fitz


def pdf_to_image_base64_list(pdf_path: str, zoom: float = 2.0) -> List[str]:
    """
    Reads a PDF file and returns a list of base64 strings of PNG images, one for each page.

    Parameters:
    - pdf_path: Path to the PDF file.
    - zoom: Zoom factor for image rendering (default = 2.0).

    Returns:
    - List of base64 strings of PNG images, in the order of the PDF pages.
    """
    images_base64 = []
    try:
        pdf_document = fitz.open(pdf_path)
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            matrix = fitz.Matrix(zoom, zoom)
            pixmap = page.get_pixmap(matrix=matrix)
            image_bytes = pixmap.tobytes(output="png")
            image_base64 = base64.b64encode(image_bytes)
            image_base64 = image_base64.decode('utf-8')
            images_base64.append(image_base64)
        pdf_document.close()
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return []
    return images_base64


def pdf_to_pages_base64(pdf_path: str) -> list:
    """
    Reads a PDF file and returns a list of base64 strings, each representing a single page of the PDF as an individual PDF file.

    Parameters:
    - pdf_path: Path to the PDF file.

    Returns:
    - List of base64 strings, each representing a single page of the PDF.
    """
    pages_base64 = []
    try:
        pdf_document = fitz.open(pdf_path)
        for page_number in range(pdf_document.page_count):
            single_page_pdf = fitz.open()  # create a new empty PDF
            single_page_pdf.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)
            buffer = single_page_pdf.write()
            page_base64 = base64.b64encode(buffer).decode('utf-8')
            pages_base64.append(page_base64)
            single_page_pdf.close()
        pdf_document.close()
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return []
    return pages_base64
