from .base import File


# General formats
class Text(File):
    ext = "txt"


class Csv(File):
    ext = "csv"


class Tsv(File):
    ext = "tsv"


class HierarchicalText(File):
    pass


class Json(HierarchicalText):
    ext = "json"


class Yaml(HierarchicalText):
    ext = "yml"
