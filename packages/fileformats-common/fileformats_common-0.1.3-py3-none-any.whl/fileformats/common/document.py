from abc import ABCMeta
from .base import File


# Document formats
class Document(File, metaclass=ABCMeta):
    pass


class Pdf(Document):
    ext = "pdf"
