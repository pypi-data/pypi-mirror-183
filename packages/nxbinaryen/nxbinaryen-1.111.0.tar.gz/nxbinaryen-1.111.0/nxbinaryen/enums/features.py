# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntFlag, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'Feature',
]


@unique
class Feature(IntFlag):
    All = lib.BinaryenFeatureAll()
    Atomics = lib.BinaryenFeatureAtomics()
    BulkMemory = lib.BinaryenFeatureBulkMemory()
    ExceptionHandling = lib.BinaryenFeatureExceptionHandling()
    ExtendedConst = lib.BinaryenFeatureExtendedConst()
    GC = lib.BinaryenFeatureGC()
    MVP = lib.BinaryenFeatureMVP()
    Memory64 = lib.BinaryenFeatureMemory64()
    MultiMemories = lib.BinaryenFeatureMultiMemories()
    Multivalue = lib.BinaryenFeatureMultivalue()
    MutableGlobals = lib.BinaryenFeatureMutableGlobals()
    NontrappingFPToInt = lib.BinaryenFeatureNontrappingFPToInt()
    ReferenceTypes = lib.BinaryenFeatureReferenceTypes()
    RelaxedSIMD = lib.BinaryenFeatureRelaxedSIMD()
    SIMD128 = lib.BinaryenFeatureSIMD128()
    SignExt = lib.BinaryenFeatureSignExt()
    Strings = lib.BinaryenFeatureStrings()
    TailCall = lib.BinaryenFeatureTailCall()
