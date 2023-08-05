# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'ExternalKind',
]


@unique
class ExternalKind(IntEnum):
    Function = lib.BinaryenExternalFunction()
    Global = lib.BinaryenExternalGlobal()
    Memory = lib.BinaryenExternalMemory()
    Table = lib.BinaryenExternalTable()
    Tag = lib.BinaryenExternalTag()
