# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from enum import IntFlag, unique

from nxbinaryen.binaryen import lib

__all__ = [
    'SideEffect',
]


@unique
class SideEffect(IntFlag):
    Any = lib.BinaryenSideEffectAny()
    Branches = lib.BinaryenSideEffectBranches()
    Calls = lib.BinaryenSideEffectCalls()
    DanglingPop = lib.BinaryenSideEffectDanglingPop()
    ImplicitTrap = lib.BinaryenSideEffectImplicitTrap()
    IsAtomic = lib.BinaryenSideEffectIsAtomic()
    None_ = lib.BinaryenSideEffectNone()
    ReadsGlobal = lib.BinaryenSideEffectReadsGlobal()
    ReadsLocal = lib.BinaryenSideEffectReadsLocal()
    ReadsMemory = lib.BinaryenSideEffectReadsMemory()
    ReadsTable = lib.BinaryenSideEffectReadsTable()
    Throws = lib.BinaryenSideEffectThrows()
    TrapsNeverHappen = lib.BinaryenSideEffectTrapsNeverHappen()
    WritesGlobal = lib.BinaryenSideEffectWritesGlobal()
    WritesLocal = lib.BinaryenSideEffectWritesLocal()
    WritesMemory = lib.BinaryenSideEffectWritesMemory()
    WritesTable = lib.BinaryenSideEffectWritesTable()
