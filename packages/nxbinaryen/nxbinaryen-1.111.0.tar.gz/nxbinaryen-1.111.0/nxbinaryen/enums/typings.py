# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntEnum, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'Type',
]


@unique
class Type(IntEnum):
    Anyref = lib.BinaryenTypeAnyref()
    Arrayref = lib.BinaryenTypeArrayref()
    Auto = lib.BinaryenTypeAuto()
    Dataref = lib.BinaryenTypeDataref()
    Eqref = lib.BinaryenTypeEqref()
    Externref = lib.BinaryenTypeExternref()
    Float32 = lib.BinaryenTypeFloat32()
    Float64 = lib.BinaryenTypeFloat64()
    Funcref = lib.BinaryenTypeFuncref()
    I31ref = lib.BinaryenTypeI31ref()
    Int32 = lib.BinaryenTypeInt32()
    Int64 = lib.BinaryenTypeInt64()
    None_ = lib.BinaryenTypeNone()
    NullExternref = lib.BinaryenTypeNullExternref()
    NullFuncref = lib.BinaryenTypeNullFuncref()
    Nullref = lib.BinaryenTypeNullref()
    Stringref = lib.BinaryenTypeStringref()
    StringviewIter = lib.BinaryenTypeStringviewIter()
    StringviewWTF16 = lib.BinaryenTypeStringviewWTF16()
    StringviewWTF8 = lib.BinaryenTypeStringviewWTF8()
    Unreachable = lib.BinaryenTypeUnreachable()
    Vec128 = lib.BinaryenTypeVec128()
