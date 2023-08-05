from fileformats.core.mark import converter
from .converters.archive import (
    extract_tar,
    extract_zip,
)
from fileformats.core import BaseFile, BaseDirectory
from .archive import Zip, Tar, TarGz

# Basic formats


class File(BaseFile):
    @classmethod
    @converter(Zip)
    def unzip(cls, fs_path):
        node = extract_zip(in_file=fs_path)
        return node, node.lzout.out_file

    @classmethod
    @converter(Tar)
    def untar(cls, fs_path):
        node = extract_tar(in_file=fs_path)
        return node, node.lzout.out_file

    @classmethod
    @converter(TarGz)
    def untargz(cls, fs_path):
        node = extract_tar(in_file=fs_path)
        return node, node.lzout.out_file


class Directory(BaseDirectory):
    @classmethod
    @converter(Zip)
    def unzip(cls, fs_path):
        node = extract_zip(in_file=fs_path)
        return node, node.lzout.out_file

    @classmethod
    @converter(Tar)
    def untar(cls, fs_path):
        node = extract_tar(in_file=fs_path)
        return node, node.lzout.out_file

    @classmethod
    @converter(TarGz)
    def untargz(cls, fs_path):
        node = extract_tar(in_file=fs_path)
        return node, node.lzout.out_file
