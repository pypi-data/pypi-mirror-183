import zipfile
from fileformats.core.base import FileGroup
from fileformats.core.file import BaseFile
from fileformats.core.mark import converter
from .converters.archive import (
    create_tar,
    create_zip,
)


# Compressed formats
class Zip(BaseFile):
    ext = "zip"

    @classmethod
    @converter(FileGroup)
    def archive(cls, fs_path):
        node = create_zip(in_file=fs_path, compression=zipfile.ZIP_DEFLATED)
        return node, node.lzout.out_file


class Gzip(BaseFile):
    ext = "gz"

    @classmethod
    @converter(FileGroup)
    def archive(cls, fs_path):
        raise NotImplementedError


class Tar(BaseFile):
    ext = "tar"

    @classmethod
    @converter(FileGroup)
    def archive(cls, fs_path):
        node = create_tar(in_file=fs_path, compression="")
        return node, node.lzout.out_file


class TarGz(Tar, Gzip):
    ext = "tar.gz"

    @classmethod
    @converter(FileGroup)
    def archive(cls, fs_path):
        node = create_tar(in_file=fs_path, compression="gz")
        return node, node.lzout.out_file
