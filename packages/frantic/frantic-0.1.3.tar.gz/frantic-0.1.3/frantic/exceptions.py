"""Exceptions"""


class FranticException(Exception):
    """A base for all Frantic Exceptions"""


class AlreadyExists(FranticException):
    """Raised on document conflict"""

    def __init__(self, document_id: str | None):
        self.document_id = document_id
        super().__init__(f"Document with id {self.document_id} already exists")
