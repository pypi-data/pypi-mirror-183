from ._version import __version__
from .base import File, Directory
from .archive import (
    Zip,
    Gzip,
    Tar,
    TarGz,
)
from .text import (
    Text,
    Csv,
    Tsv,
    Json,
    Yaml,
)
from .image import (
    Gif,
    Png,
    Jpeg,
)
from .numeric import (
    TextMatrix,
    RFile,
    MatlabMatrix,
)
from .document import (
    Pdf,
)
