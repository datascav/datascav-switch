class ModelIncompatibilityError(Exception):
    """
    Exception raised when the model is not compatible with the PDF parsing.
    """


class PDFProcessingError(Exception):
    """
    Exception raised when there's an error processing the PDF file.
    """


class InvalidInputError(Exception):
    """
    Exception raised when the input provided is invalid or unsupported.
    """
