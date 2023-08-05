# *** DO NOT EDIT ***
# Auto-generated from binaryen-c.h
from typing import List, Any, Optional, Tuple

from nxbinaryen.binaryen import ffi, lib
from nxbinaryen.capi.utils import *

BinaryenIndex = int
BinaryenType = int
BinaryenPackedType = int
BinaryenHeapType = int
BinaryenTypeSystem = int
BinaryenExpressionId = int
BinaryenExternalKind = int
BinaryenFeatures = int
BinaryenModuleRef = int
BinaryenLiteral = Any  # struct
BinaryenOp = int
BinaryenExpressionRef = int
BinaryenFunctionRef = int
BinaryenMemoryRef = int
BinaryenExportRef = int
BinaryenGlobalRef = int
BinaryenTagRef = int
BinaryenTableRef = int
BinaryenElementSegmentRef = int
BinaryenBufferSizes = Any  # struct
BinaryenModuleAllocateAndWriteResult = Any  # struct
BinaryenSideEffects = int
RelooperRef = int
RelooperBlockRef = int
ExpressionRunnerRef = int
ExpressionRunnerFlags = int
TypeBuilderRef = int
TypeBuilderErrorReason = int
BinaryenBasicHeapType = int


def TypeNone() -> BinaryenType:
    return lib.BinaryenTypeNone()


BinaryenTypeNone = TypeNone


def TypeInt32() -> BinaryenType:
    return lib.BinaryenTypeInt32()


BinaryenTypeInt32 = TypeInt32


def TypeInt64() -> BinaryenType:
    return lib.BinaryenTypeInt64()


BinaryenTypeInt64 = TypeInt64


def TypeFloat32() -> BinaryenType:
    return lib.BinaryenTypeFloat32()


BinaryenTypeFloat32 = TypeFloat32


def TypeFloat64() -> BinaryenType:
    return lib.BinaryenTypeFloat64()


BinaryenTypeFloat64 = TypeFloat64


def TypeVec128() -> BinaryenType:
    return lib.BinaryenTypeVec128()


BinaryenTypeVec128 = TypeVec128


def TypeFuncref() -> BinaryenType:
    return lib.BinaryenTypeFuncref()


BinaryenTypeFuncref = TypeFuncref


def TypeExternref() -> BinaryenType:
    return lib.BinaryenTypeExternref()


BinaryenTypeExternref = TypeExternref


def TypeAnyref() -> BinaryenType:
    return lib.BinaryenTypeAnyref()


BinaryenTypeAnyref = TypeAnyref


def TypeEqref() -> BinaryenType:
    return lib.BinaryenTypeEqref()


BinaryenTypeEqref = TypeEqref


def TypeI31ref() -> BinaryenType:
    return lib.BinaryenTypeI31ref()


BinaryenTypeI31ref = TypeI31ref


def TypeDataref() -> BinaryenType:
    return lib.BinaryenTypeDataref()


BinaryenTypeDataref = TypeDataref


def TypeArrayref() -> BinaryenType:
    return lib.BinaryenTypeArrayref()


BinaryenTypeArrayref = TypeArrayref


def TypeStringref() -> BinaryenType:
    return lib.BinaryenTypeStringref()


BinaryenTypeStringref = TypeStringref


def TypeStringviewWTF8() -> BinaryenType:
    return lib.BinaryenTypeStringviewWTF8()


BinaryenTypeStringviewWTF8 = TypeStringviewWTF8


def TypeStringviewWTF16() -> BinaryenType:
    return lib.BinaryenTypeStringviewWTF16()


BinaryenTypeStringviewWTF16 = TypeStringviewWTF16


def TypeStringviewIter() -> BinaryenType:
    return lib.BinaryenTypeStringviewIter()


BinaryenTypeStringviewIter = TypeStringviewIter


def TypeNullref() -> BinaryenType:
    return lib.BinaryenTypeNullref()


BinaryenTypeNullref = TypeNullref


def TypeNullExternref() -> BinaryenType:
    return lib.BinaryenTypeNullExternref()


BinaryenTypeNullExternref = TypeNullExternref


def TypeNullFuncref() -> BinaryenType:
    return lib.BinaryenTypeNullFuncref()


BinaryenTypeNullFuncref = TypeNullFuncref


def TypeUnreachable() -> BinaryenType:
    return lib.BinaryenTypeUnreachable()


BinaryenTypeUnreachable = TypeUnreachable


def TypeAuto() -> BinaryenType:
    """
    Not a real type. Used as the last parameter to BinaryenBlock to let
    the API figure out the type instead of providing one.
    """
    return lib.BinaryenTypeAuto()


BinaryenTypeAuto = TypeAuto


def TypeCreate(
    value_types: List[BinaryenType],
) -> BinaryenType:
    return lib.BinaryenTypeCreate(value_types, _len(value_types))


BinaryenTypeCreate = TypeCreate


def TypeArity(
    t: BinaryenType,
) -> int:
    return lib.BinaryenTypeArity(t)


BinaryenTypeArity = TypeArity


def TypeExpand(
    t: BinaryenType,
) -> List[BinaryenType]:
    dim = lib.BinaryenTypeArity(t)
    buf = ffi.new(f'BinaryenType[{dim}]')
    lib.BinaryenTypeExpand(t, buf)
    return list(buf)


BinaryenTypeExpand = TypeExpand


def PackedTypeNotPacked() -> BinaryenPackedType:
    return lib.BinaryenPackedTypeNotPacked()


BinaryenPackedTypeNotPacked = PackedTypeNotPacked


def PackedTypeInt8() -> BinaryenPackedType:
    return lib.BinaryenPackedTypeInt8()


BinaryenPackedTypeInt8 = PackedTypeInt8


def PackedTypeInt16() -> BinaryenPackedType:
    return lib.BinaryenPackedTypeInt16()


BinaryenPackedTypeInt16 = PackedTypeInt16


def HeapTypeExt() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeExt()


BinaryenHeapTypeExt = HeapTypeExt


def HeapTypeFunc() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeFunc()


BinaryenHeapTypeFunc = HeapTypeFunc


def HeapTypeAny() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeAny()


BinaryenHeapTypeAny = HeapTypeAny


def HeapTypeEq() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeEq()


BinaryenHeapTypeEq = HeapTypeEq


def HeapTypeI31() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeI31()


BinaryenHeapTypeI31 = HeapTypeI31


def HeapTypeData() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeData()


BinaryenHeapTypeData = HeapTypeData


def HeapTypeArray() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeArray()


BinaryenHeapTypeArray = HeapTypeArray


def HeapTypeString() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeString()


BinaryenHeapTypeString = HeapTypeString


def HeapTypeStringviewWTF8() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeStringviewWTF8()


BinaryenHeapTypeStringviewWTF8 = HeapTypeStringviewWTF8


def HeapTypeStringviewWTF16() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeStringviewWTF16()


BinaryenHeapTypeStringviewWTF16 = HeapTypeStringviewWTF16


def HeapTypeStringviewIter() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeStringviewIter()


BinaryenHeapTypeStringviewIter = HeapTypeStringviewIter


def HeapTypeNone() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeNone()


BinaryenHeapTypeNone = HeapTypeNone


def HeapTypeNoext() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeNoext()


BinaryenHeapTypeNoext = HeapTypeNoext


def HeapTypeNofunc() -> BinaryenHeapType:
    return lib.BinaryenHeapTypeNofunc()


BinaryenHeapTypeNofunc = HeapTypeNofunc


def HeapTypeIsBasic(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsBasic(heap_type)


BinaryenHeapTypeIsBasic = HeapTypeIsBasic


def HeapTypeIsSignature(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsSignature(heap_type)


BinaryenHeapTypeIsSignature = HeapTypeIsSignature


def HeapTypeIsStruct(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsStruct(heap_type)


BinaryenHeapTypeIsStruct = HeapTypeIsStruct


def HeapTypeIsArray(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsArray(heap_type)


BinaryenHeapTypeIsArray = HeapTypeIsArray


def HeapTypeIsBottom(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsBottom(heap_type)


BinaryenHeapTypeIsBottom = HeapTypeIsBottom


def HeapTypeGetBottom(
    heap_type: BinaryenHeapType,
) -> BinaryenHeapType:
    return lib.BinaryenHeapTypeGetBottom(heap_type)


BinaryenHeapTypeGetBottom = HeapTypeGetBottom


def HeapTypeIsSubType(
    left: BinaryenHeapType,
    right: BinaryenHeapType,
) -> bool:
    return lib.BinaryenHeapTypeIsSubType(left, right)


BinaryenHeapTypeIsSubType = HeapTypeIsSubType


def StructTypeGetNumFields(
    heap_type: BinaryenHeapType,
) -> BinaryenIndex:
    return lib.BinaryenStructTypeGetNumFields(heap_type)


BinaryenStructTypeGetNumFields = StructTypeGetNumFields


def StructTypeGetFieldType(
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
) -> BinaryenType:
    return lib.BinaryenStructTypeGetFieldType(heap_type, index)


BinaryenStructTypeGetFieldType = StructTypeGetFieldType


def StructTypeGetFieldPackedType(
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
) -> BinaryenPackedType:
    return lib.BinaryenStructTypeGetFieldPackedType(heap_type, index)


BinaryenStructTypeGetFieldPackedType = StructTypeGetFieldPackedType


def StructTypeIsFieldMutable(
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
) -> bool:
    return lib.BinaryenStructTypeIsFieldMutable(heap_type, index)


BinaryenStructTypeIsFieldMutable = StructTypeIsFieldMutable


def ArrayTypeGetElementType(
    heap_type: BinaryenHeapType,
) -> BinaryenType:
    return lib.BinaryenArrayTypeGetElementType(heap_type)


BinaryenArrayTypeGetElementType = ArrayTypeGetElementType


def ArrayTypeGetElementPackedType(
    heap_type: BinaryenHeapType,
) -> BinaryenPackedType:
    return lib.BinaryenArrayTypeGetElementPackedType(heap_type)


BinaryenArrayTypeGetElementPackedType = ArrayTypeGetElementPackedType


def ArrayTypeIsElementMutable(
    heap_type: BinaryenHeapType,
) -> bool:
    return lib.BinaryenArrayTypeIsElementMutable(heap_type)


BinaryenArrayTypeIsElementMutable = ArrayTypeIsElementMutable


def SignatureTypeGetParams(
    heap_type: BinaryenHeapType,
) -> BinaryenType:
    return lib.BinaryenSignatureTypeGetParams(heap_type)


BinaryenSignatureTypeGetParams = SignatureTypeGetParams


def SignatureTypeGetResults(
    heap_type: BinaryenHeapType,
) -> BinaryenType:
    return lib.BinaryenSignatureTypeGetResults(heap_type)


BinaryenSignatureTypeGetResults = SignatureTypeGetResults


def TypeGetHeapType(
    _type: BinaryenType,
) -> BinaryenHeapType:
    return lib.BinaryenTypeGetHeapType(_type)


BinaryenTypeGetHeapType = TypeGetHeapType


def TypeIsNullable(
    _type: BinaryenType,
) -> bool:
    return lib.BinaryenTypeIsNullable(_type)


BinaryenTypeIsNullable = TypeIsNullable


def TypeFromHeapType(
    heap_type: BinaryenHeapType,
    nullable: bool,
) -> BinaryenType:
    return lib.BinaryenTypeFromHeapType(heap_type, nullable)


BinaryenTypeFromHeapType = TypeFromHeapType


def TypeSystemEquirecursive() -> BinaryenTypeSystem:
    return lib.BinaryenTypeSystemEquirecursive()


BinaryenTypeSystemEquirecursive = TypeSystemEquirecursive


def TypeSystemNominal() -> BinaryenTypeSystem:
    return lib.BinaryenTypeSystemNominal()


BinaryenTypeSystemNominal = TypeSystemNominal


def TypeSystemIsorecursive() -> BinaryenTypeSystem:
    return lib.BinaryenTypeSystemIsorecursive()


BinaryenTypeSystemIsorecursive = TypeSystemIsorecursive


def GetTypeSystem() -> BinaryenTypeSystem:
    return lib.BinaryenGetTypeSystem()


BinaryenGetTypeSystem = GetTypeSystem


def SetTypeSystem(
    type_system: BinaryenTypeSystem,
) -> None:
    lib.BinaryenSetTypeSystem(type_system)


BinaryenSetTypeSystem = SetTypeSystem


def InvalidId() -> BinaryenExpressionId:
    return lib.BinaryenInvalidId()


BinaryenInvalidId = InvalidId


def NopId() -> BinaryenExpressionId:
    return lib.BinaryenNopId()


BinaryenNopId = NopId


def BlockId() -> BinaryenExpressionId:
    return lib.BinaryenBlockId()


BinaryenBlockId = BlockId


def IfId() -> BinaryenExpressionId:
    return lib.BinaryenIfId()


BinaryenIfId = IfId


def LoopId() -> BinaryenExpressionId:
    return lib.BinaryenLoopId()


BinaryenLoopId = LoopId


def BreakId() -> BinaryenExpressionId:
    return lib.BinaryenBreakId()


BinaryenBreakId = BreakId


def SwitchId() -> BinaryenExpressionId:
    return lib.BinaryenSwitchId()


BinaryenSwitchId = SwitchId


def CallId() -> BinaryenExpressionId:
    return lib.BinaryenCallId()


BinaryenCallId = CallId


def CallIndirectId() -> BinaryenExpressionId:
    return lib.BinaryenCallIndirectId()


BinaryenCallIndirectId = CallIndirectId


def LocalGetId() -> BinaryenExpressionId:
    return lib.BinaryenLocalGetId()


BinaryenLocalGetId = LocalGetId


def LocalSetId() -> BinaryenExpressionId:
    return lib.BinaryenLocalSetId()


BinaryenLocalSetId = LocalSetId


def GlobalGetId() -> BinaryenExpressionId:
    return lib.BinaryenGlobalGetId()


BinaryenGlobalGetId = GlobalGetId


def GlobalSetId() -> BinaryenExpressionId:
    return lib.BinaryenGlobalSetId()


BinaryenGlobalSetId = GlobalSetId


def LoadId() -> BinaryenExpressionId:
    return lib.BinaryenLoadId()


BinaryenLoadId = LoadId


def StoreId() -> BinaryenExpressionId:
    return lib.BinaryenStoreId()


BinaryenStoreId = StoreId


def AtomicRMWId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicRMWId()


BinaryenAtomicRMWId = AtomicRMWId


def AtomicCmpxchgId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicCmpxchgId()


BinaryenAtomicCmpxchgId = AtomicCmpxchgId


def AtomicWaitId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicWaitId()


BinaryenAtomicWaitId = AtomicWaitId


def AtomicNotifyId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicNotifyId()


BinaryenAtomicNotifyId = AtomicNotifyId


def AtomicFenceId() -> BinaryenExpressionId:
    return lib.BinaryenAtomicFenceId()


BinaryenAtomicFenceId = AtomicFenceId


def SIMDExtractId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDExtractId()


BinaryenSIMDExtractId = SIMDExtractId


def SIMDReplaceId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDReplaceId()


BinaryenSIMDReplaceId = SIMDReplaceId


def SIMDShuffleId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDShuffleId()


BinaryenSIMDShuffleId = SIMDShuffleId


def SIMDTernaryId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDTernaryId()


BinaryenSIMDTernaryId = SIMDTernaryId


def SIMDShiftId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDShiftId()


BinaryenSIMDShiftId = SIMDShiftId


def SIMDLoadId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDLoadId()


BinaryenSIMDLoadId = SIMDLoadId


def SIMDLoadStoreLaneId() -> BinaryenExpressionId:
    return lib.BinaryenSIMDLoadStoreLaneId()


BinaryenSIMDLoadStoreLaneId = SIMDLoadStoreLaneId


def MemoryInitId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryInitId()


BinaryenMemoryInitId = MemoryInitId


def DataDropId() -> BinaryenExpressionId:
    return lib.BinaryenDataDropId()


BinaryenDataDropId = DataDropId


def MemoryCopyId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryCopyId()


BinaryenMemoryCopyId = MemoryCopyId


def MemoryFillId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryFillId()


BinaryenMemoryFillId = MemoryFillId


def ConstId() -> BinaryenExpressionId:
    return lib.BinaryenConstId()


BinaryenConstId = ConstId


def UnaryId() -> BinaryenExpressionId:
    return lib.BinaryenUnaryId()


BinaryenUnaryId = UnaryId


def BinaryId() -> BinaryenExpressionId:
    return lib.BinaryenBinaryId()


BinaryenBinaryId = BinaryId


def SelectId() -> BinaryenExpressionId:
    return lib.BinaryenSelectId()


BinaryenSelectId = SelectId


def DropId() -> BinaryenExpressionId:
    return lib.BinaryenDropId()


BinaryenDropId = DropId


def ReturnId() -> BinaryenExpressionId:
    return lib.BinaryenReturnId()


BinaryenReturnId = ReturnId


def MemorySizeId() -> BinaryenExpressionId:
    return lib.BinaryenMemorySizeId()


BinaryenMemorySizeId = MemorySizeId


def MemoryGrowId() -> BinaryenExpressionId:
    return lib.BinaryenMemoryGrowId()


BinaryenMemoryGrowId = MemoryGrowId


def UnreachableId() -> BinaryenExpressionId:
    return lib.BinaryenUnreachableId()


BinaryenUnreachableId = UnreachableId


def PopId() -> BinaryenExpressionId:
    return lib.BinaryenPopId()


BinaryenPopId = PopId


def RefNullId() -> BinaryenExpressionId:
    return lib.BinaryenRefNullId()


BinaryenRefNullId = RefNullId


def RefIsId() -> BinaryenExpressionId:
    return lib.BinaryenRefIsId()


BinaryenRefIsId = RefIsId


def RefFuncId() -> BinaryenExpressionId:
    return lib.BinaryenRefFuncId()


BinaryenRefFuncId = RefFuncId


def RefEqId() -> BinaryenExpressionId:
    return lib.BinaryenRefEqId()


BinaryenRefEqId = RefEqId


def TableGetId() -> BinaryenExpressionId:
    return lib.BinaryenTableGetId()


BinaryenTableGetId = TableGetId


def TableSetId() -> BinaryenExpressionId:
    return lib.BinaryenTableSetId()


BinaryenTableSetId = TableSetId


def TableSizeId() -> BinaryenExpressionId:
    return lib.BinaryenTableSizeId()


BinaryenTableSizeId = TableSizeId


def TableGrowId() -> BinaryenExpressionId:
    return lib.BinaryenTableGrowId()


BinaryenTableGrowId = TableGrowId


def TryId() -> BinaryenExpressionId:
    return lib.BinaryenTryId()


BinaryenTryId = TryId


def ThrowId() -> BinaryenExpressionId:
    return lib.BinaryenThrowId()


BinaryenThrowId = ThrowId


def RethrowId() -> BinaryenExpressionId:
    return lib.BinaryenRethrowId()


BinaryenRethrowId = RethrowId


def TupleMakeId() -> BinaryenExpressionId:
    return lib.BinaryenTupleMakeId()


BinaryenTupleMakeId = TupleMakeId


def TupleExtractId() -> BinaryenExpressionId:
    return lib.BinaryenTupleExtractId()


BinaryenTupleExtractId = TupleExtractId


def I31NewId() -> BinaryenExpressionId:
    return lib.BinaryenI31NewId()


BinaryenI31NewId = I31NewId


def I31GetId() -> BinaryenExpressionId:
    return lib.BinaryenI31GetId()


BinaryenI31GetId = I31GetId


def CallRefId() -> BinaryenExpressionId:
    return lib.BinaryenCallRefId()


BinaryenCallRefId = CallRefId


def RefTestId() -> BinaryenExpressionId:
    return lib.BinaryenRefTestId()


BinaryenRefTestId = RefTestId


def RefCastId() -> BinaryenExpressionId:
    return lib.BinaryenRefCastId()


BinaryenRefCastId = RefCastId


def BrOnId() -> BinaryenExpressionId:
    return lib.BinaryenBrOnId()


BinaryenBrOnId = BrOnId


def StructNewId() -> BinaryenExpressionId:
    return lib.BinaryenStructNewId()


BinaryenStructNewId = StructNewId


def StructGetId() -> BinaryenExpressionId:
    return lib.BinaryenStructGetId()


BinaryenStructGetId = StructGetId


def StructSetId() -> BinaryenExpressionId:
    return lib.BinaryenStructSetId()


BinaryenStructSetId = StructSetId


def ArrayNewId() -> BinaryenExpressionId:
    return lib.BinaryenArrayNewId()


BinaryenArrayNewId = ArrayNewId


def ArrayNewSegId() -> BinaryenExpressionId:
    return lib.BinaryenArrayNewSegId()


BinaryenArrayNewSegId = ArrayNewSegId


def ArrayInitId() -> BinaryenExpressionId:
    return lib.BinaryenArrayInitId()


BinaryenArrayInitId = ArrayInitId


def ArrayGetId() -> BinaryenExpressionId:
    return lib.BinaryenArrayGetId()


BinaryenArrayGetId = ArrayGetId


def ArraySetId() -> BinaryenExpressionId:
    return lib.BinaryenArraySetId()


BinaryenArraySetId = ArraySetId


def ArrayLenId() -> BinaryenExpressionId:
    return lib.BinaryenArrayLenId()


BinaryenArrayLenId = ArrayLenId


def ArrayCopyId() -> BinaryenExpressionId:
    return lib.BinaryenArrayCopyId()


BinaryenArrayCopyId = ArrayCopyId


def RefAsId() -> BinaryenExpressionId:
    return lib.BinaryenRefAsId()


BinaryenRefAsId = RefAsId


def StringNewId() -> BinaryenExpressionId:
    return lib.BinaryenStringNewId()


BinaryenStringNewId = StringNewId


def StringConstId() -> BinaryenExpressionId:
    return lib.BinaryenStringConstId()


BinaryenStringConstId = StringConstId


def StringMeasureId() -> BinaryenExpressionId:
    return lib.BinaryenStringMeasureId()


BinaryenStringMeasureId = StringMeasureId


def StringEncodeId() -> BinaryenExpressionId:
    return lib.BinaryenStringEncodeId()


BinaryenStringEncodeId = StringEncodeId


def StringConcatId() -> BinaryenExpressionId:
    return lib.BinaryenStringConcatId()


BinaryenStringConcatId = StringConcatId


def StringEqId() -> BinaryenExpressionId:
    return lib.BinaryenStringEqId()


BinaryenStringEqId = StringEqId


def StringAsId() -> BinaryenExpressionId:
    return lib.BinaryenStringAsId()


BinaryenStringAsId = StringAsId


def StringWTF8AdvanceId() -> BinaryenExpressionId:
    return lib.BinaryenStringWTF8AdvanceId()


BinaryenStringWTF8AdvanceId = StringWTF8AdvanceId


def StringWTF16GetId() -> BinaryenExpressionId:
    return lib.BinaryenStringWTF16GetId()


BinaryenStringWTF16GetId = StringWTF16GetId


def StringIterNextId() -> BinaryenExpressionId:
    return lib.BinaryenStringIterNextId()


BinaryenStringIterNextId = StringIterNextId


def StringIterMoveId() -> BinaryenExpressionId:
    return lib.BinaryenStringIterMoveId()


BinaryenStringIterMoveId = StringIterMoveId


def StringSliceWTFId() -> BinaryenExpressionId:
    return lib.BinaryenStringSliceWTFId()


BinaryenStringSliceWTFId = StringSliceWTFId


def StringSliceIterId() -> BinaryenExpressionId:
    return lib.BinaryenStringSliceIterId()


BinaryenStringSliceIterId = StringSliceIterId


def ExternalFunction() -> BinaryenExternalKind:
    return lib.BinaryenExternalFunction()


BinaryenExternalFunction = ExternalFunction


def ExternalTable() -> BinaryenExternalKind:
    return lib.BinaryenExternalTable()


BinaryenExternalTable = ExternalTable


def ExternalMemory() -> BinaryenExternalKind:
    return lib.BinaryenExternalMemory()


BinaryenExternalMemory = ExternalMemory


def ExternalGlobal() -> BinaryenExternalKind:
    return lib.BinaryenExternalGlobal()


BinaryenExternalGlobal = ExternalGlobal


def ExternalTag() -> BinaryenExternalKind:
    return lib.BinaryenExternalTag()


BinaryenExternalTag = ExternalTag


def FeatureMVP() -> BinaryenFeatures:
    return lib.BinaryenFeatureMVP()


BinaryenFeatureMVP = FeatureMVP


def FeatureAtomics() -> BinaryenFeatures:
    return lib.BinaryenFeatureAtomics()


BinaryenFeatureAtomics = FeatureAtomics


def FeatureBulkMemory() -> BinaryenFeatures:
    return lib.BinaryenFeatureBulkMemory()


BinaryenFeatureBulkMemory = FeatureBulkMemory


def FeatureMutableGlobals() -> BinaryenFeatures:
    return lib.BinaryenFeatureMutableGlobals()


BinaryenFeatureMutableGlobals = FeatureMutableGlobals


def FeatureNontrappingFPToInt() -> BinaryenFeatures:
    return lib.BinaryenFeatureNontrappingFPToInt()


BinaryenFeatureNontrappingFPToInt = FeatureNontrappingFPToInt


def FeatureSignExt() -> BinaryenFeatures:
    return lib.BinaryenFeatureSignExt()


BinaryenFeatureSignExt = FeatureSignExt


def FeatureSIMD128() -> BinaryenFeatures:
    return lib.BinaryenFeatureSIMD128()


BinaryenFeatureSIMD128 = FeatureSIMD128


def FeatureExceptionHandling() -> BinaryenFeatures:
    return lib.BinaryenFeatureExceptionHandling()


BinaryenFeatureExceptionHandling = FeatureExceptionHandling


def FeatureTailCall() -> BinaryenFeatures:
    return lib.BinaryenFeatureTailCall()


BinaryenFeatureTailCall = FeatureTailCall


def FeatureReferenceTypes() -> BinaryenFeatures:
    return lib.BinaryenFeatureReferenceTypes()


BinaryenFeatureReferenceTypes = FeatureReferenceTypes


def FeatureMultivalue() -> BinaryenFeatures:
    return lib.BinaryenFeatureMultivalue()


BinaryenFeatureMultivalue = FeatureMultivalue


def FeatureGC() -> BinaryenFeatures:
    return lib.BinaryenFeatureGC()


BinaryenFeatureGC = FeatureGC


def FeatureMemory64() -> BinaryenFeatures:
    return lib.BinaryenFeatureMemory64()


BinaryenFeatureMemory64 = FeatureMemory64


def FeatureRelaxedSIMD() -> BinaryenFeatures:
    return lib.BinaryenFeatureRelaxedSIMD()


BinaryenFeatureRelaxedSIMD = FeatureRelaxedSIMD


def FeatureExtendedConst() -> BinaryenFeatures:
    return lib.BinaryenFeatureExtendedConst()


BinaryenFeatureExtendedConst = FeatureExtendedConst


def FeatureStrings() -> BinaryenFeatures:
    return lib.BinaryenFeatureStrings()


BinaryenFeatureStrings = FeatureStrings


def FeatureMultiMemories() -> BinaryenFeatures:
    return lib.BinaryenFeatureMultiMemories()


BinaryenFeatureMultiMemories = FeatureMultiMemories


def FeatureAll() -> BinaryenFeatures:
    return lib.BinaryenFeatureAll()


BinaryenFeatureAll = FeatureAll


def ModuleCreate() -> BinaryenModuleRef:
    return lib.BinaryenModuleCreate()


BinaryenModuleCreate = ModuleCreate


def ModuleDispose(
    module: BinaryenModuleRef,
) -> None:
    lib.BinaryenModuleDispose(module)


BinaryenModuleDispose = ModuleDispose


def LiteralInt32(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralInt32(x)


BinaryenLiteralInt32 = LiteralInt32


def LiteralInt64(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralInt64(x)


BinaryenLiteralInt64 = LiteralInt64


def LiteralFloat32(
    x: float,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat32(x)


BinaryenLiteralFloat32 = LiteralFloat32


def LiteralFloat64(
    x: float,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat64(x)


BinaryenLiteralFloat64 = LiteralFloat64


def LiteralVec128(
    x: List[int],
) -> BinaryenLiteral:
    return lib.BinaryenLiteralVec128(x)


BinaryenLiteralVec128 = LiteralVec128


def LiteralFloat32Bits(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat32Bits(x)


BinaryenLiteralFloat32Bits = LiteralFloat32Bits


def LiteralFloat64Bits(
    x: int,
) -> BinaryenLiteral:
    return lib.BinaryenLiteralFloat64Bits(x)


BinaryenLiteralFloat64Bits = LiteralFloat64Bits


def ClzInt32() -> BinaryenOp:
    return lib.BinaryenClzInt32()


BinaryenClzInt32 = ClzInt32


def CtzInt32() -> BinaryenOp:
    return lib.BinaryenCtzInt32()


BinaryenCtzInt32 = CtzInt32


def PopcntInt32() -> BinaryenOp:
    return lib.BinaryenPopcntInt32()


BinaryenPopcntInt32 = PopcntInt32


def NegFloat32() -> BinaryenOp:
    return lib.BinaryenNegFloat32()


BinaryenNegFloat32 = NegFloat32


def AbsFloat32() -> BinaryenOp:
    return lib.BinaryenAbsFloat32()


BinaryenAbsFloat32 = AbsFloat32


def CeilFloat32() -> BinaryenOp:
    return lib.BinaryenCeilFloat32()


BinaryenCeilFloat32 = CeilFloat32


def FloorFloat32() -> BinaryenOp:
    return lib.BinaryenFloorFloat32()


BinaryenFloorFloat32 = FloorFloat32


def TruncFloat32() -> BinaryenOp:
    return lib.BinaryenTruncFloat32()


BinaryenTruncFloat32 = TruncFloat32


def NearestFloat32() -> BinaryenOp:
    return lib.BinaryenNearestFloat32()


BinaryenNearestFloat32 = NearestFloat32


def SqrtFloat32() -> BinaryenOp:
    return lib.BinaryenSqrtFloat32()


BinaryenSqrtFloat32 = SqrtFloat32


def EqZInt32() -> BinaryenOp:
    return lib.BinaryenEqZInt32()


BinaryenEqZInt32 = EqZInt32


def ClzInt64() -> BinaryenOp:
    return lib.BinaryenClzInt64()


BinaryenClzInt64 = ClzInt64


def CtzInt64() -> BinaryenOp:
    return lib.BinaryenCtzInt64()


BinaryenCtzInt64 = CtzInt64


def PopcntInt64() -> BinaryenOp:
    return lib.BinaryenPopcntInt64()


BinaryenPopcntInt64 = PopcntInt64


def NegFloat64() -> BinaryenOp:
    return lib.BinaryenNegFloat64()


BinaryenNegFloat64 = NegFloat64


def AbsFloat64() -> BinaryenOp:
    return lib.BinaryenAbsFloat64()


BinaryenAbsFloat64 = AbsFloat64


def CeilFloat64() -> BinaryenOp:
    return lib.BinaryenCeilFloat64()


BinaryenCeilFloat64 = CeilFloat64


def FloorFloat64() -> BinaryenOp:
    return lib.BinaryenFloorFloat64()


BinaryenFloorFloat64 = FloorFloat64


def TruncFloat64() -> BinaryenOp:
    return lib.BinaryenTruncFloat64()


BinaryenTruncFloat64 = TruncFloat64


def NearestFloat64() -> BinaryenOp:
    return lib.BinaryenNearestFloat64()


BinaryenNearestFloat64 = NearestFloat64


def SqrtFloat64() -> BinaryenOp:
    return lib.BinaryenSqrtFloat64()


BinaryenSqrtFloat64 = SqrtFloat64


def EqZInt64() -> BinaryenOp:
    return lib.BinaryenEqZInt64()


BinaryenEqZInt64 = EqZInt64


def ExtendSInt32() -> BinaryenOp:
    return lib.BinaryenExtendSInt32()


BinaryenExtendSInt32 = ExtendSInt32


def ExtendUInt32() -> BinaryenOp:
    return lib.BinaryenExtendUInt32()


BinaryenExtendUInt32 = ExtendUInt32


def WrapInt64() -> BinaryenOp:
    return lib.BinaryenWrapInt64()


BinaryenWrapInt64 = WrapInt64


def TruncSFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSFloat32ToInt32()


BinaryenTruncSFloat32ToInt32 = TruncSFloat32ToInt32


def TruncSFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSFloat32ToInt64()


BinaryenTruncSFloat32ToInt64 = TruncSFloat32ToInt64


def TruncUFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncUFloat32ToInt32()


BinaryenTruncUFloat32ToInt32 = TruncUFloat32ToInt32


def TruncUFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncUFloat32ToInt64()


BinaryenTruncUFloat32ToInt64 = TruncUFloat32ToInt64


def TruncSFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSFloat64ToInt32()


BinaryenTruncSFloat64ToInt32 = TruncSFloat64ToInt32


def TruncSFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSFloat64ToInt64()


BinaryenTruncSFloat64ToInt64 = TruncSFloat64ToInt64


def TruncUFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncUFloat64ToInt32()


BinaryenTruncUFloat64ToInt32 = TruncUFloat64ToInt32


def TruncUFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncUFloat64ToInt64()


BinaryenTruncUFloat64ToInt64 = TruncUFloat64ToInt64


def ReinterpretFloat32() -> BinaryenOp:
    return lib.BinaryenReinterpretFloat32()


BinaryenReinterpretFloat32 = ReinterpretFloat32


def ReinterpretFloat64() -> BinaryenOp:
    return lib.BinaryenReinterpretFloat64()


BinaryenReinterpretFloat64 = ReinterpretFloat64


def ConvertSInt32ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertSInt32ToFloat32()


BinaryenConvertSInt32ToFloat32 = ConvertSInt32ToFloat32


def ConvertSInt32ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertSInt32ToFloat64()


BinaryenConvertSInt32ToFloat64 = ConvertSInt32ToFloat64


def ConvertUInt32ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertUInt32ToFloat32()


BinaryenConvertUInt32ToFloat32 = ConvertUInt32ToFloat32


def ConvertUInt32ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertUInt32ToFloat64()


BinaryenConvertUInt32ToFloat64 = ConvertUInt32ToFloat64


def ConvertSInt64ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertSInt64ToFloat32()


BinaryenConvertSInt64ToFloat32 = ConvertSInt64ToFloat32


def ConvertSInt64ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertSInt64ToFloat64()


BinaryenConvertSInt64ToFloat64 = ConvertSInt64ToFloat64


def ConvertUInt64ToFloat32() -> BinaryenOp:
    return lib.BinaryenConvertUInt64ToFloat32()


BinaryenConvertUInt64ToFloat32 = ConvertUInt64ToFloat32


def ConvertUInt64ToFloat64() -> BinaryenOp:
    return lib.BinaryenConvertUInt64ToFloat64()


BinaryenConvertUInt64ToFloat64 = ConvertUInt64ToFloat64


def PromoteFloat32() -> BinaryenOp:
    return lib.BinaryenPromoteFloat32()


BinaryenPromoteFloat32 = PromoteFloat32


def DemoteFloat64() -> BinaryenOp:
    return lib.BinaryenDemoteFloat64()


BinaryenDemoteFloat64 = DemoteFloat64


def ReinterpretInt32() -> BinaryenOp:
    return lib.BinaryenReinterpretInt32()


BinaryenReinterpretInt32 = ReinterpretInt32


def ReinterpretInt64() -> BinaryenOp:
    return lib.BinaryenReinterpretInt64()


BinaryenReinterpretInt64 = ReinterpretInt64


def ExtendS8Int32() -> BinaryenOp:
    return lib.BinaryenExtendS8Int32()


BinaryenExtendS8Int32 = ExtendS8Int32


def ExtendS16Int32() -> BinaryenOp:
    return lib.BinaryenExtendS16Int32()


BinaryenExtendS16Int32 = ExtendS16Int32


def ExtendS8Int64() -> BinaryenOp:
    return lib.BinaryenExtendS8Int64()


BinaryenExtendS8Int64 = ExtendS8Int64


def ExtendS16Int64() -> BinaryenOp:
    return lib.BinaryenExtendS16Int64()


BinaryenExtendS16Int64 = ExtendS16Int64


def ExtendS32Int64() -> BinaryenOp:
    return lib.BinaryenExtendS32Int64()


BinaryenExtendS32Int64 = ExtendS32Int64


def AddInt32() -> BinaryenOp:
    return lib.BinaryenAddInt32()


BinaryenAddInt32 = AddInt32


def SubInt32() -> BinaryenOp:
    return lib.BinaryenSubInt32()


BinaryenSubInt32 = SubInt32


def MulInt32() -> BinaryenOp:
    return lib.BinaryenMulInt32()


BinaryenMulInt32 = MulInt32


def DivSInt32() -> BinaryenOp:
    return lib.BinaryenDivSInt32()


BinaryenDivSInt32 = DivSInt32


def DivUInt32() -> BinaryenOp:
    return lib.BinaryenDivUInt32()


BinaryenDivUInt32 = DivUInt32


def RemSInt32() -> BinaryenOp:
    return lib.BinaryenRemSInt32()


BinaryenRemSInt32 = RemSInt32


def RemUInt32() -> BinaryenOp:
    return lib.BinaryenRemUInt32()


BinaryenRemUInt32 = RemUInt32


def AndInt32() -> BinaryenOp:
    return lib.BinaryenAndInt32()


BinaryenAndInt32 = AndInt32


def OrInt32() -> BinaryenOp:
    return lib.BinaryenOrInt32()


BinaryenOrInt32 = OrInt32


def XorInt32() -> BinaryenOp:
    return lib.BinaryenXorInt32()


BinaryenXorInt32 = XorInt32


def ShlInt32() -> BinaryenOp:
    return lib.BinaryenShlInt32()


BinaryenShlInt32 = ShlInt32


def ShrUInt32() -> BinaryenOp:
    return lib.BinaryenShrUInt32()


BinaryenShrUInt32 = ShrUInt32


def ShrSInt32() -> BinaryenOp:
    return lib.BinaryenShrSInt32()


BinaryenShrSInt32 = ShrSInt32


def RotLInt32() -> BinaryenOp:
    return lib.BinaryenRotLInt32()


BinaryenRotLInt32 = RotLInt32


def RotRInt32() -> BinaryenOp:
    return lib.BinaryenRotRInt32()


BinaryenRotRInt32 = RotRInt32


def EqInt32() -> BinaryenOp:
    return lib.BinaryenEqInt32()


BinaryenEqInt32 = EqInt32


def NeInt32() -> BinaryenOp:
    return lib.BinaryenNeInt32()


BinaryenNeInt32 = NeInt32


def LtSInt32() -> BinaryenOp:
    return lib.BinaryenLtSInt32()


BinaryenLtSInt32 = LtSInt32


def LtUInt32() -> BinaryenOp:
    return lib.BinaryenLtUInt32()


BinaryenLtUInt32 = LtUInt32


def LeSInt32() -> BinaryenOp:
    return lib.BinaryenLeSInt32()


BinaryenLeSInt32 = LeSInt32


def LeUInt32() -> BinaryenOp:
    return lib.BinaryenLeUInt32()


BinaryenLeUInt32 = LeUInt32


def GtSInt32() -> BinaryenOp:
    return lib.BinaryenGtSInt32()


BinaryenGtSInt32 = GtSInt32


def GtUInt32() -> BinaryenOp:
    return lib.BinaryenGtUInt32()


BinaryenGtUInt32 = GtUInt32


def GeSInt32() -> BinaryenOp:
    return lib.BinaryenGeSInt32()


BinaryenGeSInt32 = GeSInt32


def GeUInt32() -> BinaryenOp:
    return lib.BinaryenGeUInt32()


BinaryenGeUInt32 = GeUInt32


def AddInt64() -> BinaryenOp:
    return lib.BinaryenAddInt64()


BinaryenAddInt64 = AddInt64


def SubInt64() -> BinaryenOp:
    return lib.BinaryenSubInt64()


BinaryenSubInt64 = SubInt64


def MulInt64() -> BinaryenOp:
    return lib.BinaryenMulInt64()


BinaryenMulInt64 = MulInt64


def DivSInt64() -> BinaryenOp:
    return lib.BinaryenDivSInt64()


BinaryenDivSInt64 = DivSInt64


def DivUInt64() -> BinaryenOp:
    return lib.BinaryenDivUInt64()


BinaryenDivUInt64 = DivUInt64


def RemSInt64() -> BinaryenOp:
    return lib.BinaryenRemSInt64()


BinaryenRemSInt64 = RemSInt64


def RemUInt64() -> BinaryenOp:
    return lib.BinaryenRemUInt64()


BinaryenRemUInt64 = RemUInt64


def AndInt64() -> BinaryenOp:
    return lib.BinaryenAndInt64()


BinaryenAndInt64 = AndInt64


def OrInt64() -> BinaryenOp:
    return lib.BinaryenOrInt64()


BinaryenOrInt64 = OrInt64


def XorInt64() -> BinaryenOp:
    return lib.BinaryenXorInt64()


BinaryenXorInt64 = XorInt64


def ShlInt64() -> BinaryenOp:
    return lib.BinaryenShlInt64()


BinaryenShlInt64 = ShlInt64


def ShrUInt64() -> BinaryenOp:
    return lib.BinaryenShrUInt64()


BinaryenShrUInt64 = ShrUInt64


def ShrSInt64() -> BinaryenOp:
    return lib.BinaryenShrSInt64()


BinaryenShrSInt64 = ShrSInt64


def RotLInt64() -> BinaryenOp:
    return lib.BinaryenRotLInt64()


BinaryenRotLInt64 = RotLInt64


def RotRInt64() -> BinaryenOp:
    return lib.BinaryenRotRInt64()


BinaryenRotRInt64 = RotRInt64


def EqInt64() -> BinaryenOp:
    return lib.BinaryenEqInt64()


BinaryenEqInt64 = EqInt64


def NeInt64() -> BinaryenOp:
    return lib.BinaryenNeInt64()


BinaryenNeInt64 = NeInt64


def LtSInt64() -> BinaryenOp:
    return lib.BinaryenLtSInt64()


BinaryenLtSInt64 = LtSInt64


def LtUInt64() -> BinaryenOp:
    return lib.BinaryenLtUInt64()


BinaryenLtUInt64 = LtUInt64


def LeSInt64() -> BinaryenOp:
    return lib.BinaryenLeSInt64()


BinaryenLeSInt64 = LeSInt64


def LeUInt64() -> BinaryenOp:
    return lib.BinaryenLeUInt64()


BinaryenLeUInt64 = LeUInt64


def GtSInt64() -> BinaryenOp:
    return lib.BinaryenGtSInt64()


BinaryenGtSInt64 = GtSInt64


def GtUInt64() -> BinaryenOp:
    return lib.BinaryenGtUInt64()


BinaryenGtUInt64 = GtUInt64


def GeSInt64() -> BinaryenOp:
    return lib.BinaryenGeSInt64()


BinaryenGeSInt64 = GeSInt64


def GeUInt64() -> BinaryenOp:
    return lib.BinaryenGeUInt64()


BinaryenGeUInt64 = GeUInt64


def AddFloat32() -> BinaryenOp:
    return lib.BinaryenAddFloat32()


BinaryenAddFloat32 = AddFloat32


def SubFloat32() -> BinaryenOp:
    return lib.BinaryenSubFloat32()


BinaryenSubFloat32 = SubFloat32


def MulFloat32() -> BinaryenOp:
    return lib.BinaryenMulFloat32()


BinaryenMulFloat32 = MulFloat32


def DivFloat32() -> BinaryenOp:
    return lib.BinaryenDivFloat32()


BinaryenDivFloat32 = DivFloat32


def CopySignFloat32() -> BinaryenOp:
    return lib.BinaryenCopySignFloat32()


BinaryenCopySignFloat32 = CopySignFloat32


def MinFloat32() -> BinaryenOp:
    return lib.BinaryenMinFloat32()


BinaryenMinFloat32 = MinFloat32


def MaxFloat32() -> BinaryenOp:
    return lib.BinaryenMaxFloat32()


BinaryenMaxFloat32 = MaxFloat32


def EqFloat32() -> BinaryenOp:
    return lib.BinaryenEqFloat32()


BinaryenEqFloat32 = EqFloat32


def NeFloat32() -> BinaryenOp:
    return lib.BinaryenNeFloat32()


BinaryenNeFloat32 = NeFloat32


def LtFloat32() -> BinaryenOp:
    return lib.BinaryenLtFloat32()


BinaryenLtFloat32 = LtFloat32


def LeFloat32() -> BinaryenOp:
    return lib.BinaryenLeFloat32()


BinaryenLeFloat32 = LeFloat32


def GtFloat32() -> BinaryenOp:
    return lib.BinaryenGtFloat32()


BinaryenGtFloat32 = GtFloat32


def GeFloat32() -> BinaryenOp:
    return lib.BinaryenGeFloat32()


BinaryenGeFloat32 = GeFloat32


def AddFloat64() -> BinaryenOp:
    return lib.BinaryenAddFloat64()


BinaryenAddFloat64 = AddFloat64


def SubFloat64() -> BinaryenOp:
    return lib.BinaryenSubFloat64()


BinaryenSubFloat64 = SubFloat64


def MulFloat64() -> BinaryenOp:
    return lib.BinaryenMulFloat64()


BinaryenMulFloat64 = MulFloat64


def DivFloat64() -> BinaryenOp:
    return lib.BinaryenDivFloat64()


BinaryenDivFloat64 = DivFloat64


def CopySignFloat64() -> BinaryenOp:
    return lib.BinaryenCopySignFloat64()


BinaryenCopySignFloat64 = CopySignFloat64


def MinFloat64() -> BinaryenOp:
    return lib.BinaryenMinFloat64()


BinaryenMinFloat64 = MinFloat64


def MaxFloat64() -> BinaryenOp:
    return lib.BinaryenMaxFloat64()


BinaryenMaxFloat64 = MaxFloat64


def EqFloat64() -> BinaryenOp:
    return lib.BinaryenEqFloat64()


BinaryenEqFloat64 = EqFloat64


def NeFloat64() -> BinaryenOp:
    return lib.BinaryenNeFloat64()


BinaryenNeFloat64 = NeFloat64


def LtFloat64() -> BinaryenOp:
    return lib.BinaryenLtFloat64()


BinaryenLtFloat64 = LtFloat64


def LeFloat64() -> BinaryenOp:
    return lib.BinaryenLeFloat64()


BinaryenLeFloat64 = LeFloat64


def GtFloat64() -> BinaryenOp:
    return lib.BinaryenGtFloat64()


BinaryenGtFloat64 = GtFloat64


def GeFloat64() -> BinaryenOp:
    return lib.BinaryenGeFloat64()


BinaryenGeFloat64 = GeFloat64


def AtomicRMWAdd() -> BinaryenOp:
    return lib.BinaryenAtomicRMWAdd()


BinaryenAtomicRMWAdd = AtomicRMWAdd


def AtomicRMWSub() -> BinaryenOp:
    return lib.BinaryenAtomicRMWSub()


BinaryenAtomicRMWSub = AtomicRMWSub


def AtomicRMWAnd() -> BinaryenOp:
    return lib.BinaryenAtomicRMWAnd()


BinaryenAtomicRMWAnd = AtomicRMWAnd


def AtomicRMWOr() -> BinaryenOp:
    return lib.BinaryenAtomicRMWOr()


BinaryenAtomicRMWOr = AtomicRMWOr


def AtomicRMWXor() -> BinaryenOp:
    return lib.BinaryenAtomicRMWXor()


BinaryenAtomicRMWXor = AtomicRMWXor


def AtomicRMWXchg() -> BinaryenOp:
    return lib.BinaryenAtomicRMWXchg()


BinaryenAtomicRMWXchg = AtomicRMWXchg


def TruncSatSFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat32ToInt32()


BinaryenTruncSatSFloat32ToInt32 = TruncSatSFloat32ToInt32


def TruncSatSFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat32ToInt64()


BinaryenTruncSatSFloat32ToInt64 = TruncSatSFloat32ToInt64


def TruncSatUFloat32ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat32ToInt32()


BinaryenTruncSatUFloat32ToInt32 = TruncSatUFloat32ToInt32


def TruncSatUFloat32ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat32ToInt64()


BinaryenTruncSatUFloat32ToInt64 = TruncSatUFloat32ToInt64


def TruncSatSFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat64ToInt32()


BinaryenTruncSatSFloat64ToInt32 = TruncSatSFloat64ToInt32


def TruncSatSFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatSFloat64ToInt64()


BinaryenTruncSatSFloat64ToInt64 = TruncSatSFloat64ToInt64


def TruncSatUFloat64ToInt32() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat64ToInt32()


BinaryenTruncSatUFloat64ToInt32 = TruncSatUFloat64ToInt32


def TruncSatUFloat64ToInt64() -> BinaryenOp:
    return lib.BinaryenTruncSatUFloat64ToInt64()


BinaryenTruncSatUFloat64ToInt64 = TruncSatUFloat64ToInt64


def SplatVecI8x16() -> BinaryenOp:
    return lib.BinaryenSplatVecI8x16()


BinaryenSplatVecI8x16 = SplatVecI8x16


def ExtractLaneSVecI8x16() -> BinaryenOp:
    return lib.BinaryenExtractLaneSVecI8x16()


BinaryenExtractLaneSVecI8x16 = ExtractLaneSVecI8x16


def ExtractLaneUVecI8x16() -> BinaryenOp:
    return lib.BinaryenExtractLaneUVecI8x16()


BinaryenExtractLaneUVecI8x16 = ExtractLaneUVecI8x16


def ReplaceLaneVecI8x16() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI8x16()


BinaryenReplaceLaneVecI8x16 = ReplaceLaneVecI8x16


def SplatVecI16x8() -> BinaryenOp:
    return lib.BinaryenSplatVecI16x8()


BinaryenSplatVecI16x8 = SplatVecI16x8


def ExtractLaneSVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtractLaneSVecI16x8()


BinaryenExtractLaneSVecI16x8 = ExtractLaneSVecI16x8


def ExtractLaneUVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtractLaneUVecI16x8()


BinaryenExtractLaneUVecI16x8 = ExtractLaneUVecI16x8


def ReplaceLaneVecI16x8() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI16x8()


BinaryenReplaceLaneVecI16x8 = ReplaceLaneVecI16x8


def SplatVecI32x4() -> BinaryenOp:
    return lib.BinaryenSplatVecI32x4()


BinaryenSplatVecI32x4 = SplatVecI32x4


def ExtractLaneVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecI32x4()


BinaryenExtractLaneVecI32x4 = ExtractLaneVecI32x4


def ReplaceLaneVecI32x4() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI32x4()


BinaryenReplaceLaneVecI32x4 = ReplaceLaneVecI32x4


def SplatVecI64x2() -> BinaryenOp:
    return lib.BinaryenSplatVecI64x2()


BinaryenSplatVecI64x2 = SplatVecI64x2


def ExtractLaneVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecI64x2()


BinaryenExtractLaneVecI64x2 = ExtractLaneVecI64x2


def ReplaceLaneVecI64x2() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecI64x2()


BinaryenReplaceLaneVecI64x2 = ReplaceLaneVecI64x2


def SplatVecF32x4() -> BinaryenOp:
    return lib.BinaryenSplatVecF32x4()


BinaryenSplatVecF32x4 = SplatVecF32x4


def ExtractLaneVecF32x4() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecF32x4()


BinaryenExtractLaneVecF32x4 = ExtractLaneVecF32x4


def ReplaceLaneVecF32x4() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecF32x4()


BinaryenReplaceLaneVecF32x4 = ReplaceLaneVecF32x4


def SplatVecF64x2() -> BinaryenOp:
    return lib.BinaryenSplatVecF64x2()


BinaryenSplatVecF64x2 = SplatVecF64x2


def ExtractLaneVecF64x2() -> BinaryenOp:
    return lib.BinaryenExtractLaneVecF64x2()


BinaryenExtractLaneVecF64x2 = ExtractLaneVecF64x2


def ReplaceLaneVecF64x2() -> BinaryenOp:
    return lib.BinaryenReplaceLaneVecF64x2()


BinaryenReplaceLaneVecF64x2 = ReplaceLaneVecF64x2


def EqVecI8x16() -> BinaryenOp:
    return lib.BinaryenEqVecI8x16()


BinaryenEqVecI8x16 = EqVecI8x16


def NeVecI8x16() -> BinaryenOp:
    return lib.BinaryenNeVecI8x16()


BinaryenNeVecI8x16 = NeVecI8x16


def LtSVecI8x16() -> BinaryenOp:
    return lib.BinaryenLtSVecI8x16()


BinaryenLtSVecI8x16 = LtSVecI8x16


def LtUVecI8x16() -> BinaryenOp:
    return lib.BinaryenLtUVecI8x16()


BinaryenLtUVecI8x16 = LtUVecI8x16


def GtSVecI8x16() -> BinaryenOp:
    return lib.BinaryenGtSVecI8x16()


BinaryenGtSVecI8x16 = GtSVecI8x16


def GtUVecI8x16() -> BinaryenOp:
    return lib.BinaryenGtUVecI8x16()


BinaryenGtUVecI8x16 = GtUVecI8x16


def LeSVecI8x16() -> BinaryenOp:
    return lib.BinaryenLeSVecI8x16()


BinaryenLeSVecI8x16 = LeSVecI8x16


def LeUVecI8x16() -> BinaryenOp:
    return lib.BinaryenLeUVecI8x16()


BinaryenLeUVecI8x16 = LeUVecI8x16


def GeSVecI8x16() -> BinaryenOp:
    return lib.BinaryenGeSVecI8x16()


BinaryenGeSVecI8x16 = GeSVecI8x16


def GeUVecI8x16() -> BinaryenOp:
    return lib.BinaryenGeUVecI8x16()


BinaryenGeUVecI8x16 = GeUVecI8x16


def EqVecI16x8() -> BinaryenOp:
    return lib.BinaryenEqVecI16x8()


BinaryenEqVecI16x8 = EqVecI16x8


def NeVecI16x8() -> BinaryenOp:
    return lib.BinaryenNeVecI16x8()


BinaryenNeVecI16x8 = NeVecI16x8


def LtSVecI16x8() -> BinaryenOp:
    return lib.BinaryenLtSVecI16x8()


BinaryenLtSVecI16x8 = LtSVecI16x8


def LtUVecI16x8() -> BinaryenOp:
    return lib.BinaryenLtUVecI16x8()


BinaryenLtUVecI16x8 = LtUVecI16x8


def GtSVecI16x8() -> BinaryenOp:
    return lib.BinaryenGtSVecI16x8()


BinaryenGtSVecI16x8 = GtSVecI16x8


def GtUVecI16x8() -> BinaryenOp:
    return lib.BinaryenGtUVecI16x8()


BinaryenGtUVecI16x8 = GtUVecI16x8


def LeSVecI16x8() -> BinaryenOp:
    return lib.BinaryenLeSVecI16x8()


BinaryenLeSVecI16x8 = LeSVecI16x8


def LeUVecI16x8() -> BinaryenOp:
    return lib.BinaryenLeUVecI16x8()


BinaryenLeUVecI16x8 = LeUVecI16x8


def GeSVecI16x8() -> BinaryenOp:
    return lib.BinaryenGeSVecI16x8()


BinaryenGeSVecI16x8 = GeSVecI16x8


def GeUVecI16x8() -> BinaryenOp:
    return lib.BinaryenGeUVecI16x8()


BinaryenGeUVecI16x8 = GeUVecI16x8


def EqVecI32x4() -> BinaryenOp:
    return lib.BinaryenEqVecI32x4()


BinaryenEqVecI32x4 = EqVecI32x4


def NeVecI32x4() -> BinaryenOp:
    return lib.BinaryenNeVecI32x4()


BinaryenNeVecI32x4 = NeVecI32x4


def LtSVecI32x4() -> BinaryenOp:
    return lib.BinaryenLtSVecI32x4()


BinaryenLtSVecI32x4 = LtSVecI32x4


def LtUVecI32x4() -> BinaryenOp:
    return lib.BinaryenLtUVecI32x4()


BinaryenLtUVecI32x4 = LtUVecI32x4


def GtSVecI32x4() -> BinaryenOp:
    return lib.BinaryenGtSVecI32x4()


BinaryenGtSVecI32x4 = GtSVecI32x4


def GtUVecI32x4() -> BinaryenOp:
    return lib.BinaryenGtUVecI32x4()


BinaryenGtUVecI32x4 = GtUVecI32x4


def LeSVecI32x4() -> BinaryenOp:
    return lib.BinaryenLeSVecI32x4()


BinaryenLeSVecI32x4 = LeSVecI32x4


def LeUVecI32x4() -> BinaryenOp:
    return lib.BinaryenLeUVecI32x4()


BinaryenLeUVecI32x4 = LeUVecI32x4


def GeSVecI32x4() -> BinaryenOp:
    return lib.BinaryenGeSVecI32x4()


BinaryenGeSVecI32x4 = GeSVecI32x4


def GeUVecI32x4() -> BinaryenOp:
    return lib.BinaryenGeUVecI32x4()


BinaryenGeUVecI32x4 = GeUVecI32x4


def EqVecI64x2() -> BinaryenOp:
    return lib.BinaryenEqVecI64x2()


BinaryenEqVecI64x2 = EqVecI64x2


def NeVecI64x2() -> BinaryenOp:
    return lib.BinaryenNeVecI64x2()


BinaryenNeVecI64x2 = NeVecI64x2


def LtSVecI64x2() -> BinaryenOp:
    return lib.BinaryenLtSVecI64x2()


BinaryenLtSVecI64x2 = LtSVecI64x2


def GtSVecI64x2() -> BinaryenOp:
    return lib.BinaryenGtSVecI64x2()


BinaryenGtSVecI64x2 = GtSVecI64x2


def LeSVecI64x2() -> BinaryenOp:
    return lib.BinaryenLeSVecI64x2()


BinaryenLeSVecI64x2 = LeSVecI64x2


def GeSVecI64x2() -> BinaryenOp:
    return lib.BinaryenGeSVecI64x2()


BinaryenGeSVecI64x2 = GeSVecI64x2


def EqVecF32x4() -> BinaryenOp:
    return lib.BinaryenEqVecF32x4()


BinaryenEqVecF32x4 = EqVecF32x4


def NeVecF32x4() -> BinaryenOp:
    return lib.BinaryenNeVecF32x4()


BinaryenNeVecF32x4 = NeVecF32x4


def LtVecF32x4() -> BinaryenOp:
    return lib.BinaryenLtVecF32x4()


BinaryenLtVecF32x4 = LtVecF32x4


def GtVecF32x4() -> BinaryenOp:
    return lib.BinaryenGtVecF32x4()


BinaryenGtVecF32x4 = GtVecF32x4


def LeVecF32x4() -> BinaryenOp:
    return lib.BinaryenLeVecF32x4()


BinaryenLeVecF32x4 = LeVecF32x4


def GeVecF32x4() -> BinaryenOp:
    return lib.BinaryenGeVecF32x4()


BinaryenGeVecF32x4 = GeVecF32x4


def EqVecF64x2() -> BinaryenOp:
    return lib.BinaryenEqVecF64x2()


BinaryenEqVecF64x2 = EqVecF64x2


def NeVecF64x2() -> BinaryenOp:
    return lib.BinaryenNeVecF64x2()


BinaryenNeVecF64x2 = NeVecF64x2


def LtVecF64x2() -> BinaryenOp:
    return lib.BinaryenLtVecF64x2()


BinaryenLtVecF64x2 = LtVecF64x2


def GtVecF64x2() -> BinaryenOp:
    return lib.BinaryenGtVecF64x2()


BinaryenGtVecF64x2 = GtVecF64x2


def LeVecF64x2() -> BinaryenOp:
    return lib.BinaryenLeVecF64x2()


BinaryenLeVecF64x2 = LeVecF64x2


def GeVecF64x2() -> BinaryenOp:
    return lib.BinaryenGeVecF64x2()


BinaryenGeVecF64x2 = GeVecF64x2


def NotVec128() -> BinaryenOp:
    return lib.BinaryenNotVec128()


BinaryenNotVec128 = NotVec128


def AndVec128() -> BinaryenOp:
    return lib.BinaryenAndVec128()


BinaryenAndVec128 = AndVec128


def OrVec128() -> BinaryenOp:
    return lib.BinaryenOrVec128()


BinaryenOrVec128 = OrVec128


def XorVec128() -> BinaryenOp:
    return lib.BinaryenXorVec128()


BinaryenXorVec128 = XorVec128


def AndNotVec128() -> BinaryenOp:
    return lib.BinaryenAndNotVec128()


BinaryenAndNotVec128 = AndNotVec128


def BitselectVec128() -> BinaryenOp:
    return lib.BinaryenBitselectVec128()


BinaryenBitselectVec128 = BitselectVec128


def AnyTrueVec128() -> BinaryenOp:
    return lib.BinaryenAnyTrueVec128()


BinaryenAnyTrueVec128 = AnyTrueVec128


def PopcntVecI8x16() -> BinaryenOp:
    return lib.BinaryenPopcntVecI8x16()


BinaryenPopcntVecI8x16 = PopcntVecI8x16


def AbsVecI8x16() -> BinaryenOp:
    return lib.BinaryenAbsVecI8x16()


BinaryenAbsVecI8x16 = AbsVecI8x16


def NegVecI8x16() -> BinaryenOp:
    return lib.BinaryenNegVecI8x16()


BinaryenNegVecI8x16 = NegVecI8x16


def AllTrueVecI8x16() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI8x16()


BinaryenAllTrueVecI8x16 = AllTrueVecI8x16


def BitmaskVecI8x16() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI8x16()


BinaryenBitmaskVecI8x16 = BitmaskVecI8x16


def ShlVecI8x16() -> BinaryenOp:
    return lib.BinaryenShlVecI8x16()


BinaryenShlVecI8x16 = ShlVecI8x16


def ShrSVecI8x16() -> BinaryenOp:
    return lib.BinaryenShrSVecI8x16()


BinaryenShrSVecI8x16 = ShrSVecI8x16


def ShrUVecI8x16() -> BinaryenOp:
    return lib.BinaryenShrUVecI8x16()


BinaryenShrUVecI8x16 = ShrUVecI8x16


def AddVecI8x16() -> BinaryenOp:
    return lib.BinaryenAddVecI8x16()


BinaryenAddVecI8x16 = AddVecI8x16


def AddSatSVecI8x16() -> BinaryenOp:
    return lib.BinaryenAddSatSVecI8x16()


BinaryenAddSatSVecI8x16 = AddSatSVecI8x16


def AddSatUVecI8x16() -> BinaryenOp:
    return lib.BinaryenAddSatUVecI8x16()


BinaryenAddSatUVecI8x16 = AddSatUVecI8x16


def SubVecI8x16() -> BinaryenOp:
    return lib.BinaryenSubVecI8x16()


BinaryenSubVecI8x16 = SubVecI8x16


def SubSatSVecI8x16() -> BinaryenOp:
    return lib.BinaryenSubSatSVecI8x16()


BinaryenSubSatSVecI8x16 = SubSatSVecI8x16


def SubSatUVecI8x16() -> BinaryenOp:
    return lib.BinaryenSubSatUVecI8x16()


BinaryenSubSatUVecI8x16 = SubSatUVecI8x16


def MinSVecI8x16() -> BinaryenOp:
    return lib.BinaryenMinSVecI8x16()


BinaryenMinSVecI8x16 = MinSVecI8x16


def MinUVecI8x16() -> BinaryenOp:
    return lib.BinaryenMinUVecI8x16()


BinaryenMinUVecI8x16 = MinUVecI8x16


def MaxSVecI8x16() -> BinaryenOp:
    return lib.BinaryenMaxSVecI8x16()


BinaryenMaxSVecI8x16 = MaxSVecI8x16


def MaxUVecI8x16() -> BinaryenOp:
    return lib.BinaryenMaxUVecI8x16()


BinaryenMaxUVecI8x16 = MaxUVecI8x16


def AvgrUVecI8x16() -> BinaryenOp:
    return lib.BinaryenAvgrUVecI8x16()


BinaryenAvgrUVecI8x16 = AvgrUVecI8x16


def AbsVecI16x8() -> BinaryenOp:
    return lib.BinaryenAbsVecI16x8()


BinaryenAbsVecI16x8 = AbsVecI16x8


def NegVecI16x8() -> BinaryenOp:
    return lib.BinaryenNegVecI16x8()


BinaryenNegVecI16x8 = NegVecI16x8


def AllTrueVecI16x8() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI16x8()


BinaryenAllTrueVecI16x8 = AllTrueVecI16x8


def BitmaskVecI16x8() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI16x8()


BinaryenBitmaskVecI16x8 = BitmaskVecI16x8


def ShlVecI16x8() -> BinaryenOp:
    return lib.BinaryenShlVecI16x8()


BinaryenShlVecI16x8 = ShlVecI16x8


def ShrSVecI16x8() -> BinaryenOp:
    return lib.BinaryenShrSVecI16x8()


BinaryenShrSVecI16x8 = ShrSVecI16x8


def ShrUVecI16x8() -> BinaryenOp:
    return lib.BinaryenShrUVecI16x8()


BinaryenShrUVecI16x8 = ShrUVecI16x8


def AddVecI16x8() -> BinaryenOp:
    return lib.BinaryenAddVecI16x8()


BinaryenAddVecI16x8 = AddVecI16x8


def AddSatSVecI16x8() -> BinaryenOp:
    return lib.BinaryenAddSatSVecI16x8()


BinaryenAddSatSVecI16x8 = AddSatSVecI16x8


def AddSatUVecI16x8() -> BinaryenOp:
    return lib.BinaryenAddSatUVecI16x8()


BinaryenAddSatUVecI16x8 = AddSatUVecI16x8


def SubVecI16x8() -> BinaryenOp:
    return lib.BinaryenSubVecI16x8()


BinaryenSubVecI16x8 = SubVecI16x8


def SubSatSVecI16x8() -> BinaryenOp:
    return lib.BinaryenSubSatSVecI16x8()


BinaryenSubSatSVecI16x8 = SubSatSVecI16x8


def SubSatUVecI16x8() -> BinaryenOp:
    return lib.BinaryenSubSatUVecI16x8()


BinaryenSubSatUVecI16x8 = SubSatUVecI16x8


def MulVecI16x8() -> BinaryenOp:
    return lib.BinaryenMulVecI16x8()


BinaryenMulVecI16x8 = MulVecI16x8


def MinSVecI16x8() -> BinaryenOp:
    return lib.BinaryenMinSVecI16x8()


BinaryenMinSVecI16x8 = MinSVecI16x8


def MinUVecI16x8() -> BinaryenOp:
    return lib.BinaryenMinUVecI16x8()


BinaryenMinUVecI16x8 = MinUVecI16x8


def MaxSVecI16x8() -> BinaryenOp:
    return lib.BinaryenMaxSVecI16x8()


BinaryenMaxSVecI16x8 = MaxSVecI16x8


def MaxUVecI16x8() -> BinaryenOp:
    return lib.BinaryenMaxUVecI16x8()


BinaryenMaxUVecI16x8 = MaxUVecI16x8


def AvgrUVecI16x8() -> BinaryenOp:
    return lib.BinaryenAvgrUVecI16x8()


BinaryenAvgrUVecI16x8 = AvgrUVecI16x8


def Q15MulrSatSVecI16x8() -> BinaryenOp:
    return lib.BinaryenQ15MulrSatSVecI16x8()


BinaryenQ15MulrSatSVecI16x8 = Q15MulrSatSVecI16x8


def ExtMulLowSVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulLowSVecI16x8()


BinaryenExtMulLowSVecI16x8 = ExtMulLowSVecI16x8


def ExtMulHighSVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulHighSVecI16x8()


BinaryenExtMulHighSVecI16x8 = ExtMulHighSVecI16x8


def ExtMulLowUVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulLowUVecI16x8()


BinaryenExtMulLowUVecI16x8 = ExtMulLowUVecI16x8


def ExtMulHighUVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtMulHighUVecI16x8()


BinaryenExtMulHighUVecI16x8 = ExtMulHighUVecI16x8


def AbsVecI32x4() -> BinaryenOp:
    return lib.BinaryenAbsVecI32x4()


BinaryenAbsVecI32x4 = AbsVecI32x4


def NegVecI32x4() -> BinaryenOp:
    return lib.BinaryenNegVecI32x4()


BinaryenNegVecI32x4 = NegVecI32x4


def AllTrueVecI32x4() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI32x4()


BinaryenAllTrueVecI32x4 = AllTrueVecI32x4


def BitmaskVecI32x4() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI32x4()


BinaryenBitmaskVecI32x4 = BitmaskVecI32x4


def ShlVecI32x4() -> BinaryenOp:
    return lib.BinaryenShlVecI32x4()


BinaryenShlVecI32x4 = ShlVecI32x4


def ShrSVecI32x4() -> BinaryenOp:
    return lib.BinaryenShrSVecI32x4()


BinaryenShrSVecI32x4 = ShrSVecI32x4


def ShrUVecI32x4() -> BinaryenOp:
    return lib.BinaryenShrUVecI32x4()


BinaryenShrUVecI32x4 = ShrUVecI32x4


def AddVecI32x4() -> BinaryenOp:
    return lib.BinaryenAddVecI32x4()


BinaryenAddVecI32x4 = AddVecI32x4


def SubVecI32x4() -> BinaryenOp:
    return lib.BinaryenSubVecI32x4()


BinaryenSubVecI32x4 = SubVecI32x4


def MulVecI32x4() -> BinaryenOp:
    return lib.BinaryenMulVecI32x4()


BinaryenMulVecI32x4 = MulVecI32x4


def MinSVecI32x4() -> BinaryenOp:
    return lib.BinaryenMinSVecI32x4()


BinaryenMinSVecI32x4 = MinSVecI32x4


def MinUVecI32x4() -> BinaryenOp:
    return lib.BinaryenMinUVecI32x4()


BinaryenMinUVecI32x4 = MinUVecI32x4


def MaxSVecI32x4() -> BinaryenOp:
    return lib.BinaryenMaxSVecI32x4()


BinaryenMaxSVecI32x4 = MaxSVecI32x4


def MaxUVecI32x4() -> BinaryenOp:
    return lib.BinaryenMaxUVecI32x4()


BinaryenMaxUVecI32x4 = MaxUVecI32x4


def DotSVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenDotSVecI16x8ToVecI32x4()


BinaryenDotSVecI16x8ToVecI32x4 = DotSVecI16x8ToVecI32x4


def ExtMulLowSVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulLowSVecI32x4()


BinaryenExtMulLowSVecI32x4 = ExtMulLowSVecI32x4


def ExtMulHighSVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulHighSVecI32x4()


BinaryenExtMulHighSVecI32x4 = ExtMulHighSVecI32x4


def ExtMulLowUVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulLowUVecI32x4()


BinaryenExtMulLowUVecI32x4 = ExtMulLowUVecI32x4


def ExtMulHighUVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtMulHighUVecI32x4()


BinaryenExtMulHighUVecI32x4 = ExtMulHighUVecI32x4


def AbsVecI64x2() -> BinaryenOp:
    return lib.BinaryenAbsVecI64x2()


BinaryenAbsVecI64x2 = AbsVecI64x2


def NegVecI64x2() -> BinaryenOp:
    return lib.BinaryenNegVecI64x2()


BinaryenNegVecI64x2 = NegVecI64x2


def AllTrueVecI64x2() -> BinaryenOp:
    return lib.BinaryenAllTrueVecI64x2()


BinaryenAllTrueVecI64x2 = AllTrueVecI64x2


def BitmaskVecI64x2() -> BinaryenOp:
    return lib.BinaryenBitmaskVecI64x2()


BinaryenBitmaskVecI64x2 = BitmaskVecI64x2


def ShlVecI64x2() -> BinaryenOp:
    return lib.BinaryenShlVecI64x2()


BinaryenShlVecI64x2 = ShlVecI64x2


def ShrSVecI64x2() -> BinaryenOp:
    return lib.BinaryenShrSVecI64x2()


BinaryenShrSVecI64x2 = ShrSVecI64x2


def ShrUVecI64x2() -> BinaryenOp:
    return lib.BinaryenShrUVecI64x2()


BinaryenShrUVecI64x2 = ShrUVecI64x2


def AddVecI64x2() -> BinaryenOp:
    return lib.BinaryenAddVecI64x2()


BinaryenAddVecI64x2 = AddVecI64x2


def SubVecI64x2() -> BinaryenOp:
    return lib.BinaryenSubVecI64x2()


BinaryenSubVecI64x2 = SubVecI64x2


def MulVecI64x2() -> BinaryenOp:
    return lib.BinaryenMulVecI64x2()


BinaryenMulVecI64x2 = MulVecI64x2


def ExtMulLowSVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulLowSVecI64x2()


BinaryenExtMulLowSVecI64x2 = ExtMulLowSVecI64x2


def ExtMulHighSVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulHighSVecI64x2()


BinaryenExtMulHighSVecI64x2 = ExtMulHighSVecI64x2


def ExtMulLowUVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulLowUVecI64x2()


BinaryenExtMulLowUVecI64x2 = ExtMulLowUVecI64x2


def ExtMulHighUVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtMulHighUVecI64x2()


BinaryenExtMulHighUVecI64x2 = ExtMulHighUVecI64x2


def AbsVecF32x4() -> BinaryenOp:
    return lib.BinaryenAbsVecF32x4()


BinaryenAbsVecF32x4 = AbsVecF32x4


def NegVecF32x4() -> BinaryenOp:
    return lib.BinaryenNegVecF32x4()


BinaryenNegVecF32x4 = NegVecF32x4


def SqrtVecF32x4() -> BinaryenOp:
    return lib.BinaryenSqrtVecF32x4()


BinaryenSqrtVecF32x4 = SqrtVecF32x4


def AddVecF32x4() -> BinaryenOp:
    return lib.BinaryenAddVecF32x4()


BinaryenAddVecF32x4 = AddVecF32x4


def SubVecF32x4() -> BinaryenOp:
    return lib.BinaryenSubVecF32x4()


BinaryenSubVecF32x4 = SubVecF32x4


def MulVecF32x4() -> BinaryenOp:
    return lib.BinaryenMulVecF32x4()


BinaryenMulVecF32x4 = MulVecF32x4


def DivVecF32x4() -> BinaryenOp:
    return lib.BinaryenDivVecF32x4()


BinaryenDivVecF32x4 = DivVecF32x4


def MinVecF32x4() -> BinaryenOp:
    return lib.BinaryenMinVecF32x4()


BinaryenMinVecF32x4 = MinVecF32x4


def MaxVecF32x4() -> BinaryenOp:
    return lib.BinaryenMaxVecF32x4()


BinaryenMaxVecF32x4 = MaxVecF32x4


def PMinVecF32x4() -> BinaryenOp:
    return lib.BinaryenPMinVecF32x4()


BinaryenPMinVecF32x4 = PMinVecF32x4


def PMaxVecF32x4() -> BinaryenOp:
    return lib.BinaryenPMaxVecF32x4()


BinaryenPMaxVecF32x4 = PMaxVecF32x4


def CeilVecF32x4() -> BinaryenOp:
    return lib.BinaryenCeilVecF32x4()


BinaryenCeilVecF32x4 = CeilVecF32x4


def FloorVecF32x4() -> BinaryenOp:
    return lib.BinaryenFloorVecF32x4()


BinaryenFloorVecF32x4 = FloorVecF32x4


def TruncVecF32x4() -> BinaryenOp:
    return lib.BinaryenTruncVecF32x4()


BinaryenTruncVecF32x4 = TruncVecF32x4


def NearestVecF32x4() -> BinaryenOp:
    return lib.BinaryenNearestVecF32x4()


BinaryenNearestVecF32x4 = NearestVecF32x4


def AbsVecF64x2() -> BinaryenOp:
    return lib.BinaryenAbsVecF64x2()


BinaryenAbsVecF64x2 = AbsVecF64x2


def NegVecF64x2() -> BinaryenOp:
    return lib.BinaryenNegVecF64x2()


BinaryenNegVecF64x2 = NegVecF64x2


def SqrtVecF64x2() -> BinaryenOp:
    return lib.BinaryenSqrtVecF64x2()


BinaryenSqrtVecF64x2 = SqrtVecF64x2


def AddVecF64x2() -> BinaryenOp:
    return lib.BinaryenAddVecF64x2()


BinaryenAddVecF64x2 = AddVecF64x2


def SubVecF64x2() -> BinaryenOp:
    return lib.BinaryenSubVecF64x2()


BinaryenSubVecF64x2 = SubVecF64x2


def MulVecF64x2() -> BinaryenOp:
    return lib.BinaryenMulVecF64x2()


BinaryenMulVecF64x2 = MulVecF64x2


def DivVecF64x2() -> BinaryenOp:
    return lib.BinaryenDivVecF64x2()


BinaryenDivVecF64x2 = DivVecF64x2


def MinVecF64x2() -> BinaryenOp:
    return lib.BinaryenMinVecF64x2()


BinaryenMinVecF64x2 = MinVecF64x2


def MaxVecF64x2() -> BinaryenOp:
    return lib.BinaryenMaxVecF64x2()


BinaryenMaxVecF64x2 = MaxVecF64x2


def PMinVecF64x2() -> BinaryenOp:
    return lib.BinaryenPMinVecF64x2()


BinaryenPMinVecF64x2 = PMinVecF64x2


def PMaxVecF64x2() -> BinaryenOp:
    return lib.BinaryenPMaxVecF64x2()


BinaryenPMaxVecF64x2 = PMaxVecF64x2


def CeilVecF64x2() -> BinaryenOp:
    return lib.BinaryenCeilVecF64x2()


BinaryenCeilVecF64x2 = CeilVecF64x2


def FloorVecF64x2() -> BinaryenOp:
    return lib.BinaryenFloorVecF64x2()


BinaryenFloorVecF64x2 = FloorVecF64x2


def TruncVecF64x2() -> BinaryenOp:
    return lib.BinaryenTruncVecF64x2()


BinaryenTruncVecF64x2 = TruncVecF64x2


def NearestVecF64x2() -> BinaryenOp:
    return lib.BinaryenNearestVecF64x2()


BinaryenNearestVecF64x2 = NearestVecF64x2


def ExtAddPairwiseSVecI8x16ToI16x8() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseSVecI8x16ToI16x8()


BinaryenExtAddPairwiseSVecI8x16ToI16x8 = ExtAddPairwiseSVecI8x16ToI16x8


def ExtAddPairwiseUVecI8x16ToI16x8() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseUVecI8x16ToI16x8()


BinaryenExtAddPairwiseUVecI8x16ToI16x8 = ExtAddPairwiseUVecI8x16ToI16x8


def ExtAddPairwiseSVecI16x8ToI32x4() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseSVecI16x8ToI32x4()


BinaryenExtAddPairwiseSVecI16x8ToI32x4 = ExtAddPairwiseSVecI16x8ToI32x4


def ExtAddPairwiseUVecI16x8ToI32x4() -> BinaryenOp:
    return lib.BinaryenExtAddPairwiseUVecI16x8ToI32x4()


BinaryenExtAddPairwiseUVecI16x8ToI32x4 = ExtAddPairwiseUVecI16x8ToI32x4


def TruncSatSVecF32x4ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatSVecF32x4ToVecI32x4()


BinaryenTruncSatSVecF32x4ToVecI32x4 = TruncSatSVecF32x4ToVecI32x4


def TruncSatUVecF32x4ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatUVecF32x4ToVecI32x4()


BinaryenTruncSatUVecF32x4ToVecI32x4 = TruncSatUVecF32x4ToVecI32x4


def ConvertSVecI32x4ToVecF32x4() -> BinaryenOp:
    return lib.BinaryenConvertSVecI32x4ToVecF32x4()


BinaryenConvertSVecI32x4ToVecF32x4 = ConvertSVecI32x4ToVecF32x4


def ConvertUVecI32x4ToVecF32x4() -> BinaryenOp:
    return lib.BinaryenConvertUVecI32x4ToVecF32x4()


BinaryenConvertUVecI32x4ToVecF32x4 = ConvertUVecI32x4ToVecF32x4


def Load8SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad8SplatVec128()


BinaryenLoad8SplatVec128 = Load8SplatVec128


def Load16SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad16SplatVec128()


BinaryenLoad16SplatVec128 = Load16SplatVec128


def Load32SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad32SplatVec128()


BinaryenLoad32SplatVec128 = Load32SplatVec128


def Load64SplatVec128() -> BinaryenOp:
    return lib.BinaryenLoad64SplatVec128()


BinaryenLoad64SplatVec128 = Load64SplatVec128


def Load8x8SVec128() -> BinaryenOp:
    return lib.BinaryenLoad8x8SVec128()


BinaryenLoad8x8SVec128 = Load8x8SVec128


def Load8x8UVec128() -> BinaryenOp:
    return lib.BinaryenLoad8x8UVec128()


BinaryenLoad8x8UVec128 = Load8x8UVec128


def Load16x4SVec128() -> BinaryenOp:
    return lib.BinaryenLoad16x4SVec128()


BinaryenLoad16x4SVec128 = Load16x4SVec128


def Load16x4UVec128() -> BinaryenOp:
    return lib.BinaryenLoad16x4UVec128()


BinaryenLoad16x4UVec128 = Load16x4UVec128


def Load32x2SVec128() -> BinaryenOp:
    return lib.BinaryenLoad32x2SVec128()


BinaryenLoad32x2SVec128 = Load32x2SVec128


def Load32x2UVec128() -> BinaryenOp:
    return lib.BinaryenLoad32x2UVec128()


BinaryenLoad32x2UVec128 = Load32x2UVec128


def Load32ZeroVec128() -> BinaryenOp:
    return lib.BinaryenLoad32ZeroVec128()


BinaryenLoad32ZeroVec128 = Load32ZeroVec128


def Load64ZeroVec128() -> BinaryenOp:
    return lib.BinaryenLoad64ZeroVec128()


BinaryenLoad64ZeroVec128 = Load64ZeroVec128


def Load8LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad8LaneVec128()


BinaryenLoad8LaneVec128 = Load8LaneVec128


def Load16LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad16LaneVec128()


BinaryenLoad16LaneVec128 = Load16LaneVec128


def Load32LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad32LaneVec128()


BinaryenLoad32LaneVec128 = Load32LaneVec128


def Load64LaneVec128() -> BinaryenOp:
    return lib.BinaryenLoad64LaneVec128()


BinaryenLoad64LaneVec128 = Load64LaneVec128


def Store8LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore8LaneVec128()


BinaryenStore8LaneVec128 = Store8LaneVec128


def Store16LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore16LaneVec128()


BinaryenStore16LaneVec128 = Store16LaneVec128


def Store32LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore32LaneVec128()


BinaryenStore32LaneVec128 = Store32LaneVec128


def Store64LaneVec128() -> BinaryenOp:
    return lib.BinaryenStore64LaneVec128()


BinaryenStore64LaneVec128 = Store64LaneVec128


def NarrowSVecI16x8ToVecI8x16() -> BinaryenOp:
    return lib.BinaryenNarrowSVecI16x8ToVecI8x16()


BinaryenNarrowSVecI16x8ToVecI8x16 = NarrowSVecI16x8ToVecI8x16


def NarrowUVecI16x8ToVecI8x16() -> BinaryenOp:
    return lib.BinaryenNarrowUVecI16x8ToVecI8x16()


BinaryenNarrowUVecI16x8ToVecI8x16 = NarrowUVecI16x8ToVecI8x16


def NarrowSVecI32x4ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenNarrowSVecI32x4ToVecI16x8()


BinaryenNarrowSVecI32x4ToVecI16x8 = NarrowSVecI32x4ToVecI16x8


def NarrowUVecI32x4ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenNarrowUVecI32x4ToVecI16x8()


BinaryenNarrowUVecI32x4ToVecI16x8 = NarrowUVecI32x4ToVecI16x8


def ExtendLowSVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendLowSVecI8x16ToVecI16x8()


BinaryenExtendLowSVecI8x16ToVecI16x8 = ExtendLowSVecI8x16ToVecI16x8


def ExtendHighSVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendHighSVecI8x16ToVecI16x8()


BinaryenExtendHighSVecI8x16ToVecI16x8 = ExtendHighSVecI8x16ToVecI16x8


def ExtendLowUVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendLowUVecI8x16ToVecI16x8()


BinaryenExtendLowUVecI8x16ToVecI16x8 = ExtendLowUVecI8x16ToVecI16x8


def ExtendHighUVecI8x16ToVecI16x8() -> BinaryenOp:
    return lib.BinaryenExtendHighUVecI8x16ToVecI16x8()


BinaryenExtendHighUVecI8x16ToVecI16x8 = ExtendHighUVecI8x16ToVecI16x8


def ExtendLowSVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendLowSVecI16x8ToVecI32x4()


BinaryenExtendLowSVecI16x8ToVecI32x4 = ExtendLowSVecI16x8ToVecI32x4


def ExtendHighSVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendHighSVecI16x8ToVecI32x4()


BinaryenExtendHighSVecI16x8ToVecI32x4 = ExtendHighSVecI16x8ToVecI32x4


def ExtendLowUVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendLowUVecI16x8ToVecI32x4()


BinaryenExtendLowUVecI16x8ToVecI32x4 = ExtendLowUVecI16x8ToVecI32x4


def ExtendHighUVecI16x8ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenExtendHighUVecI16x8ToVecI32x4()


BinaryenExtendHighUVecI16x8ToVecI32x4 = ExtendHighUVecI16x8ToVecI32x4


def ExtendLowSVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendLowSVecI32x4ToVecI64x2()


BinaryenExtendLowSVecI32x4ToVecI64x2 = ExtendLowSVecI32x4ToVecI64x2


def ExtendHighSVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendHighSVecI32x4ToVecI64x2()


BinaryenExtendHighSVecI32x4ToVecI64x2 = ExtendHighSVecI32x4ToVecI64x2


def ExtendLowUVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendLowUVecI32x4ToVecI64x2()


BinaryenExtendLowUVecI32x4ToVecI64x2 = ExtendLowUVecI32x4ToVecI64x2


def ExtendHighUVecI32x4ToVecI64x2() -> BinaryenOp:
    return lib.BinaryenExtendHighUVecI32x4ToVecI64x2()


BinaryenExtendHighUVecI32x4ToVecI64x2 = ExtendHighUVecI32x4ToVecI64x2


def ConvertLowSVecI32x4ToVecF64x2() -> BinaryenOp:
    return lib.BinaryenConvertLowSVecI32x4ToVecF64x2()


BinaryenConvertLowSVecI32x4ToVecF64x2 = ConvertLowSVecI32x4ToVecF64x2


def ConvertLowUVecI32x4ToVecF64x2() -> BinaryenOp:
    return lib.BinaryenConvertLowUVecI32x4ToVecF64x2()


BinaryenConvertLowUVecI32x4ToVecF64x2 = ConvertLowUVecI32x4ToVecF64x2


def TruncSatZeroSVecF64x2ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatZeroSVecF64x2ToVecI32x4()


BinaryenTruncSatZeroSVecF64x2ToVecI32x4 = TruncSatZeroSVecF64x2ToVecI32x4


def TruncSatZeroUVecF64x2ToVecI32x4() -> BinaryenOp:
    return lib.BinaryenTruncSatZeroUVecF64x2ToVecI32x4()


BinaryenTruncSatZeroUVecF64x2ToVecI32x4 = TruncSatZeroUVecF64x2ToVecI32x4


def DemoteZeroVecF64x2ToVecF32x4() -> BinaryenOp:
    return lib.BinaryenDemoteZeroVecF64x2ToVecF32x4()


BinaryenDemoteZeroVecF64x2ToVecF32x4 = DemoteZeroVecF64x2ToVecF32x4


def PromoteLowVecF32x4ToVecF64x2() -> BinaryenOp:
    return lib.BinaryenPromoteLowVecF32x4ToVecF64x2()


BinaryenPromoteLowVecF32x4ToVecF64x2 = PromoteLowVecF32x4ToVecF64x2


def SwizzleVecI8x16() -> BinaryenOp:
    return lib.BinaryenSwizzleVecI8x16()


BinaryenSwizzleVecI8x16 = SwizzleVecI8x16


def RefIsNull() -> BinaryenOp:
    return lib.BinaryenRefIsNull()


BinaryenRefIsNull = RefIsNull


def RefIsFunc() -> BinaryenOp:
    return lib.BinaryenRefIsFunc()


BinaryenRefIsFunc = RefIsFunc


def RefIsData() -> BinaryenOp:
    return lib.BinaryenRefIsData()


BinaryenRefIsData = RefIsData


def RefIsI31() -> BinaryenOp:
    return lib.BinaryenRefIsI31()


BinaryenRefIsI31 = RefIsI31


def RefAsNonNull() -> BinaryenOp:
    return lib.BinaryenRefAsNonNull()


BinaryenRefAsNonNull = RefAsNonNull


def RefAsFunc() -> BinaryenOp:
    return lib.BinaryenRefAsFunc()


BinaryenRefAsFunc = RefAsFunc


def RefAsData() -> BinaryenOp:
    return lib.BinaryenRefAsData()


BinaryenRefAsData = RefAsData


def RefAsI31() -> BinaryenOp:
    return lib.BinaryenRefAsI31()


BinaryenRefAsI31 = RefAsI31


def RefAsExternInternalize() -> BinaryenOp:
    return lib.BinaryenRefAsExternInternalize()


BinaryenRefAsExternInternalize = RefAsExternInternalize


def RefAsExternExternalize() -> BinaryenOp:
    return lib.BinaryenRefAsExternExternalize()


BinaryenRefAsExternExternalize = RefAsExternExternalize


def BrOnNull() -> BinaryenOp:
    return lib.BinaryenBrOnNull()


BinaryenBrOnNull = BrOnNull


def BrOnNonNull() -> BinaryenOp:
    return lib.BinaryenBrOnNonNull()


BinaryenBrOnNonNull = BrOnNonNull


def BrOnCast() -> BinaryenOp:
    return lib.BinaryenBrOnCast()


BinaryenBrOnCast = BrOnCast


def BrOnCastFail() -> BinaryenOp:
    return lib.BinaryenBrOnCastFail()


BinaryenBrOnCastFail = BrOnCastFail


def BrOnFunc() -> BinaryenOp:
    return lib.BinaryenBrOnFunc()


BinaryenBrOnFunc = BrOnFunc


def BrOnNonFunc() -> BinaryenOp:
    return lib.BinaryenBrOnNonFunc()


BinaryenBrOnNonFunc = BrOnNonFunc


def BrOnData() -> BinaryenOp:
    return lib.BinaryenBrOnData()


BinaryenBrOnData = BrOnData


def BrOnNonData() -> BinaryenOp:
    return lib.BinaryenBrOnNonData()


BinaryenBrOnNonData = BrOnNonData


def BrOnI31() -> BinaryenOp:
    return lib.BinaryenBrOnI31()


BinaryenBrOnI31 = BrOnI31


def BrOnNonI31() -> BinaryenOp:
    return lib.BinaryenBrOnNonI31()


BinaryenBrOnNonI31 = BrOnNonI31


def StringNewUTF8() -> BinaryenOp:
    return lib.BinaryenStringNewUTF8()


BinaryenStringNewUTF8 = StringNewUTF8


def StringNewWTF8() -> BinaryenOp:
    return lib.BinaryenStringNewWTF8()


BinaryenStringNewWTF8 = StringNewWTF8


def StringNewReplace() -> BinaryenOp:
    return lib.BinaryenStringNewReplace()


BinaryenStringNewReplace = StringNewReplace


def StringNewWTF16() -> BinaryenOp:
    return lib.BinaryenStringNewWTF16()


BinaryenStringNewWTF16 = StringNewWTF16


def StringNewUTF8Array() -> BinaryenOp:
    return lib.BinaryenStringNewUTF8Array()


BinaryenStringNewUTF8Array = StringNewUTF8Array


def StringNewWTF8Array() -> BinaryenOp:
    return lib.BinaryenStringNewWTF8Array()


BinaryenStringNewWTF8Array = StringNewWTF8Array


def StringNewReplaceArray() -> BinaryenOp:
    return lib.BinaryenStringNewReplaceArray()


BinaryenStringNewReplaceArray = StringNewReplaceArray


def StringNewWTF16Array() -> BinaryenOp:
    return lib.BinaryenStringNewWTF16Array()


BinaryenStringNewWTF16Array = StringNewWTF16Array


def StringMeasureUTF8() -> BinaryenOp:
    return lib.BinaryenStringMeasureUTF8()


BinaryenStringMeasureUTF8 = StringMeasureUTF8


def StringMeasureWTF8() -> BinaryenOp:
    return lib.BinaryenStringMeasureWTF8()


BinaryenStringMeasureWTF8 = StringMeasureWTF8


def StringMeasureWTF16() -> BinaryenOp:
    return lib.BinaryenStringMeasureWTF16()


BinaryenStringMeasureWTF16 = StringMeasureWTF16


def StringMeasureIsUSV() -> BinaryenOp:
    return lib.BinaryenStringMeasureIsUSV()


BinaryenStringMeasureIsUSV = StringMeasureIsUSV


def StringMeasureWTF16View() -> BinaryenOp:
    return lib.BinaryenStringMeasureWTF16View()


BinaryenStringMeasureWTF16View = StringMeasureWTF16View


def StringEncodeUTF8() -> BinaryenOp:
    return lib.BinaryenStringEncodeUTF8()


BinaryenStringEncodeUTF8 = StringEncodeUTF8


def StringEncodeWTF8() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF8()


BinaryenStringEncodeWTF8 = StringEncodeWTF8


def StringEncodeWTF16() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF16()


BinaryenStringEncodeWTF16 = StringEncodeWTF16


def StringEncodeUTF8Array() -> BinaryenOp:
    return lib.BinaryenStringEncodeUTF8Array()


BinaryenStringEncodeUTF8Array = StringEncodeUTF8Array


def StringEncodeWTF8Array() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF8Array()


BinaryenStringEncodeWTF8Array = StringEncodeWTF8Array


def StringEncodeWTF16Array() -> BinaryenOp:
    return lib.BinaryenStringEncodeWTF16Array()


BinaryenStringEncodeWTF16Array = StringEncodeWTF16Array


def StringAsWTF8() -> BinaryenOp:
    return lib.BinaryenStringAsWTF8()


BinaryenStringAsWTF8 = StringAsWTF8


def StringAsWTF16() -> BinaryenOp:
    return lib.BinaryenStringAsWTF16()


BinaryenStringAsWTF16 = StringAsWTF16


def StringAsIter() -> BinaryenOp:
    return lib.BinaryenStringAsIter()


BinaryenStringAsIter = StringAsIter


def StringIterMoveAdvance() -> BinaryenOp:
    return lib.BinaryenStringIterMoveAdvance()


BinaryenStringIterMoveAdvance = StringIterMoveAdvance


def StringIterMoveRewind() -> BinaryenOp:
    return lib.BinaryenStringIterMoveRewind()


BinaryenStringIterMoveRewind = StringIterMoveRewind


def StringSliceWTF8() -> BinaryenOp:
    return lib.BinaryenStringSliceWTF8()


BinaryenStringSliceWTF8 = StringSliceWTF8


def StringSliceWTF16() -> BinaryenOp:
    return lib.BinaryenStringSliceWTF16()


BinaryenStringSliceWTF16 = StringSliceWTF16


def Block(
    module: BinaryenModuleRef,
    name: Optional[str],
    children: Optional[BinaryenExpressionRef | List[BinaryenExpressionRef]],
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    """
    Block: name can be NULL. Specifying BinaryenUndefined() as the 'type'
    parameter indicates that the block's type shall be figured out
    automatically instead of explicitly providing it. This conforms
    to the behavior before the 'type' parameter has been introduced.
    """
    return lib.BinaryenBlock(module, _enc(name), _opt_seq(children), _len(children), _type)


BinaryenBlock = Block


def If(
    module: BinaryenModuleRef,
    condition: BinaryenExpressionRef,
    if_true: BinaryenExpressionRef,
    if_false: Optional[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    """ If: ifFalse can be NULL """
    return lib.BinaryenIf(module, condition, if_true, _opt(if_false))


BinaryenIf = If


def Loop(
    module: BinaryenModuleRef,
    _in: Optional[str],
    body: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenLoop(module, _enc(_in), body)


BinaryenLoop = Loop


def Break(
    module: BinaryenModuleRef,
    name: str,
    condition: Optional[BinaryenExpressionRef],
    value: Optional[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    """ Break: value and condition can be NULL """
    return lib.BinaryenBreak(module, _enc(name), _opt(condition), _opt(value))


BinaryenBreak = Break


def Switch(
    module: BinaryenModuleRef,
    names: List[str],
    default_name: str,
    condition: BinaryenExpressionRef,
    value: Optional[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    """ Switch: value can be NULL """
    return lib.BinaryenSwitch(module, _enc_seq(names), _len(names), _enc(default_name), condition, _opt(value))


BinaryenSwitch = Switch


def Call(
    module: BinaryenModuleRef,
    target: str,
    operands: List[BinaryenExpressionRef],
    return_type: BinaryenType,
) -> BinaryenExpressionRef:
    """
    Call: Note the 'returnType' parameter. You must declare the
    type returned by the function being called, as that
    function might not have been created yet, so we don't
    know what it is.
    """
    return lib.BinaryenCall(module, _enc(target), operands, _len(operands), return_type)


BinaryenCall = Call


def CallIndirect(
    module: BinaryenModuleRef,
    table: str,
    target: BinaryenExpressionRef,
    operands: Optional[List[BinaryenExpressionRef]],
    params: BinaryenType,
    results: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallIndirect(
        module, _enc(table), target, _opt_seq(operands), _len(operands), params, results
    )


BinaryenCallIndirect = CallIndirect


def ReturnCall(
    module: BinaryenModuleRef,
    target: str,
    operands: List[BinaryenExpressionRef],
    return_type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenReturnCall(module, _enc(target), operands, _len(operands), return_type)


BinaryenReturnCall = ReturnCall


def ReturnCallIndirect(
    module: BinaryenModuleRef,
    table: str,
    target: BinaryenExpressionRef,
    operands: List[BinaryenExpressionRef],
    params: BinaryenType,
    results: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenReturnCallIndirect(module, _enc(table), target, operands, _len(operands), params, results)


BinaryenReturnCallIndirect = ReturnCallIndirect


def LocalGet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    """
    LocalGet: Note the 'type' parameter. It might seem redundant, since the
    local at that index must have a type. However, this API lets you
    build code "top-down": create a node, then its parents, and so
    on, and finally create the function at the end. (Note that in fact
    you do not mention a function when creating ExpressionRefs, only
    a module.) And since LocalGet is a leaf node, we need to be told
    its type. (Other nodes detect their type either from their
    type or their opcode, or failing that, their children. But
    LocalGet has no children, it is where a "stream" of type info
    begins.)
    Note also that the index of a local can refer to a param or
    a var, that is, either a parameter to the function or a variable
    declared when you call BinaryenAddFunction. See BinaryenAddFunction
    for more details.
    """
    return lib.BinaryenLocalGet(module, index, _type)


BinaryenLocalGet = LocalGet


def LocalSet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenLocalSet(module, index, value)


BinaryenLocalSet = LocalSet


def LocalTee(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenLocalTee(module, index, value, _type)


BinaryenLocalTee = LocalTee


def GlobalGet(
    module: BinaryenModuleRef,
    name: str,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenGlobalGet(module, _enc(name), _type)


BinaryenGlobalGet = GlobalGet


def GlobalSet(
    module: BinaryenModuleRef,
    name: str,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenGlobalSet(module, _enc(name), value)


BinaryenGlobalSet = GlobalSet


def Load(
    module: BinaryenModuleRef,
    _bytes: int,
    signed_: bool,
    offset: int,
    align: int,
    _type: BinaryenType,
    ptr: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    """
    Load: align can be 0, in which case it will be the natural alignment (equal
    to bytes)
    """
    return lib.BinaryenLoad(module, _bytes, signed_, offset, align, _type, ptr, _enc(memory_name))


BinaryenLoad = Load


def Store(
    module: BinaryenModuleRef,
    _bytes: int,
    offset: int,
    align: int,
    ptr: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    """
    Store: align can be 0, in which case it will be the natural alignment (equal
    to bytes)
    """
    return lib.BinaryenStore(module, _bytes, offset, align, ptr, value, _type, _enc(memory_name))


BinaryenStore = Store


def Const(
    module: BinaryenModuleRef,
    value: BinaryenLiteral,
) -> BinaryenExpressionRef:
    return lib.BinaryenConst(module, value)


BinaryenConst = Const


def Unary(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenUnary(module, op, value)


BinaryenUnary = Unary


def Binary(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenBinary(module, op, left, right)


BinaryenBinary = Binary


def Select(
    module: BinaryenModuleRef,
    condition: BinaryenExpressionRef,
    if_true: BinaryenExpressionRef,
    if_false: BinaryenExpressionRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenSelect(module, condition, if_true, if_false, _type)


BinaryenSelect = Select


def Drop(
    module: BinaryenModuleRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenDrop(module, value)


BinaryenDrop = Drop


def Return(
    module: BinaryenModuleRef,
    value: Optional[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    """ Return: value can be NULL """
    return lib.BinaryenReturn(module, _opt(value))


BinaryenReturn = Return


def MemorySize(
    module: BinaryenModuleRef,
    memory_name: str,
    memory_is64: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemorySize(module, _enc(memory_name), memory_is64)


BinaryenMemorySize = MemorySize


def MemoryGrow(
    module: BinaryenModuleRef,
    delta: BinaryenExpressionRef,
    memory_name: str,
    memory_is64: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryGrow(module, delta, _enc(memory_name), memory_is64)


BinaryenMemoryGrow = MemoryGrow


def Nop(
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenNop(module)


BinaryenNop = Nop


def Unreachable(
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenUnreachable(module)


BinaryenUnreachable = Unreachable


def AtomicLoad(
    module: BinaryenModuleRef,
    _bytes: int,
    offset: int,
    _type: BinaryenType,
    ptr: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicLoad(module, _bytes, offset, _type, ptr, _enc(memory_name))


BinaryenAtomicLoad = AtomicLoad


def AtomicStore(
    module: BinaryenModuleRef,
    _bytes: int,
    offset: int,
    ptr: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicStore(module, _bytes, offset, ptr, value, _type, _enc(memory_name))


BinaryenAtomicStore = AtomicStore


def AtomicRMW(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    _bytes: BinaryenIndex,
    offset: BinaryenIndex,
    ptr: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicRMW(module, op, _bytes, offset, ptr, value, _type, _enc(memory_name))


BinaryenAtomicRMW = AtomicRMW


def AtomicCmpxchg(
    module: BinaryenModuleRef,
    _bytes: BinaryenIndex,
    offset: BinaryenIndex,
    ptr: BinaryenExpressionRef,
    expected: BinaryenExpressionRef,
    replacement: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicCmpxchg(module, _bytes, offset, ptr, expected, replacement, _type, _enc(memory_name))


BinaryenAtomicCmpxchg = AtomicCmpxchg


def AtomicWait(
    module: BinaryenModuleRef,
    ptr: BinaryenExpressionRef,
    expected: BinaryenExpressionRef,
    timeout: BinaryenExpressionRef,
    _type: BinaryenType,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicWait(module, ptr, expected, timeout, _type, _enc(memory_name))


BinaryenAtomicWait = AtomicWait


def AtomicNotify(
    module: BinaryenModuleRef,
    ptr: BinaryenExpressionRef,
    notify_count: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicNotify(module, ptr, notify_count, _enc(memory_name))


BinaryenAtomicNotify = AtomicNotify


def AtomicFence(
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenAtomicFence(module)


BinaryenAtomicFence = AtomicFence


def SIMDExtract(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    vec: BinaryenExpressionRef,
    index: int,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDExtract(module, op, vec, index)


BinaryenSIMDExtract = SIMDExtract


def SIMDReplace(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    vec: BinaryenExpressionRef,
    index: int,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDReplace(module, op, vec, index, value)


BinaryenSIMDReplace = SIMDReplace


def SIMDShuffle(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
    mask: bytes,
) -> BinaryenExpressionRef:
    assert len(mask) == 16
    return lib.BinaryenSIMDShuffle(module, left, right, mask)


BinaryenSIMDShuffle = SIMDShuffle


def SIMDTernary(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    a: BinaryenExpressionRef,
    b: BinaryenExpressionRef,
    c: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDTernary(module, op, a, b, c)


BinaryenSIMDTernary = SIMDTernary


def SIMDShift(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    vec: BinaryenExpressionRef,
    shift: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDShift(module, op, vec, shift)


BinaryenSIMDShift = SIMDShift


def SIMDLoad(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    offset: int,
    align: int,
    ptr: BinaryenExpressionRef,
    name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDLoad(module, op, offset, align, ptr, _enc(name))


BinaryenSIMDLoad = SIMDLoad


def SIMDLoadStoreLane(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    offset: int,
    align: int,
    index: int,
    ptr: BinaryenExpressionRef,
    vec: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenSIMDLoadStoreLane(module, op, offset, align, index, ptr, vec, _enc(memory_name))


BinaryenSIMDLoadStoreLane = SIMDLoadStoreLane


def MemoryInit(
    module: BinaryenModuleRef,
    segment: int,
    dest: BinaryenExpressionRef,
    offset: BinaryenExpressionRef,
    size: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryInit(module, segment, dest, offset, size, _enc(memory_name))


BinaryenMemoryInit = MemoryInit


def DataDrop(
    module: BinaryenModuleRef,
    segment: int,
) -> BinaryenExpressionRef:
    return lib.BinaryenDataDrop(module, segment)


BinaryenDataDrop = DataDrop


def MemoryCopy(
    module: BinaryenModuleRef,
    dest: BinaryenExpressionRef,
    source: BinaryenExpressionRef,
    size: BinaryenExpressionRef,
    dest_memory: str,
    source_memory: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryCopy(module, dest, source, size, _enc(dest_memory), _enc(source_memory))


BinaryenMemoryCopy = MemoryCopy


def MemoryFill(
    module: BinaryenModuleRef,
    dest: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
    size: BinaryenExpressionRef,
    memory_name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenMemoryFill(module, dest, value, size, _enc(memory_name))


BinaryenMemoryFill = MemoryFill


def RefNull(
    module: BinaryenModuleRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefNull(module, _type)


BinaryenRefNull = RefNull


def RefIs(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefIs(module, op, value)


BinaryenRefIs = RefIs


def RefAs(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefAs(module, op, value)


BinaryenRefAs = RefAs


def RefFunc(
    module: BinaryenModuleRef,
    func: str,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefFunc(module, _enc(func), _type)


BinaryenRefFunc = RefFunc


def RefEq(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefEq(module, left, right)


BinaryenRefEq = RefEq


def TableGet(
    module: BinaryenModuleRef,
    name: str,
    index: BinaryenExpressionRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableGet(module, _enc(name), index, _type)


BinaryenTableGet = TableGet


def TableSet(
    module: BinaryenModuleRef,
    name: str,
    index: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableSet(module, _enc(name), index, value)


BinaryenTableSet = TableSet


def TableSize(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableSize(module, _enc(name))


BinaryenTableSize = TableSize


def TableGrow(
    module: BinaryenModuleRef,
    name: str,
    value: BinaryenExpressionRef,
    delta: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenTableGrow(module, _enc(name), value, delta)


BinaryenTableGrow = TableGrow


def Try(
    module: BinaryenModuleRef,
    name: Optional[str],
    body: BinaryenExpressionRef,
    catch_tags: List[str],
    catch_bodies: List[BinaryenExpressionRef],
    delegate_target: Optional[str],
) -> BinaryenExpressionRef:
    """ Try: name can be NULL. delegateTarget should be NULL in try-catch. """
    return lib.BinaryenTry(
        module, _enc(name), body, _enc_seq(catch_tags), _len(catch_tags),
        catch_bodies, _len(catch_bodies), _enc(delegate_target)
    )


BinaryenTry = Try


def Throw(
    module: BinaryenModuleRef,
    tag: str,
    operands: List[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenThrow(module, _enc(tag), operands, _len(operands))


BinaryenThrow = Throw


def Rethrow(
    module: BinaryenModuleRef,
    target: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenRethrow(module, _enc(target))


BinaryenRethrow = Rethrow


def TupleMake(
    module: BinaryenModuleRef,
    operands: List[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenTupleMake(module, operands, _len(operands))


BinaryenTupleMake = TupleMake


def TupleExtract(
    module: BinaryenModuleRef,
    _tuple: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenTupleExtract(module, _tuple, index)


BinaryenTupleExtract = TupleExtract


def Pop(
    module: BinaryenModuleRef,
    _type: BinaryenType,
) -> BinaryenExpressionRef:
    return lib.BinaryenPop(module, _type)


BinaryenPop = Pop


def I31New(
    module: BinaryenModuleRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenI31New(module, value)


BinaryenI31New = I31New


def I31Get(
    module: BinaryenModuleRef,
    i31: BinaryenExpressionRef,
    signed_: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenI31Get(module, i31, signed_)


BinaryenI31Get = I31Get


def CallRef(
    module: BinaryenModuleRef,
    target: BinaryenExpressionRef,
    operands: List[BinaryenExpressionRef],
    _type: BinaryenType,
    is_return: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRef(module, target, operands, _len(operands), _type, is_return)


BinaryenCallRef = CallRef


def RefTest(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefTest(module, ref, intended_type)


BinaryenRefTest = RefTest


def RefCast(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefCast(module, ref, intended_type)


BinaryenRefCast = RefCast


def BrOn(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    name: str,
    ref: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenBrOn(module, op, _enc(name), ref, intended_type)


BinaryenBrOn = BrOn


def StructNew(
    module: BinaryenModuleRef,
    operands: Optional[List[BinaryenExpressionRef]],
    _type: BinaryenHeapType,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructNew(module, _opt_seq(operands), _len(operands), _type)


BinaryenStructNew = StructNew


def StructGet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    ref: BinaryenExpressionRef,
    _type: BinaryenType,
    signed_: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructGet(module, index, ref, _type, signed_)


BinaryenStructGet = StructGet


def StructSet(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
    ref: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructSet(module, index, ref, value)


BinaryenStructSet = StructSet


def ArrayNew(
    module: BinaryenModuleRef,
    _type: BinaryenHeapType,
    size: BinaryenExpressionRef,
    init: Optional[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayNew(module, _type, size, _opt(init))


BinaryenArrayNew = ArrayNew


def ArrayInit(
    module: BinaryenModuleRef,
    _type: BinaryenHeapType,
    values: List[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayInit(module, _type, values, _len(values))


BinaryenArrayInit = ArrayInit


def ArrayGet(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    index: BinaryenExpressionRef,
    _type: BinaryenType,
    signed_: bool,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayGet(module, ref, index, _type, signed_)


BinaryenArrayGet = ArrayGet


def ArraySet(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    index: BinaryenExpressionRef,
    value: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArraySet(module, ref, index, value)


BinaryenArraySet = ArraySet


def ArrayLen(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayLen(module, ref)


BinaryenArrayLen = ArrayLen


def ArrayCopy(
    module: BinaryenModuleRef,
    dest_ref: BinaryenExpressionRef,
    dest_index: BinaryenExpressionRef,
    src_ref: BinaryenExpressionRef,
    src_index: BinaryenExpressionRef,
    length: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopy(module, dest_ref, dest_index, src_ref, src_index, length)


BinaryenArrayCopy = ArrayCopy


def StringNew(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ptr: BinaryenExpressionRef,
    length: Optional[BinaryenExpressionRef],
    start: Optional[BinaryenExpressionRef],
    end: Optional[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNew(module, op, ptr, _opt(length), _opt(start), _opt(end))


BinaryenStringNew = StringNew


def StringConst(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringConst(module, _enc(name))


BinaryenStringConst = StringConst


def StringMeasure(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringMeasure(module, op, ref)


BinaryenStringMeasure = StringMeasure


def StringEncode(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
    ptr: BinaryenExpressionRef,
    start: Optional[BinaryenExpressionRef],
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncode(module, op, ref, ptr, _opt(start))


BinaryenStringEncode = StringEncode


def StringConcat(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringConcat(module, left, right)


BinaryenStringConcat = StringConcat


def StringEq(
    module: BinaryenModuleRef,
    left: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEq(module, left, right)


BinaryenStringEq = StringEq


def StringAs(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringAs(module, op, ref)


BinaryenStringAs = StringAs


def StringWTF8Advance(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    pos: BinaryenExpressionRef,
    _bytes: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF8Advance(module, ref, pos, _bytes)


BinaryenStringWTF8Advance = StringWTF8Advance


def StringWTF16Get(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    pos: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF16Get(module, ref, pos)


BinaryenStringWTF16Get = StringWTF16Get


def StringIterNext(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterNext(module, ref)


BinaryenStringIterNext = StringIterNext


def StringIterMove(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
    num: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterMove(module, op, ref, num)


BinaryenStringIterMove = StringIterMove


def StringSliceWTF(
    module: BinaryenModuleRef,
    op: BinaryenOp,
    ref: BinaryenExpressionRef,
    start: BinaryenExpressionRef,
    end: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTF(module, op, ref, start, end)


BinaryenStringSliceWTF = StringSliceWTF


def StringSliceIter(
    module: BinaryenModuleRef,
    ref: BinaryenExpressionRef,
    num: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceIter(module, ref, num)


BinaryenStringSliceIter = StringSliceIter


def ExpressionGetId(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionId:
    """ Gets the id (kind) of the given expression. """
    return lib.BinaryenExpressionGetId(expr)


BinaryenExpressionGetId = ExpressionGetId


def ExpressionGetType(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the type of the given expression. """
    return lib.BinaryenExpressionGetType(expr)


BinaryenExpressionGetType = ExpressionGetType


def ExpressionSetType(
    expr: BinaryenExpressionRef,
    _type: BinaryenType,
) -> None:
    """ Sets the type of the given expression. """
    lib.BinaryenExpressionSetType(expr, _type)


BinaryenExpressionSetType = ExpressionSetType


def ExpressionPrint(
    expr: BinaryenExpressionRef,
) -> None:
    """ Prints text format of the given expression to stdout. """
    lib.BinaryenExpressionPrint(expr)


BinaryenExpressionPrint = ExpressionPrint


def ExpressionFinalize(
    expr: BinaryenExpressionRef,
) -> None:
    """ Re-finalizes an expression after it has been modified. """
    lib.BinaryenExpressionFinalize(expr)


BinaryenExpressionFinalize = ExpressionFinalize


def ExpressionCopy(
    expr: BinaryenExpressionRef,
    module: BinaryenModuleRef,
) -> BinaryenExpressionRef:
    """ Makes a deep copy of the given expression. """
    return lib.BinaryenExpressionCopy(expr, module)


BinaryenExpressionCopy = ExpressionCopy


def BlockGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name (label) of a `block` expression. """
    return _dec(lib.BinaryenBlockGetName(expr))


BinaryenBlockGetName = BlockGetName


def BlockSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (label) of a `block` expression. """
    lib.BinaryenBlockSetName(expr, _enc(name))


BinaryenBlockSetName = BlockSetName


def BlockGetNumChildren(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of child expressions of a `block` expression. """
    return lib.BinaryenBlockGetNumChildren(expr)


BinaryenBlockGetNumChildren = BlockGetNumChildren


def BlockGetChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the child expression at the specified index of a `block` expression. """
    return lib.BinaryenBlockGetChildAt(expr, index)


BinaryenBlockGetChildAt = BlockGetChildAt


def BlockSetChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    child_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets (replaces) the child expression at the specified index of a `block`
    expression.
    """
    lib.BinaryenBlockSetChildAt(expr, index, child_expr)


BinaryenBlockSetChildAt = BlockSetChildAt


def BlockAppendChild(
    expr: BinaryenExpressionRef,
    child_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends a child expression to a `block` expression, returning its insertion
    index.
    """
    return lib.BinaryenBlockAppendChild(expr, child_expr)


BinaryenBlockAppendChild = BlockAppendChild


def BlockInsertChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    child_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts a child expression at the specified index of a `block` expression,
    moving existing children including the one previously at that index one index
    up.
    """
    lib.BinaryenBlockInsertChildAt(expr, index, child_expr)


BinaryenBlockInsertChildAt = BlockInsertChildAt


def BlockRemoveChildAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the child expression at the specified index of a `block` expression,
    moving all subsequent children one index down. Returns the child expression.
    """
    return lib.BinaryenBlockRemoveChildAt(expr, index)


BinaryenBlockRemoveChildAt = BlockRemoveChildAt


def IfGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the condition expression of an `if` expression. """
    return lib.BinaryenIfGetCondition(expr)


BinaryenIfGetCondition = IfGetCondition


def IfSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the condition expression of an `if` expression. """
    lib.BinaryenIfSetCondition(expr, cond_expr)


BinaryenIfSetCondition = IfSetCondition


def IfGetIfTrue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the ifTrue (then) expression of an `if` expression. """
    return lib.BinaryenIfGetIfTrue(expr)


BinaryenIfGetIfTrue = IfGetIfTrue


def IfSetIfTrue(
    expr: BinaryenExpressionRef,
    if_true_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the ifTrue (then) expression of an `if` expression. """
    lib.BinaryenIfSetIfTrue(expr, if_true_expr)


BinaryenIfSetIfTrue = IfSetIfTrue


def IfGetIfFalse(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the ifFalse (else) expression, if any, of an `if` expression. """
    return lib.BinaryenIfGetIfFalse(expr)


BinaryenIfGetIfFalse = IfGetIfFalse


def IfSetIfFalse(
    expr: BinaryenExpressionRef,
    if_false_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the ifFalse (else) expression, if any, of an `if` expression. """
    lib.BinaryenIfSetIfFalse(expr, if_false_expr)


BinaryenIfSetIfFalse = IfSetIfFalse


def LoopGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name (label) of a `loop` expression. """
    return _dec(lib.BinaryenLoopGetName(expr))


BinaryenLoopGetName = LoopGetName


def LoopSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (label) of a `loop` expression. """
    lib.BinaryenLoopSetName(expr, _enc(name))


BinaryenLoopSetName = LoopSetName


def LoopGetBody(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the body expression of a `loop` expression. """
    return lib.BinaryenLoopGetBody(expr)


BinaryenLoopGetBody = LoopGetBody


def LoopSetBody(
    expr: BinaryenExpressionRef,
    body_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the body expression of a `loop` expression. """
    lib.BinaryenLoopSetBody(expr, body_expr)


BinaryenLoopSetBody = LoopSetBody


def BreakGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name (target label) of a `br` or `br_if` expression. """
    return _dec(lib.BinaryenBreakGetName(expr))


BinaryenBreakGetName = BreakGetName


def BreakSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (target label) of a `br` or `br_if` expression. """
    lib.BinaryenBreakSetName(expr, _enc(name))


BinaryenBreakSetName = BreakSetName


def BreakGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the condition expression, if any, of a `br_if` expression. No condition
    indicates a `br` expression.
    """
    return lib.BinaryenBreakGetCondition(expr)


BinaryenBreakGetCondition = BreakGetCondition


def BreakSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the condition expression, if any, of a `br_if` expression. No condition
    makes it a `br` expression.
    """
    lib.BinaryenBreakSetCondition(expr, cond_expr)


BinaryenBreakSetCondition = BreakSetCondition


def BreakGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression, if any, of a `br` or `br_if` expression. """
    return lib.BinaryenBreakGetValue(expr)


BinaryenBreakGetValue = BreakGetValue


def BreakSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression, if any, of a `br` or `br_if` expression. """
    lib.BinaryenBreakSetValue(expr, value_expr)


BinaryenBreakSetValue = BreakSetValue


def SwitchGetNumNames(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of names (target labels) of a `br_table` expression. """
    return lib.BinaryenSwitchGetNumNames(expr)


BinaryenSwitchGetNumNames = SwitchGetNumNames


def SwitchGetNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """
    Gets the name (target label) at the specified index of a `br_table`
    expression.
    """
    return _dec(lib.BinaryenSwitchGetNameAt(expr, index))


BinaryenSwitchGetNameAt = SwitchGetNameAt


def SwitchSetNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    name: str,
) -> None:
    """
    Sets the name (target label) at the specified index of a `br_table`
    expression.
    """
    lib.BinaryenSwitchSetNameAt(expr, index, _enc(name))


BinaryenSwitchSetNameAt = SwitchSetNameAt


def SwitchAppendName(
    expr: BinaryenExpressionRef,
    name: str,
) -> BinaryenIndex:
    """ Appends a name to a `br_table` expression, returning its insertion index. """
    return lib.BinaryenSwitchAppendName(expr, _enc(name))


BinaryenSwitchAppendName = SwitchAppendName


def SwitchInsertNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    name: str,
) -> None:
    """
    Inserts a name at the specified index of a `br_table` expression, moving
    existing names including the one previously at that index one index up.
    """
    lib.BinaryenSwitchInsertNameAt(expr, index, _enc(name))


BinaryenSwitchInsertNameAt = SwitchInsertNameAt


def SwitchRemoveNameAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """
    Removes the name at the specified index of a `br_table` expression, moving
    all subsequent names one index down. Returns the name.
    """
    return _dec(lib.BinaryenSwitchRemoveNameAt(expr, index))


BinaryenSwitchRemoveNameAt = SwitchRemoveNameAt


def SwitchGetDefaultName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the default name (target label), if any, of a `br_table` expression. """
    return _dec(lib.BinaryenSwitchGetDefaultName(expr))


BinaryenSwitchGetDefaultName = SwitchGetDefaultName


def SwitchSetDefaultName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the default name (target label), if any, of a `br_table` expression. """
    lib.BinaryenSwitchSetDefaultName(expr, _enc(name))


BinaryenSwitchSetDefaultName = SwitchSetDefaultName


def SwitchGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the condition expression of a `br_table` expression. """
    return lib.BinaryenSwitchGetCondition(expr)


BinaryenSwitchGetCondition = SwitchGetCondition


def SwitchSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the condition expression of a `br_table` expression. """
    lib.BinaryenSwitchSetCondition(expr, cond_expr)


BinaryenSwitchSetCondition = SwitchSetCondition


def SwitchGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression, if any, of a `br_table` expression. """
    return lib.BinaryenSwitchGetValue(expr)


BinaryenSwitchGetValue = SwitchGetValue


def SwitchSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression, if any, of a `br_table` expression. """
    lib.BinaryenSwitchSetValue(expr, value_expr)


BinaryenSwitchSetValue = SwitchSetValue


def CallGetTarget(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the target function name of a `call` expression. """
    return _dec(lib.BinaryenCallGetTarget(expr))


BinaryenCallGetTarget = CallGetTarget


def CallSetTarget(
    expr: BinaryenExpressionRef,
    target: str,
) -> None:
    """ Sets the target function name of a `call` expression. """
    lib.BinaryenCallSetTarget(expr, _enc(target))


BinaryenCallSetTarget = CallSetTarget


def CallGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of operands of a `call` expression. """
    return lib.BinaryenCallGetNumOperands(expr)


BinaryenCallGetNumOperands = CallGetNumOperands


def CallGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the operand expression at the specified index of a `call` expression. """
    return lib.BinaryenCallGetOperandAt(expr, index)


BinaryenCallGetOperandAt = CallGetOperandAt


def CallSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the operand expression at the specified index of a `call` expression. """
    lib.BinaryenCallSetOperandAt(expr, index, operand_expr)


BinaryenCallSetOperandAt = CallSetOperandAt


def CallAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `call` expression, returning its insertion
    index.
    """
    return lib.BinaryenCallAppendOperand(expr, operand_expr)


BinaryenCallAppendOperand = CallAppendOperand


def CallInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `call` expression,
    moving existing operands including the one previously at that index one index
    up.
    """
    lib.BinaryenCallInsertOperandAt(expr, index, operand_expr)


BinaryenCallInsertOperandAt = CallInsertOperandAt


def CallRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `call` expression,
    moving all subsequent operands one index down. Returns the operand
    expression.
    """
    return lib.BinaryenCallRemoveOperandAt(expr, index)


BinaryenCallRemoveOperandAt = CallRemoveOperandAt


def CallIsReturn(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether the specified `call` expression is a tail call. """
    return lib.BinaryenCallIsReturn(expr)


BinaryenCallIsReturn = CallIsReturn


def CallSetReturn(
    expr: BinaryenExpressionRef,
    is_return: bool,
) -> None:
    """ Sets whether the specified `call` expression is a tail call. """
    lib.BinaryenCallSetReturn(expr, is_return)


BinaryenCallSetReturn = CallSetReturn


def CallIndirectGetTarget(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the target expression of a `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetTarget(expr)


BinaryenCallIndirectGetTarget = CallIndirectGetTarget


def CallIndirectSetTarget(
    expr: BinaryenExpressionRef,
    target_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the target expression of a `call_indirect` expression. """
    lib.BinaryenCallIndirectSetTarget(expr, target_expr)


BinaryenCallIndirectSetTarget = CallIndirectSetTarget


def CallIndirectGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the table name of a `call_indirect` expression. """
    return _dec(lib.BinaryenCallIndirectGetTable(expr))


BinaryenCallIndirectGetTable = CallIndirectGetTable


def CallIndirectSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the table name of a `call_indirect` expression. """
    lib.BinaryenCallIndirectSetTable(expr, _enc(table))


BinaryenCallIndirectSetTable = CallIndirectSetTable


def CallIndirectGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of operands of a `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetNumOperands(expr)


BinaryenCallIndirectGetNumOperands = CallIndirectGetNumOperands


def CallIndirectGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Gets the operand expression at the specified index of a `call_indirect`
    expression.
    """
    return lib.BinaryenCallIndirectGetOperandAt(expr, index)


BinaryenCallIndirectGetOperandAt = CallIndirectGetOperandAt


def CallIndirectSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the operand expression at the specified index of a `call_indirect`
    expression.
    """
    lib.BinaryenCallIndirectSetOperandAt(expr, index, operand_expr)


BinaryenCallIndirectSetOperandAt = CallIndirectSetOperandAt


def CallIndirectAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `call_indirect` expression, returning its
    insertion index.
    """
    return lib.BinaryenCallIndirectAppendOperand(expr, operand_expr)


BinaryenCallIndirectAppendOperand = CallIndirectAppendOperand


def CallIndirectInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `call_indirect`
    expression, moving existing operands including the one previously at that
    index one index up.
    """
    lib.BinaryenCallIndirectInsertOperandAt(expr, index, operand_expr)


BinaryenCallIndirectInsertOperandAt = CallIndirectInsertOperandAt


def CallIndirectRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `call_indirect`
    expression, moving all subsequent operands one index down. Returns the
    operand expression.
    """
    return lib.BinaryenCallIndirectRemoveOperandAt(expr, index)


BinaryenCallIndirectRemoveOperandAt = CallIndirectRemoveOperandAt


def CallIndirectIsReturn(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether the specified `call_indirect` expression is a tail call. """
    return lib.BinaryenCallIndirectIsReturn(expr)


BinaryenCallIndirectIsReturn = CallIndirectIsReturn


def CallIndirectSetReturn(
    expr: BinaryenExpressionRef,
    is_return: bool,
) -> None:
    """ Sets whether the specified `call_indirect` expression is a tail call. """
    lib.BinaryenCallIndirectSetReturn(expr, is_return)


BinaryenCallIndirectSetReturn = CallIndirectSetReturn


def CallIndirectGetParams(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the parameter types of the specified `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetParams(expr)


BinaryenCallIndirectGetParams = CallIndirectGetParams


def CallIndirectSetParams(
    expr: BinaryenExpressionRef,
    params: BinaryenType,
) -> None:
    """ Sets the parameter types of the specified `call_indirect` expression. """
    lib.BinaryenCallIndirectSetParams(expr, params)


BinaryenCallIndirectSetParams = CallIndirectSetParams


def CallIndirectGetResults(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the result types of the specified `call_indirect` expression. """
    return lib.BinaryenCallIndirectGetResults(expr)


BinaryenCallIndirectGetResults = CallIndirectGetResults


def CallIndirectSetResults(
    expr: BinaryenExpressionRef,
    params: BinaryenType,
) -> None:
    """ Sets the result types of the specified `call_indirect` expression. """
    lib.BinaryenCallIndirectSetResults(expr, params)


BinaryenCallIndirectSetResults = CallIndirectSetResults


def LocalGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the local index of a `local.get` expression. """
    return lib.BinaryenLocalGetGetIndex(expr)


BinaryenLocalGetGetIndex = LocalGetGetIndex


def LocalGetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    """ Sets the local index of a `local.get` expression. """
    lib.BinaryenLocalGetSetIndex(expr, index)


BinaryenLocalGetSetIndex = LocalGetSetIndex


def LocalSetIsTee(
    expr: BinaryenExpressionRef,
) -> bool:
    """
    Gets whether a `local.set` tees its value (is a `local.tee`). True if the
    expression has a type other than `none`.
    """
    return lib.BinaryenLocalSetIsTee(expr)


BinaryenLocalSetIsTee = LocalSetIsTee


def LocalSetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the local index of a `local.set` or `local.tee` expression. """
    return lib.BinaryenLocalSetGetIndex(expr)


BinaryenLocalSetGetIndex = LocalSetGetIndex


def LocalSetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    """ Sets the local index of a `local.set` or `local.tee` expression. """
    lib.BinaryenLocalSetSetIndex(expr, index)


BinaryenLocalSetSetIndex = LocalSetSetIndex


def LocalSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `local.set` or `local.tee` expression. """
    return lib.BinaryenLocalSetGetValue(expr)


BinaryenLocalSetGetValue = LocalSetGetValue


def LocalSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `local.set` or `local.tee` expression. """
    lib.BinaryenLocalSetSetValue(expr, value_expr)


BinaryenLocalSetSetValue = LocalSetSetValue


def GlobalGetGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the global being accessed by a `global.get` expression. """
    return _dec(lib.BinaryenGlobalGetGetName(expr))


BinaryenGlobalGetGetName = GlobalGetGetName


def GlobalGetSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name of the global being accessed by a `global.get` expression. """
    lib.BinaryenGlobalGetSetName(expr, _enc(name))


BinaryenGlobalGetSetName = GlobalGetSetName


def GlobalSetGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the global being accessed by a `global.set` expression. """
    return _dec(lib.BinaryenGlobalSetGetName(expr))


BinaryenGlobalSetGetName = GlobalSetGetName


def GlobalSetSetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name of the global being accessed by a `global.set` expression. """
    lib.BinaryenGlobalSetSetName(expr, _enc(name))


BinaryenGlobalSetSetName = GlobalSetSetName


def GlobalSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `global.set` expression. """
    return lib.BinaryenGlobalSetGetValue(expr)


BinaryenGlobalSetGetValue = GlobalSetGetValue


def GlobalSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `global.set` expression. """
    lib.BinaryenGlobalSetSetValue(expr, value_expr)


BinaryenGlobalSetSetValue = GlobalSetSetValue


def TableGetGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the table being accessed by a `table.get` expression. """
    return _dec(lib.BinaryenTableGetGetTable(expr))


BinaryenTableGetGetTable = TableGetGetTable


def TableGetSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.get` expression. """
    lib.BinaryenTableGetSetTable(expr, _enc(table))


BinaryenTableGetSetTable = TableGetSetTable


def TableGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the index expression of a `table.get` expression. """
    return lib.BinaryenTableGetGetIndex(expr)


BinaryenTableGetGetIndex = TableGetGetIndex


def TableGetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the index expression of a `table.get` expression. """
    lib.BinaryenTableGetSetIndex(expr, index_expr)


BinaryenTableGetSetIndex = TableGetSetIndex


def TableSetGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the table being accessed by a `table.set` expression. """
    return _dec(lib.BinaryenTableSetGetTable(expr))


BinaryenTableSetGetTable = TableSetGetTable


def TableSetSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.set` expression. """
    lib.BinaryenTableSetSetTable(expr, _enc(table))


BinaryenTableSetSetTable = TableSetSetTable


def TableSetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the index expression of a `table.set` expression. """
    return lib.BinaryenTableSetGetIndex(expr)


BinaryenTableSetGetIndex = TableSetGetIndex


def TableSetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the index expression of a `table.set` expression. """
    lib.BinaryenTableSetSetIndex(expr, index_expr)


BinaryenTableSetSetIndex = TableSetSetIndex


def TableSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `table.set` expression. """
    return lib.BinaryenTableSetGetValue(expr)


BinaryenTableSetGetValue = TableSetGetValue


def TableSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `table.set` expression. """
    lib.BinaryenTableSetSetValue(expr, value_expr)


BinaryenTableSetSetValue = TableSetSetValue


def TableSizeGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the table being accessed by a `table.size` expression. """
    return _dec(lib.BinaryenTableSizeGetTable(expr))


BinaryenTableSizeGetTable = TableSizeGetTable


def TableSizeSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.size` expression. """
    lib.BinaryenTableSizeSetTable(expr, _enc(table))


BinaryenTableSizeSetTable = TableSizeSetTable


def TableGrowGetTable(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the table being accessed by a `table.grow` expression. """
    return _dec(lib.BinaryenTableGrowGetTable(expr))


BinaryenTableGrowGetTable = TableGrowGetTable


def TableGrowSetTable(
    expr: BinaryenExpressionRef,
    table: str,
) -> None:
    """ Sets the name of the table being accessed by a `table.grow` expression. """
    lib.BinaryenTableGrowSetTable(expr, _enc(table))


BinaryenTableGrowSetTable = TableGrowSetTable


def TableGrowGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `table.grow` expression. """
    return lib.BinaryenTableGrowGetValue(expr)


BinaryenTableGrowGetValue = TableGrowGetValue


def TableGrowSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `table.grow` expression. """
    lib.BinaryenTableGrowSetValue(expr, value_expr)


BinaryenTableGrowSetValue = TableGrowSetValue


def TableGrowGetDelta(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the delta of a `table.grow` expression. """
    return lib.BinaryenTableGrowGetDelta(expr)


BinaryenTableGrowGetDelta = TableGrowGetDelta


def TableGrowSetDelta(
    expr: BinaryenExpressionRef,
    delta_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the delta of a `table.grow` expression. """
    lib.BinaryenTableGrowSetDelta(expr, delta_expr)


BinaryenTableGrowSetDelta = TableGrowSetDelta


def MemoryGrowGetDelta(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the delta of a `memory.grow` expression. """
    return lib.BinaryenMemoryGrowGetDelta(expr)


BinaryenMemoryGrowGetDelta = MemoryGrowGetDelta


def MemoryGrowSetDelta(
    expr: BinaryenExpressionRef,
    delta_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the delta of a `memory.grow` expression. """
    lib.BinaryenMemoryGrowSetDelta(expr, delta_expr)


BinaryenMemoryGrowSetDelta = MemoryGrowSetDelta


def LoadIsAtomic(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `load` expression is atomic (is an `atomic.load`). """
    return lib.BinaryenLoadIsAtomic(expr)


BinaryenLoadIsAtomic = LoadIsAtomic


def LoadSetAtomic(
    expr: BinaryenExpressionRef,
    is_atomic: bool,
) -> None:
    """ Sets whether a `load` expression is atomic (is an `atomic.load`). """
    lib.BinaryenLoadSetAtomic(expr, is_atomic)


BinaryenLoadSetAtomic = LoadSetAtomic


def LoadIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `load` expression operates on a signed value (`_s`). """
    return lib.BinaryenLoadIsSigned(expr)


BinaryenLoadIsSigned = LoadIsSigned


def LoadSetSigned(
    expr: BinaryenExpressionRef,
    is_signed: bool,
) -> None:
    """ Sets whether a `load` expression operates on a signed value (`_s`). """
    lib.BinaryenLoadSetSigned(expr, is_signed)


BinaryenLoadSetSigned = LoadSetSigned


def LoadGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a `load` expression. """
    return lib.BinaryenLoadGetOffset(expr)


BinaryenLoadGetOffset = LoadGetOffset


def LoadSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a `load` expression. """
    lib.BinaryenLoadSetOffset(expr, offset)


BinaryenLoadSetOffset = LoadSetOffset


def LoadGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the number of bytes loaded by a `load` expression. """
    return lib.BinaryenLoadGetBytes(expr)


BinaryenLoadGetBytes = LoadGetBytes


def LoadSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """ Sets the number of bytes loaded by a `load` expression. """
    lib.BinaryenLoadSetBytes(expr, _bytes)


BinaryenLoadSetBytes = LoadSetBytes


def LoadGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a `load` expression. """
    return lib.BinaryenLoadGetAlign(expr)


BinaryenLoadGetAlign = LoadGetAlign


def LoadSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a `load` expression. """
    lib.BinaryenLoadSetAlign(expr, align)


BinaryenLoadSetAlign = LoadSetAlign


def LoadGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a `load` expression. """
    return lib.BinaryenLoadGetPtr(expr)


BinaryenLoadGetPtr = LoadGetPtr


def LoadSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a `load` expression. """
    lib.BinaryenLoadSetPtr(expr, ptr_expr)


BinaryenLoadSetPtr = LoadSetPtr


def StoreIsAtomic(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `store` expression is atomic (is an `atomic.store`). """
    return lib.BinaryenStoreIsAtomic(expr)


BinaryenStoreIsAtomic = StoreIsAtomic


def StoreSetAtomic(
    expr: BinaryenExpressionRef,
    is_atomic: bool,
) -> None:
    """ Sets whether a `store` expression is atomic (is an `atomic.store`). """
    lib.BinaryenStoreSetAtomic(expr, is_atomic)


BinaryenStoreSetAtomic = StoreSetAtomic


def StoreGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the number of bytes stored by a `store` expression. """
    return lib.BinaryenStoreGetBytes(expr)


BinaryenStoreGetBytes = StoreGetBytes


def StoreSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """ Sets the number of bytes stored by a `store` expression. """
    lib.BinaryenStoreSetBytes(expr, _bytes)


BinaryenStoreSetBytes = StoreSetBytes


def StoreGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a `store` expression. """
    return lib.BinaryenStoreGetOffset(expr)


BinaryenStoreGetOffset = StoreGetOffset


def StoreSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a `store` expression. """
    lib.BinaryenStoreSetOffset(expr, offset)


BinaryenStoreSetOffset = StoreSetOffset


def StoreGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a `store` expression. """
    return lib.BinaryenStoreGetAlign(expr)


BinaryenStoreGetAlign = StoreGetAlign


def StoreSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a `store` expression. """
    lib.BinaryenStoreSetAlign(expr, align)


BinaryenStoreSetAlign = StoreSetAlign


def StoreGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a `store` expression. """
    return lib.BinaryenStoreGetPtr(expr)


BinaryenStoreGetPtr = StoreGetPtr


def StoreSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a `store` expression. """
    lib.BinaryenStoreSetPtr(expr, ptr_expr)


BinaryenStoreSetPtr = StoreSetPtr


def StoreGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `store` expression. """
    return lib.BinaryenStoreGetValue(expr)


BinaryenStoreGetValue = StoreGetValue


def StoreSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `store` expression. """
    lib.BinaryenStoreSetValue(expr, value_expr)


BinaryenStoreSetValue = StoreSetValue


def StoreGetValueType(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the value type of a `store` expression. """
    return lib.BinaryenStoreGetValueType(expr)


BinaryenStoreGetValueType = StoreGetValueType


def StoreSetValueType(
    expr: BinaryenExpressionRef,
    value_type: BinaryenType,
) -> None:
    """ Sets the value type of a `store` expression. """
    lib.BinaryenStoreSetValueType(expr, value_type)


BinaryenStoreSetValueType = StoreSetValueType


def ConstGetValueI32(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the 32-bit integer value of an `i32.const` expression. """
    return lib.BinaryenConstGetValueI32(expr)


BinaryenConstGetValueI32 = ConstGetValueI32


def ConstSetValueI32(
    expr: BinaryenExpressionRef,
    value: int,
) -> None:
    """ Sets the 32-bit integer value of an `i32.const` expression. """
    lib.BinaryenConstSetValueI32(expr, value)


BinaryenConstSetValueI32 = ConstSetValueI32


def ConstGetValueI64(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the 64-bit integer value of an `i64.const` expression. """
    return lib.BinaryenConstGetValueI64(expr)


BinaryenConstGetValueI64 = ConstGetValueI64


def ConstSetValueI64(
    expr: BinaryenExpressionRef,
    value: int,
) -> None:
    """ Sets the 64-bit integer value of an `i64.const` expression. """
    lib.BinaryenConstSetValueI64(expr, value)


BinaryenConstSetValueI64 = ConstSetValueI64


def ConstGetValueI64Low(
    expr: BinaryenExpressionRef,
) -> int:
    """
    Gets the low 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    return lib.BinaryenConstGetValueI64Low(expr)


BinaryenConstGetValueI64Low = ConstGetValueI64Low


def ConstSetValueI64Low(
    expr: BinaryenExpressionRef,
    value_low: int,
) -> None:
    """
    Sets the low 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    lib.BinaryenConstSetValueI64Low(expr, value_low)


BinaryenConstSetValueI64Low = ConstSetValueI64Low


def ConstGetValueI64High(
    expr: BinaryenExpressionRef,
) -> int:
    """
    Gets the high 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    return lib.BinaryenConstGetValueI64High(expr)


BinaryenConstGetValueI64High = ConstGetValueI64High


def ConstSetValueI64High(
    expr: BinaryenExpressionRef,
    value_high: int,
) -> None:
    """
    Sets the high 32-bits of the 64-bit integer value of an `i64.const`
    expression.
    """
    lib.BinaryenConstSetValueI64High(expr, value_high)


BinaryenConstSetValueI64High = ConstSetValueI64High


def ConstGetValueF32(
    expr: BinaryenExpressionRef,
) -> float:
    """ Gets the 32-bit float value of a `f32.const` expression. """
    return lib.BinaryenConstGetValueF32(expr)


BinaryenConstGetValueF32 = ConstGetValueF32


def ConstSetValueF32(
    expr: BinaryenExpressionRef,
    value: float,
) -> None:
    """ Sets the 32-bit float value of a `f32.const` expression. """
    lib.BinaryenConstSetValueF32(expr, value)


BinaryenConstSetValueF32 = ConstSetValueF32


def ConstGetValueF64(
    expr: BinaryenExpressionRef,
) -> float:
    """ Gets the 64-bit float (double) value of a `f64.const` expression. """
    return lib.BinaryenConstGetValueF64(expr)


BinaryenConstGetValueF64 = ConstGetValueF64


def ConstSetValueF64(
    expr: BinaryenExpressionRef,
    value: float,
) -> None:
    """ Sets the 64-bit float (double) value of a `f64.const` expression. """
    lib.BinaryenConstSetValueF64(expr, value)


BinaryenConstSetValueF64 = ConstSetValueF64


def ConstGetValueV128(
    expr: BinaryenExpressionRef,
    out: List[int],
) -> None:
    """ Reads the 128-bit vector value of a `v128.const` expression. """
    lib.BinaryenConstGetValueV128(expr, out)


BinaryenConstGetValueV128 = ConstGetValueV128


def ConstSetValueV128(
    expr: BinaryenExpressionRef,
    value: List[int],
) -> None:
    """ Sets the 128-bit vector value of a `v128.const` expression. """
    lib.BinaryenConstSetValueV128(expr, value)


BinaryenConstSetValueV128 = ConstSetValueV128


def UnaryGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a unary expression. """
    return lib.BinaryenUnaryGetOp(expr)


BinaryenUnaryGetOp = UnaryGetOp


def UnarySetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a unary expression. """
    lib.BinaryenUnarySetOp(expr, op)


BinaryenUnarySetOp = UnarySetOp


def UnaryGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a unary expression. """
    return lib.BinaryenUnaryGetValue(expr)


BinaryenUnaryGetValue = UnaryGetValue


def UnarySetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a unary expression. """
    lib.BinaryenUnarySetValue(expr, value_expr)


BinaryenUnarySetValue = UnarySetValue


def BinaryGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a binary expression. """
    return lib.BinaryenBinaryGetOp(expr)


BinaryenBinaryGetOp = BinaryGetOp


def BinarySetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a binary expression. """
    lib.BinaryenBinarySetOp(expr, op)


BinaryenBinarySetOp = BinarySetOp


def BinaryGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the left expression of a binary expression. """
    return lib.BinaryenBinaryGetLeft(expr)


BinaryenBinaryGetLeft = BinaryGetLeft


def BinarySetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the left expression of a binary expression. """
    lib.BinaryenBinarySetLeft(expr, left_expr)


BinaryenBinarySetLeft = BinarySetLeft


def BinaryGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the right expression of a binary expression. """
    return lib.BinaryenBinaryGetRight(expr)


BinaryenBinaryGetRight = BinaryGetRight


def BinarySetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the right expression of a binary expression. """
    lib.BinaryenBinarySetRight(expr, right_expr)


BinaryenBinarySetRight = BinarySetRight


def SelectGetIfTrue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the expression becoming selected by a `select` expression if the
    condition turns out true.
    """
    return lib.BinaryenSelectGetIfTrue(expr)


BinaryenSelectGetIfTrue = SelectGetIfTrue


def SelectSetIfTrue(
    expr: BinaryenExpressionRef,
    if_true_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression becoming selected by a `select` expression if the
    condition turns out true.
    """
    lib.BinaryenSelectSetIfTrue(expr, if_true_expr)


BinaryenSelectSetIfTrue = SelectSetIfTrue


def SelectGetIfFalse(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the expression becoming selected by a `select` expression if the
    condition turns out false.
    """
    return lib.BinaryenSelectGetIfFalse(expr)


BinaryenSelectGetIfFalse = SelectGetIfFalse


def SelectSetIfFalse(
    expr: BinaryenExpressionRef,
    if_false_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression becoming selected by a `select` expression if the
    condition turns out false.
    """
    lib.BinaryenSelectSetIfFalse(expr, if_false_expr)


BinaryenSelectSetIfFalse = SelectSetIfFalse


def SelectGetCondition(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the condition expression of a `select` expression. """
    return lib.BinaryenSelectGetCondition(expr)


BinaryenSelectGetCondition = SelectGetCondition


def SelectSetCondition(
    expr: BinaryenExpressionRef,
    cond_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the condition expression of a `select` expression. """
    lib.BinaryenSelectSetCondition(expr, cond_expr)


BinaryenSelectSetCondition = SelectSetCondition


def DropGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression being dropped by a `drop` expression. """
    return lib.BinaryenDropGetValue(expr)


BinaryenDropGetValue = DropGetValue


def DropSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression being dropped by a `drop` expression. """
    lib.BinaryenDropSetValue(expr, value_expr)


BinaryenDropSetValue = DropSetValue


def ReturnGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression, if any, being returned by a `return` expression. """
    return lib.BinaryenReturnGetValue(expr)


BinaryenReturnGetValue = ReturnGetValue


def ReturnSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression, if any, being returned by a `return` expression. """
    lib.BinaryenReturnSetValue(expr, value_expr)


BinaryenReturnSetValue = ReturnSetValue


def AtomicRMWGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetOp(expr)


BinaryenAtomicRMWGetOp = AtomicRMWGetOp


def AtomicRMWSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetOp(expr, op)


BinaryenAtomicRMWSetOp = AtomicRMWSetOp


def AtomicRMWGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the number of bytes affected by an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetBytes(expr)


BinaryenAtomicRMWGetBytes = AtomicRMWGetBytes


def AtomicRMWSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """ Sets the number of bytes affected by an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetBytes(expr, _bytes)


BinaryenAtomicRMWSetBytes = AtomicRMWSetBytes


def AtomicRMWGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetOffset(expr)


BinaryenAtomicRMWGetOffset = AtomicRMWGetOffset


def AtomicRMWSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetOffset(expr, offset)


BinaryenAtomicRMWSetOffset = AtomicRMWSetOffset


def AtomicRMWGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetPtr(expr)


BinaryenAtomicRMWGetPtr = AtomicRMWGetPtr


def AtomicRMWSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetPtr(expr, ptr_expr)


BinaryenAtomicRMWSetPtr = AtomicRMWSetPtr


def AtomicRMWGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of an atomic read-modify-write expression. """
    return lib.BinaryenAtomicRMWGetValue(expr)


BinaryenAtomicRMWGetValue = AtomicRMWGetValue


def AtomicRMWSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of an atomic read-modify-write expression. """
    lib.BinaryenAtomicRMWSetValue(expr, value_expr)


BinaryenAtomicRMWSetValue = AtomicRMWSetValue


def AtomicCmpxchgGetBytes(
    expr: BinaryenExpressionRef,
) -> int:
    """
    Gets the number of bytes affected by an atomic compare and exchange
    expression.
    """
    return lib.BinaryenAtomicCmpxchgGetBytes(expr)


BinaryenAtomicCmpxchgGetBytes = AtomicCmpxchgGetBytes


def AtomicCmpxchgSetBytes(
    expr: BinaryenExpressionRef,
    _bytes: int,
) -> None:
    """
    Sets the number of bytes affected by an atomic compare and exchange
    expression.
    """
    lib.BinaryenAtomicCmpxchgSetBytes(expr, _bytes)


BinaryenAtomicCmpxchgSetBytes = AtomicCmpxchgSetBytes


def AtomicCmpxchgGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of an atomic compare and exchange expression. """
    return lib.BinaryenAtomicCmpxchgGetOffset(expr)


BinaryenAtomicCmpxchgGetOffset = AtomicCmpxchgGetOffset


def AtomicCmpxchgSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of an atomic compare and exchange expression. """
    lib.BinaryenAtomicCmpxchgSetOffset(expr, offset)


BinaryenAtomicCmpxchgSetOffset = AtomicCmpxchgSetOffset


def AtomicCmpxchgGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of an atomic compare and exchange expression. """
    return lib.BinaryenAtomicCmpxchgGetPtr(expr)


BinaryenAtomicCmpxchgGetPtr = AtomicCmpxchgGetPtr


def AtomicCmpxchgSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an atomic compare and exchange expression. """
    lib.BinaryenAtomicCmpxchgSetPtr(expr, ptr_expr)


BinaryenAtomicCmpxchgSetPtr = AtomicCmpxchgSetPtr


def AtomicCmpxchgGetExpected(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the expression representing the expected value of an atomic compare and
    exchange expression.
    """
    return lib.BinaryenAtomicCmpxchgGetExpected(expr)


BinaryenAtomicCmpxchgGetExpected = AtomicCmpxchgGetExpected


def AtomicCmpxchgSetExpected(
    expr: BinaryenExpressionRef,
    expected_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression representing the expected value of an atomic compare and
    exchange expression.
    """
    lib.BinaryenAtomicCmpxchgSetExpected(expr, expected_expr)


BinaryenAtomicCmpxchgSetExpected = AtomicCmpxchgSetExpected


def AtomicCmpxchgGetReplacement(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the replacement expression of an atomic compare and exchange expression. """
    return lib.BinaryenAtomicCmpxchgGetReplacement(expr)


BinaryenAtomicCmpxchgGetReplacement = AtomicCmpxchgGetReplacement


def AtomicCmpxchgSetReplacement(
    expr: BinaryenExpressionRef,
    replacement_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the replacement expression of an atomic compare and exchange expression. """
    lib.BinaryenAtomicCmpxchgSetReplacement(expr, replacement_expr)


BinaryenAtomicCmpxchgSetReplacement = AtomicCmpxchgSetReplacement


def AtomicWaitGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of an `memory.atomic.wait` expression. """
    return lib.BinaryenAtomicWaitGetPtr(expr)


BinaryenAtomicWaitGetPtr = AtomicWaitGetPtr


def AtomicWaitSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an `memory.atomic.wait` expression. """
    lib.BinaryenAtomicWaitSetPtr(expr, ptr_expr)


BinaryenAtomicWaitSetPtr = AtomicWaitSetPtr


def AtomicWaitGetExpected(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the expression representing the expected value of an
    `memory.atomic.wait` expression.
    """
    return lib.BinaryenAtomicWaitGetExpected(expr)


BinaryenAtomicWaitGetExpected = AtomicWaitGetExpected


def AtomicWaitSetExpected(
    expr: BinaryenExpressionRef,
    expected_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the expression representing the expected value of an
    `memory.atomic.wait` expression.
    """
    lib.BinaryenAtomicWaitSetExpected(expr, expected_expr)


BinaryenAtomicWaitSetExpected = AtomicWaitSetExpected


def AtomicWaitGetTimeout(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the timeout expression of an `memory.atomic.wait` expression. """
    return lib.BinaryenAtomicWaitGetTimeout(expr)


BinaryenAtomicWaitGetTimeout = AtomicWaitGetTimeout


def AtomicWaitSetTimeout(
    expr: BinaryenExpressionRef,
    timeout_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the timeout expression of an `memory.atomic.wait` expression. """
    lib.BinaryenAtomicWaitSetTimeout(expr, timeout_expr)


BinaryenAtomicWaitSetTimeout = AtomicWaitSetTimeout


def AtomicWaitGetExpectedType(
    expr: BinaryenExpressionRef,
) -> BinaryenType:
    """ Gets the expected type of an `memory.atomic.wait` expression. """
    return lib.BinaryenAtomicWaitGetExpectedType(expr)


BinaryenAtomicWaitGetExpectedType = AtomicWaitGetExpectedType


def AtomicWaitSetExpectedType(
    expr: BinaryenExpressionRef,
    expected_type: BinaryenType,
) -> None:
    """ Sets the expected type of an `memory.atomic.wait` expression. """
    lib.BinaryenAtomicWaitSetExpectedType(expr, expected_type)


BinaryenAtomicWaitSetExpectedType = AtomicWaitSetExpectedType


def AtomicNotifyGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of an `memory.atomic.notify` expression. """
    return lib.BinaryenAtomicNotifyGetPtr(expr)


BinaryenAtomicNotifyGetPtr = AtomicNotifyGetPtr


def AtomicNotifySetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of an `memory.atomic.notify` expression. """
    lib.BinaryenAtomicNotifySetPtr(expr, ptr_expr)


BinaryenAtomicNotifySetPtr = AtomicNotifySetPtr


def AtomicNotifyGetNotifyCount(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the notify count expression of an `memory.atomic.notify` expression. """
    return lib.BinaryenAtomicNotifyGetNotifyCount(expr)


BinaryenAtomicNotifyGetNotifyCount = AtomicNotifyGetNotifyCount


def AtomicNotifySetNotifyCount(
    expr: BinaryenExpressionRef,
    notify_count_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the notify count expression of an `memory.atomic.notify` expression. """
    lib.BinaryenAtomicNotifySetNotifyCount(expr, notify_count_expr)


BinaryenAtomicNotifySetNotifyCount = AtomicNotifySetNotifyCount


def AtomicFenceGetOrder(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the order of an `atomic.fence` expression. """
    return lib.BinaryenAtomicFenceGetOrder(expr)


BinaryenAtomicFenceGetOrder = AtomicFenceGetOrder


def AtomicFenceSetOrder(
    expr: BinaryenExpressionRef,
    order: int,
) -> None:
    """ Sets the order of an `atomic.fence` expression. """
    lib.BinaryenAtomicFenceSetOrder(expr, order)


BinaryenAtomicFenceSetOrder = AtomicFenceSetOrder


def SIMDExtractGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a SIMD extract expression. """
    return lib.BinaryenSIMDExtractGetOp(expr)


BinaryenSIMDExtractGetOp = SIMDExtractGetOp


def SIMDExtractSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD extract expression. """
    lib.BinaryenSIMDExtractSetOp(expr, op)


BinaryenSIMDExtractSetOp = SIMDExtractSetOp


def SIMDExtractGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the vector expression a SIMD extract expression extracts from. """
    return lib.BinaryenSIMDExtractGetVec(expr)


BinaryenSIMDExtractGetVec = SIMDExtractGetVec


def SIMDExtractSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the vector expression a SIMD extract expression extracts from. """
    lib.BinaryenSIMDExtractSetVec(expr, vec_expr)


BinaryenSIMDExtractSetVec = SIMDExtractSetVec


def SIMDExtractGetIndex(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the index of the extracted lane of a SIMD extract expression. """
    return lib.BinaryenSIMDExtractGetIndex(expr)


BinaryenSIMDExtractGetIndex = SIMDExtractGetIndex


def SIMDExtractSetIndex(
    expr: BinaryenExpressionRef,
    index: int,
) -> None:
    """ Sets the index of the extracted lane of a SIMD extract expression. """
    lib.BinaryenSIMDExtractSetIndex(expr, index)


BinaryenSIMDExtractSetIndex = SIMDExtractSetIndex


def SIMDReplaceGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a SIMD replace expression. """
    return lib.BinaryenSIMDReplaceGetOp(expr)


BinaryenSIMDReplaceGetOp = SIMDReplaceGetOp


def SIMDReplaceSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD replace expression. """
    lib.BinaryenSIMDReplaceSetOp(expr, op)


BinaryenSIMDReplaceSetOp = SIMDReplaceSetOp


def SIMDReplaceGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the vector expression a SIMD replace expression replaces in. """
    return lib.BinaryenSIMDReplaceGetVec(expr)


BinaryenSIMDReplaceGetVec = SIMDReplaceGetVec


def SIMDReplaceSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the vector expression a SIMD replace expression replaces in. """
    lib.BinaryenSIMDReplaceSetVec(expr, vec_expr)


BinaryenSIMDReplaceSetVec = SIMDReplaceSetVec


def SIMDReplaceGetIndex(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the index of the replaced lane of a SIMD replace expression. """
    return lib.BinaryenSIMDReplaceGetIndex(expr)


BinaryenSIMDReplaceGetIndex = SIMDReplaceGetIndex


def SIMDReplaceSetIndex(
    expr: BinaryenExpressionRef,
    index: int,
) -> None:
    """ Sets the index of the replaced lane of a SIMD replace expression. """
    lib.BinaryenSIMDReplaceSetIndex(expr, index)


BinaryenSIMDReplaceSetIndex = SIMDReplaceSetIndex


def SIMDReplaceGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression a SIMD replace expression replaces with. """
    return lib.BinaryenSIMDReplaceGetValue(expr)


BinaryenSIMDReplaceGetValue = SIMDReplaceGetValue


def SIMDReplaceSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression a SIMD replace expression replaces with. """
    lib.BinaryenSIMDReplaceSetValue(expr, value_expr)


BinaryenSIMDReplaceSetValue = SIMDReplaceSetValue


def SIMDShuffleGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the left expression of a SIMD shuffle expression. """
    return lib.BinaryenSIMDShuffleGetLeft(expr)


BinaryenSIMDShuffleGetLeft = SIMDShuffleGetLeft


def SIMDShuffleSetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the left expression of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleSetLeft(expr, left_expr)


BinaryenSIMDShuffleSetLeft = SIMDShuffleSetLeft


def SIMDShuffleGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the right expression of a SIMD shuffle expression. """
    return lib.BinaryenSIMDShuffleGetRight(expr)


BinaryenSIMDShuffleGetRight = SIMDShuffleGetRight


def SIMDShuffleSetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the right expression of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleSetRight(expr, right_expr)


BinaryenSIMDShuffleSetRight = SIMDShuffleSetRight


def SIMDShuffleGetMask(
    expr: BinaryenExpressionRef,
    mask: List[int],
) -> None:
    """ Gets the 128-bit mask of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleGetMask(expr, mask)


BinaryenSIMDShuffleGetMask = SIMDShuffleGetMask


def SIMDShuffleSetMask(
    expr: BinaryenExpressionRef,
    mask: List[int],
) -> None:
    """ Sets the 128-bit mask of a SIMD shuffle expression. """
    lib.BinaryenSIMDShuffleSetMask(expr, mask)


BinaryenSIMDShuffleSetMask = SIMDShuffleSetMask


def SIMDTernaryGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a SIMD ternary expression. """
    return lib.BinaryenSIMDTernaryGetOp(expr)


BinaryenSIMDTernaryGetOp = SIMDTernaryGetOp


def SIMDTernarySetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetOp(expr, op)


BinaryenSIMDTernarySetOp = SIMDTernarySetOp


def SIMDTernaryGetA(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the first operand expression of a SIMD ternary expression. """
    return lib.BinaryenSIMDTernaryGetA(expr)


BinaryenSIMDTernaryGetA = SIMDTernaryGetA


def SIMDTernarySetA(
    expr: BinaryenExpressionRef,
    a_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the first operand expression of a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetA(expr, a_expr)


BinaryenSIMDTernarySetA = SIMDTernarySetA


def SIMDTernaryGetB(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the second operand expression of a SIMD ternary expression. """
    return lib.BinaryenSIMDTernaryGetB(expr)


BinaryenSIMDTernaryGetB = SIMDTernaryGetB


def SIMDTernarySetB(
    expr: BinaryenExpressionRef,
    b_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the second operand expression of a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetB(expr, b_expr)


BinaryenSIMDTernarySetB = SIMDTernarySetB


def SIMDTernaryGetC(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the third operand expression of a SIMD ternary expression. """
    return lib.BinaryenSIMDTernaryGetC(expr)


BinaryenSIMDTernaryGetC = SIMDTernaryGetC


def SIMDTernarySetC(
    expr: BinaryenExpressionRef,
    c_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the third operand expression of a SIMD ternary expression. """
    lib.BinaryenSIMDTernarySetC(expr, c_expr)


BinaryenSIMDTernarySetC = SIMDTernarySetC


def SIMDShiftGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a SIMD shift expression. """
    return lib.BinaryenSIMDShiftGetOp(expr)


BinaryenSIMDShiftGetOp = SIMDShiftGetOp


def SIMDShiftSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD shift expression. """
    lib.BinaryenSIMDShiftSetOp(expr, op)


BinaryenSIMDShiftSetOp = SIMDShiftSetOp


def SIMDShiftGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the expression being shifted by a SIMD shift expression. """
    return lib.BinaryenSIMDShiftGetVec(expr)


BinaryenSIMDShiftGetVec = SIMDShiftGetVec


def SIMDShiftSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the expression being shifted by a SIMD shift expression. """
    lib.BinaryenSIMDShiftSetVec(expr, vec_expr)


BinaryenSIMDShiftSetVec = SIMDShiftSetVec


def SIMDShiftGetShift(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the expression representing the shift of a SIMD shift expression. """
    return lib.BinaryenSIMDShiftGetShift(expr)


BinaryenSIMDShiftGetShift = SIMDShiftGetShift


def SIMDShiftSetShift(
    expr: BinaryenExpressionRef,
    shift_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the expression representing the shift of a SIMD shift expression. """
    lib.BinaryenSIMDShiftSetShift(expr, shift_expr)


BinaryenSIMDShiftSetShift = SIMDShiftSetShift


def SIMDLoadGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a SIMD load expression. """
    return lib.BinaryenSIMDLoadGetOp(expr)


BinaryenSIMDLoadGetOp = SIMDLoadGetOp


def SIMDLoadSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD load expression. """
    lib.BinaryenSIMDLoadSetOp(expr, op)


BinaryenSIMDLoadSetOp = SIMDLoadSetOp


def SIMDLoadGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a SIMD load expression. """
    return lib.BinaryenSIMDLoadGetOffset(expr)


BinaryenSIMDLoadGetOffset = SIMDLoadGetOffset


def SIMDLoadSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a SIMD load expression. """
    lib.BinaryenSIMDLoadSetOffset(expr, offset)


BinaryenSIMDLoadSetOffset = SIMDLoadSetOffset


def SIMDLoadGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a SIMD load expression. """
    return lib.BinaryenSIMDLoadGetAlign(expr)


BinaryenSIMDLoadGetAlign = SIMDLoadGetAlign


def SIMDLoadSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a SIMD load expression. """
    lib.BinaryenSIMDLoadSetAlign(expr, align)


BinaryenSIMDLoadSetAlign = SIMDLoadSetAlign


def SIMDLoadGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a SIMD load expression. """
    return lib.BinaryenSIMDLoadGetPtr(expr)


BinaryenSIMDLoadGetPtr = SIMDLoadGetPtr


def SIMDLoadSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a SIMD load expression. """
    lib.BinaryenSIMDLoadSetPtr(expr, ptr_expr)


BinaryenSIMDLoadSetPtr = SIMDLoadSetPtr


def SIMDLoadStoreLaneGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation being performed by a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetOp(expr)


BinaryenSIMDLoadStoreLaneGetOp = SIMDLoadStoreLaneGetOp


def SIMDLoadStoreLaneSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation being performed by a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetOp(expr, op)


BinaryenSIMDLoadStoreLaneSetOp = SIMDLoadStoreLaneSetOp


def SIMDLoadStoreLaneGetOffset(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the constant offset of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetOffset(expr)


BinaryenSIMDLoadStoreLaneGetOffset = SIMDLoadStoreLaneGetOffset


def SIMDLoadStoreLaneSetOffset(
    expr: BinaryenExpressionRef,
    offset: int,
) -> None:
    """ Sets the constant offset of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetOffset(expr, offset)


BinaryenSIMDLoadStoreLaneSetOffset = SIMDLoadStoreLaneSetOffset


def SIMDLoadStoreLaneGetAlign(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the byte alignment of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetAlign(expr)


BinaryenSIMDLoadStoreLaneGetAlign = SIMDLoadStoreLaneGetAlign


def SIMDLoadStoreLaneSetAlign(
    expr: BinaryenExpressionRef,
    align: int,
) -> None:
    """ Sets the byte alignment of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetAlign(expr, align)


BinaryenSIMDLoadStoreLaneSetAlign = SIMDLoadStoreLaneSetAlign


def SIMDLoadStoreLaneGetIndex(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the lane index of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetIndex(expr)


BinaryenSIMDLoadStoreLaneGetIndex = SIMDLoadStoreLaneGetIndex


def SIMDLoadStoreLaneSetIndex(
    expr: BinaryenExpressionRef,
    index: int,
) -> None:
    """ Sets the lane index of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetIndex(expr, index)


BinaryenSIMDLoadStoreLaneSetIndex = SIMDLoadStoreLaneSetIndex


def SIMDLoadStoreLaneGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the pointer expression of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetPtr(expr)


BinaryenSIMDLoadStoreLaneGetPtr = SIMDLoadStoreLaneGetPtr


def SIMDLoadStoreLaneSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the pointer expression of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetPtr(expr, ptr_expr)


BinaryenSIMDLoadStoreLaneSetPtr = SIMDLoadStoreLaneSetPtr


def SIMDLoadStoreLaneGetVec(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the vector expression of a SIMD load/store lane expression. """
    return lib.BinaryenSIMDLoadStoreLaneGetVec(expr)


BinaryenSIMDLoadStoreLaneGetVec = SIMDLoadStoreLaneGetVec


def SIMDLoadStoreLaneSetVec(
    expr: BinaryenExpressionRef,
    vec_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the vector expression of a SIMD load/store lane expression. """
    lib.BinaryenSIMDLoadStoreLaneSetVec(expr, vec_expr)


BinaryenSIMDLoadStoreLaneSetVec = SIMDLoadStoreLaneSetVec


def SIMDLoadStoreLaneIsStore(
    expr: BinaryenExpressionRef,
) -> bool:
    """
    Gets whether a SIMD load/store lane expression performs a store. Otherwise it
    performs a load.
    """
    return lib.BinaryenSIMDLoadStoreLaneIsStore(expr)


BinaryenSIMDLoadStoreLaneIsStore = SIMDLoadStoreLaneIsStore


def MemoryInitGetSegment(
    expr: BinaryenExpressionRef,
) -> int:
    """
    Gets the index of the segment being initialized by a `memory.init`
    expression.
    """
    return lib.BinaryenMemoryInitGetSegment(expr)


BinaryenMemoryInitGetSegment = MemoryInitGetSegment


def MemoryInitSetSegment(
    expr: BinaryenExpressionRef,
    segment_index: int,
) -> None:
    """
    Sets the index of the segment being initialized by a `memory.init`
    expression.
    """
    lib.BinaryenMemoryInitSetSegment(expr, segment_index)


BinaryenMemoryInitSetSegment = MemoryInitSetSegment


def MemoryInitGetDest(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the destination expression of a `memory.init` expression. """
    return lib.BinaryenMemoryInitGetDest(expr)


BinaryenMemoryInitGetDest = MemoryInitGetDest


def MemoryInitSetDest(
    expr: BinaryenExpressionRef,
    dest_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the destination expression of a `memory.init` expression. """
    lib.BinaryenMemoryInitSetDest(expr, dest_expr)


BinaryenMemoryInitSetDest = MemoryInitSetDest


def MemoryInitGetOffset(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the offset expression of a `memory.init` expression. """
    return lib.BinaryenMemoryInitGetOffset(expr)


BinaryenMemoryInitGetOffset = MemoryInitGetOffset


def MemoryInitSetOffset(
    expr: BinaryenExpressionRef,
    offset_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the offset expression of a `memory.init` expression. """
    lib.BinaryenMemoryInitSetOffset(expr, offset_expr)


BinaryenMemoryInitSetOffset = MemoryInitSetOffset


def MemoryInitGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the size expression of a `memory.init` expression. """
    return lib.BinaryenMemoryInitGetSize(expr)


BinaryenMemoryInitGetSize = MemoryInitGetSize


def MemoryInitSetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the size expression of a `memory.init` expression. """
    lib.BinaryenMemoryInitSetSize(expr, size_expr)


BinaryenMemoryInitSetSize = MemoryInitSetSize


def DataDropGetSegment(
    expr: BinaryenExpressionRef,
) -> int:
    """ Gets the index of the segment being dropped by a `data.drop` expression. """
    return lib.BinaryenDataDropGetSegment(expr)


BinaryenDataDropGetSegment = DataDropGetSegment


def DataDropSetSegment(
    expr: BinaryenExpressionRef,
    segment_index: int,
) -> None:
    """ Sets the index of the segment being dropped by a `data.drop` expression. """
    lib.BinaryenDataDropSetSegment(expr, segment_index)


BinaryenDataDropSetSegment = DataDropSetSegment


def MemoryCopyGetDest(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the destination expression of a `memory.copy` expression. """
    return lib.BinaryenMemoryCopyGetDest(expr)


BinaryenMemoryCopyGetDest = MemoryCopyGetDest


def MemoryCopySetDest(
    expr: BinaryenExpressionRef,
    dest_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the destination expression of a `memory.copy` expression. """
    lib.BinaryenMemoryCopySetDest(expr, dest_expr)


BinaryenMemoryCopySetDest = MemoryCopySetDest


def MemoryCopyGetSource(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the source expression of a `memory.copy` expression. """
    return lib.BinaryenMemoryCopyGetSource(expr)


BinaryenMemoryCopyGetSource = MemoryCopyGetSource


def MemoryCopySetSource(
    expr: BinaryenExpressionRef,
    source_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the source expression of a `memory.copy` expression. """
    lib.BinaryenMemoryCopySetSource(expr, source_expr)


BinaryenMemoryCopySetSource = MemoryCopySetSource


def MemoryCopyGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the size expression (number of bytes copied) of a `memory.copy`
    expression.
    """
    return lib.BinaryenMemoryCopyGetSize(expr)


BinaryenMemoryCopyGetSize = MemoryCopyGetSize


def MemoryCopySetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the size expression (number of bytes copied) of a `memory.copy`
    expression.
    """
    lib.BinaryenMemoryCopySetSize(expr, size_expr)


BinaryenMemoryCopySetSize = MemoryCopySetSize


def MemoryFillGetDest(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the destination expression of a `memory.fill` expression. """
    return lib.BinaryenMemoryFillGetDest(expr)


BinaryenMemoryFillGetDest = MemoryFillGetDest


def MemoryFillSetDest(
    expr: BinaryenExpressionRef,
    dest_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the destination expression of a `memory.fill` expression. """
    lib.BinaryenMemoryFillSetDest(expr, dest_expr)


BinaryenMemoryFillSetDest = MemoryFillSetDest


def MemoryFillGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of a `memory.fill` expression. """
    return lib.BinaryenMemoryFillGetValue(expr)


BinaryenMemoryFillGetValue = MemoryFillGetValue


def MemoryFillSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of a `memory.fill` expression. """
    lib.BinaryenMemoryFillSetValue(expr, value_expr)


BinaryenMemoryFillSetValue = MemoryFillSetValue


def MemoryFillGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Gets the size expression (number of bytes filled) of a `memory.fill`
    expression.
    """
    return lib.BinaryenMemoryFillGetSize(expr)


BinaryenMemoryFillGetSize = MemoryFillGetSize


def MemoryFillSetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    """
    Sets the size expression (number of bytes filled) of a `memory.fill`
    expression.
    """
    lib.BinaryenMemoryFillSetSize(expr, size_expr)


BinaryenMemoryFillSetSize = MemoryFillSetSize


def RefIsGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation performed by a `ref.is_*` expression. """
    return lib.BinaryenRefIsGetOp(expr)


BinaryenRefIsGetOp = RefIsGetOp


def RefIsSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation performed by a `ref.is_*` expression. """
    lib.BinaryenRefIsSetOp(expr, op)


BinaryenRefIsSetOp = RefIsSetOp


def RefIsGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression tested by a `ref.is_*` expression. """
    return lib.BinaryenRefIsGetValue(expr)


BinaryenRefIsGetValue = RefIsGetValue


def RefIsSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression tested by a `ref.is_*` expression. """
    lib.BinaryenRefIsSetValue(expr, value_expr)


BinaryenRefIsSetValue = RefIsSetValue


def RefAsGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    """ Gets the operation performed by a `ref.as_*` expression. """
    return lib.BinaryenRefAsGetOp(expr)


BinaryenRefAsGetOp = RefAsGetOp


def RefAsSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    """ Sets the operation performed by a `ref.as_*` expression. """
    lib.BinaryenRefAsSetOp(expr, op)


BinaryenRefAsSetOp = RefAsSetOp


def RefAsGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression tested by a `ref.as_*` expression. """
    return lib.BinaryenRefAsGetValue(expr)


BinaryenRefAsGetValue = RefAsGetValue


def RefAsSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression tested by a `ref.as_*` expression. """
    lib.BinaryenRefAsSetValue(expr, value_expr)


BinaryenRefAsSetValue = RefAsSetValue


def RefFuncGetFunc(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the function being wrapped by a `ref.func` expression. """
    return _dec(lib.BinaryenRefFuncGetFunc(expr))


BinaryenRefFuncGetFunc = RefFuncGetFunc


def RefFuncSetFunc(
    expr: BinaryenExpressionRef,
    func_name: str,
) -> None:
    """ Sets the name of the function being wrapped by a `ref.func` expression. """
    lib.BinaryenRefFuncSetFunc(expr, _enc(func_name))


BinaryenRefFuncSetFunc = RefFuncSetFunc


def RefEqGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the left expression of a `ref.eq` expression. """
    return lib.BinaryenRefEqGetLeft(expr)


BinaryenRefEqGetLeft = RefEqGetLeft


def RefEqSetLeft(
    expr: BinaryenExpressionRef,
    left: BinaryenExpressionRef,
) -> None:
    """ Sets the left expression of a `ref.eq` expression. """
    lib.BinaryenRefEqSetLeft(expr, left)


BinaryenRefEqSetLeft = RefEqSetLeft


def RefEqGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the right expression of a `ref.eq` expression. """
    return lib.BinaryenRefEqGetRight(expr)


BinaryenRefEqGetRight = RefEqGetRight


def RefEqSetRight(
    expr: BinaryenExpressionRef,
    right: BinaryenExpressionRef,
) -> None:
    """ Sets the right expression of a `ref.eq` expression. """
    lib.BinaryenRefEqSetRight(expr, right)


BinaryenRefEqSetRight = RefEqSetRight


def TryGetName(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name (label) of a `try` expression. """
    return _dec(lib.BinaryenTryGetName(expr))


BinaryenTryGetName = TryGetName


def TrySetName(
    expr: BinaryenExpressionRef,
    name: str,
) -> None:
    """ Sets the name (label) of a `try` expression. """
    lib.BinaryenTrySetName(expr, _enc(name))


BinaryenTrySetName = TrySetName


def TryGetBody(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the body expression of a `try` expression. """
    return lib.BinaryenTryGetBody(expr)


BinaryenTryGetBody = TryGetBody


def TrySetBody(
    expr: BinaryenExpressionRef,
    body_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the body expression of a `try` expression. """
    lib.BinaryenTrySetBody(expr, body_expr)


BinaryenTrySetBody = TrySetBody


def TryGetNumCatchTags(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Gets the number of catch blocks (= the number of catch tags) of a `try`
    expression.
    """
    return lib.BinaryenTryGetNumCatchTags(expr)


BinaryenTryGetNumCatchTags = TryGetNumCatchTags


def TryGetNumCatchBodies(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of catch/catch_all blocks of a `try` expression. """
    return lib.BinaryenTryGetNumCatchBodies(expr)


BinaryenTryGetNumCatchBodies = TryGetNumCatchBodies


def TryGetCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """ Gets the catch tag at the specified index of a `try` expression. """
    return _dec(lib.BinaryenTryGetCatchTagAt(expr, index))


BinaryenTryGetCatchTagAt = TryGetCatchTagAt


def TrySetCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_tag: str,
) -> None:
    """ Sets the catch tag at the specified index of a `try` expression. """
    lib.BinaryenTrySetCatchTagAt(expr, index, _enc(catch_tag))


BinaryenTrySetCatchTagAt = TrySetCatchTagAt


def TryAppendCatchTag(
    expr: BinaryenExpressionRef,
    catch_tag: str,
) -> BinaryenIndex:
    """ Appends a catch tag to a `try` expression, returning its insertion index. """
    return lib.BinaryenTryAppendCatchTag(expr, _enc(catch_tag))


BinaryenTryAppendCatchTag = TryAppendCatchTag


def TryInsertCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_tag: str,
) -> None:
    """
    Inserts a catch tag at the specified index of a `try` expression, moving
    existing catch tags including the one previously at that index one index up.
    """
    lib.BinaryenTryInsertCatchTagAt(expr, index, _enc(catch_tag))


BinaryenTryInsertCatchTagAt = TryInsertCatchTagAt


def TryRemoveCatchTagAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> str:
    """
    Removes the catch tag at the specified index of a `try` expression, moving
    all subsequent catch tags one index down. Returns the tag.
    """
    return _dec(lib.BinaryenTryRemoveCatchTagAt(expr, index))


BinaryenTryRemoveCatchTagAt = TryRemoveCatchTagAt


def TryGetCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the catch body expression at the specified index of a `try` expression. """
    return lib.BinaryenTryGetCatchBodyAt(expr, index)


BinaryenTryGetCatchBodyAt = TryGetCatchBodyAt


def TrySetCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the catch body expression at the specified index of a `try` expression. """
    lib.BinaryenTrySetCatchBodyAt(expr, index, catch_expr)


BinaryenTrySetCatchBodyAt = TrySetCatchBodyAt


def TryAppendCatchBody(
    expr: BinaryenExpressionRef,
    catch_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends a catch expression to a `try` expression, returning its insertion
    index.
    """
    return lib.BinaryenTryAppendCatchBody(expr, catch_expr)


BinaryenTryAppendCatchBody = TryAppendCatchBody


def TryInsertCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    catch_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts a catch expression at the specified index of a `try` expression,
    moving existing catch bodies including the one previously at that index one
    index up.
    """
    lib.BinaryenTryInsertCatchBodyAt(expr, index, catch_expr)


BinaryenTryInsertCatchBodyAt = TryInsertCatchBodyAt


def TryRemoveCatchBodyAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the catch expression at the specified index of a `try` expression,
    moving all subsequent catch bodies one index down. Returns the catch
    expression.
    """
    return lib.BinaryenTryRemoveCatchBodyAt(expr, index)


BinaryenTryRemoveCatchBodyAt = TryRemoveCatchBodyAt


def TryHasCatchAll(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `try` expression has a catch_all clause. """
    return lib.BinaryenTryHasCatchAll(expr)


BinaryenTryHasCatchAll = TryHasCatchAll


def TryGetDelegateTarget(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the target label of a `delegate`. """
    return _dec(lib.BinaryenTryGetDelegateTarget(expr))


BinaryenTryGetDelegateTarget = TryGetDelegateTarget


def TrySetDelegateTarget(
    expr: BinaryenExpressionRef,
    delegate_target: str,
) -> None:
    """ Sets the target label of a `delegate`. """
    lib.BinaryenTrySetDelegateTarget(expr, _enc(delegate_target))


BinaryenTrySetDelegateTarget = TrySetDelegateTarget


def TryIsDelegate(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether a `try` expression is a try-delegate. """
    return lib.BinaryenTryIsDelegate(expr)


BinaryenTryIsDelegate = TryIsDelegate


def ThrowGetTag(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the name of the tag being thrown by a `throw` expression. """
    return _dec(lib.BinaryenThrowGetTag(expr))


BinaryenThrowGetTag = ThrowGetTag


def ThrowSetTag(
    expr: BinaryenExpressionRef,
    tag_name: str,
) -> None:
    """ Sets the name of the tag being thrown by a `throw` expression. """
    lib.BinaryenThrowSetTag(expr, _enc(tag_name))


BinaryenThrowSetTag = ThrowSetTag


def ThrowGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of operands of a `throw` expression. """
    return lib.BinaryenThrowGetNumOperands(expr)


BinaryenThrowGetNumOperands = ThrowGetNumOperands


def ThrowGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the operand at the specified index of a `throw` expression. """
    return lib.BinaryenThrowGetOperandAt(expr, index)


BinaryenThrowGetOperandAt = ThrowGetOperandAt


def ThrowSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the operand at the specified index of a `throw` expression. """
    lib.BinaryenThrowSetOperandAt(expr, index, operand_expr)


BinaryenThrowSetOperandAt = ThrowSetOperandAt


def ThrowAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `throw` expression, returning its
    insertion index.
    """
    return lib.BinaryenThrowAppendOperand(expr, operand_expr)


BinaryenThrowAppendOperand = ThrowAppendOperand


def ThrowInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `throw` expression,
    moving existing operands including the one previously at that index one index
    up.
    """
    lib.BinaryenThrowInsertOperandAt(expr, index, operand_expr)


BinaryenThrowInsertOperandAt = ThrowInsertOperandAt


def ThrowRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `throw`
    expression, moving all subsequent operands one index down. Returns the
    operand expression.
    """
    return lib.BinaryenThrowRemoveOperandAt(expr, index)


BinaryenThrowRemoveOperandAt = ThrowRemoveOperandAt


def RethrowGetTarget(
    expr: BinaryenExpressionRef,
) -> str:
    """ Gets the target catch's corresponding try label of a `rethrow` expression. """
    return _dec(lib.BinaryenRethrowGetTarget(expr))


BinaryenRethrowGetTarget = RethrowGetTarget


def RethrowSetTarget(
    expr: BinaryenExpressionRef,
    target: str,
) -> None:
    """ Sets the target catch's corresponding try label of a `rethrow` expression. """
    lib.BinaryenRethrowSetTarget(expr, _enc(target))


BinaryenRethrowSetTarget = RethrowSetTarget


def TupleMakeGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the number of operands of a `tuple.make` expression. """
    return lib.BinaryenTupleMakeGetNumOperands(expr)


BinaryenTupleMakeGetNumOperands = TupleMakeGetNumOperands


def TupleMakeGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """ Gets the operand at the specified index of a `tuple.make` expression. """
    return lib.BinaryenTupleMakeGetOperandAt(expr, index)


BinaryenTupleMakeGetOperandAt = TupleMakeGetOperandAt


def TupleMakeSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the operand at the specified index of a `tuple.make` expression. """
    lib.BinaryenTupleMakeSetOperandAt(expr, index, operand_expr)


BinaryenTupleMakeSetOperandAt = TupleMakeSetOperandAt


def TupleMakeAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """
    Appends an operand expression to a `tuple.make` expression, returning its
    insertion index.
    """
    return lib.BinaryenTupleMakeAppendOperand(expr, operand_expr)


BinaryenTupleMakeAppendOperand = TupleMakeAppendOperand


def TupleMakeInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    """
    Inserts an operand expression at the specified index of a `tuple.make`
    expression, moving existing operands including the one previously at that
    index one index up.
    """
    lib.BinaryenTupleMakeInsertOperandAt(expr, index, operand_expr)


BinaryenTupleMakeInsertOperandAt = TupleMakeInsertOperandAt


def TupleMakeRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Removes the operand expression at the specified index of a `tuple.make`
    expression, moving all subsequent operands one index down. Returns the
    operand expression.
    """
    return lib.BinaryenTupleMakeRemoveOperandAt(expr, index)


BinaryenTupleMakeRemoveOperandAt = TupleMakeRemoveOperandAt


def TupleExtractGetTuple(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the tuple extracted from of a `tuple.extract` expression. """
    return lib.BinaryenTupleExtractGetTuple(expr)


BinaryenTupleExtractGetTuple = TupleExtractGetTuple


def TupleExtractSetTuple(
    expr: BinaryenExpressionRef,
    tuple_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the tuple extracted from of a `tuple.extract` expression. """
    lib.BinaryenTupleExtractSetTuple(expr, tuple_expr)


BinaryenTupleExtractSetTuple = TupleExtractSetTuple


def TupleExtractGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    """ Gets the index extracted at of a `tuple.extract` expression. """
    return lib.BinaryenTupleExtractGetIndex(expr)


BinaryenTupleExtractGetIndex = TupleExtractGetIndex


def TupleExtractSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    """ Sets the index extracted at of a `tuple.extract` expression. """
    lib.BinaryenTupleExtractSetIndex(expr, index)


BinaryenTupleExtractSetIndex = TupleExtractSetIndex


def I31NewGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the value expression of an `i31.new` expression. """
    return lib.BinaryenI31NewGetValue(expr)


BinaryenI31NewGetValue = I31NewGetValue


def I31NewSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the value expression of an `i31.new` expression. """
    lib.BinaryenI31NewSetValue(expr, value_expr)


BinaryenI31NewSetValue = I31NewSetValue


def I31GetGetI31(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """ Gets the i31 expression of an `i31.get` expression. """
    return lib.BinaryenI31GetGetI31(expr)


BinaryenI31GetGetI31 = I31GetGetI31


def I31GetSetI31(
    expr: BinaryenExpressionRef,
    i31_expr: BinaryenExpressionRef,
) -> None:
    """ Sets the i31 expression of an `i31.get` expression. """
    lib.BinaryenI31GetSetI31(expr, i31_expr)


BinaryenI31GetSetI31 = I31GetSetI31


def I31GetIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    """ Gets whether an `i31.get` expression returns a signed value (`_s`). """
    return lib.BinaryenI31GetIsSigned(expr)


BinaryenI31GetIsSigned = I31GetIsSigned


def I31GetSetSigned(
    expr: BinaryenExpressionRef,
    signed_: bool,
) -> None:
    """ Sets whether an `i31.get` expression returns a signed value (`_s`). """
    lib.BinaryenI31GetSetSigned(expr, signed_)


BinaryenI31GetSetSigned = I31GetSetSigned


def CallRefGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenCallRefGetNumOperands(expr)


BinaryenCallRefGetNumOperands = CallRefGetNumOperands


def CallRefGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRefGetOperandAt(expr, index)


BinaryenCallRefGetOperandAt = CallRefGetOperandAt


def CallRefSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenCallRefSetOperandAt(expr, index, operand_expr)


BinaryenCallRefSetOperandAt = CallRefSetOperandAt


def CallRefAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenCallRefAppendOperand(expr, operand_expr)


BinaryenCallRefAppendOperand = CallRefAppendOperand


def CallRefInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenCallRefInsertOperandAt(expr, index, operand_expr)


BinaryenCallRefInsertOperandAt = CallRefInsertOperandAt


def CallRefRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRefRemoveOperandAt(expr, index)


BinaryenCallRefRemoveOperandAt = CallRefRemoveOperandAt


def CallRefGetTarget(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenCallRefGetTarget(expr)


BinaryenCallRefGetTarget = CallRefGetTarget


def CallRefSetTarget(
    expr: BinaryenExpressionRef,
    target_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenCallRefSetTarget(expr, target_expr)


BinaryenCallRefSetTarget = CallRefSetTarget


def CallRefIsReturn(
    expr: BinaryenExpressionRef,
) -> bool:
    return lib.BinaryenCallRefIsReturn(expr)


BinaryenCallRefIsReturn = CallRefIsReturn


def CallRefSetReturn(
    expr: BinaryenExpressionRef,
    is_return: bool,
) -> None:
    lib.BinaryenCallRefSetReturn(expr, is_return)


BinaryenCallRefSetReturn = CallRefSetReturn


def RefTestGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefTestGetRef(expr)


BinaryenRefTestGetRef = RefTestGetRef


def RefTestSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenRefTestSetRef(expr, ref_expr)


BinaryenRefTestSetRef = RefTestSetRef


def RefTestGetIntendedType(
    expr: BinaryenExpressionRef,
) -> BinaryenHeapType:
    return lib.BinaryenRefTestGetIntendedType(expr)


BinaryenRefTestGetIntendedType = RefTestGetIntendedType


def RefTestSetIntendedType(
    expr: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> None:
    lib.BinaryenRefTestSetIntendedType(expr, intended_type)


BinaryenRefTestSetIntendedType = RefTestSetIntendedType


def RefCastGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenRefCastGetRef(expr)


BinaryenRefCastGetRef = RefCastGetRef


def RefCastSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenRefCastSetRef(expr, ref_expr)


BinaryenRefCastSetRef = RefCastSetRef


def RefCastGetIntendedType(
    expr: BinaryenExpressionRef,
) -> BinaryenHeapType:
    return lib.BinaryenRefCastGetIntendedType(expr)


BinaryenRefCastGetIntendedType = RefCastGetIntendedType


def RefCastSetIntendedType(
    expr: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> None:
    lib.BinaryenRefCastSetIntendedType(expr, intended_type)


BinaryenRefCastSetIntendedType = RefCastSetIntendedType


def BrOnGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    return lib.BinaryenBrOnGetOp(expr)


BinaryenBrOnGetOp = BrOnGetOp


def BrOnSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenBrOnSetOp(expr, op)


BinaryenBrOnSetOp = BrOnSetOp


def BrOnGetName(
    expr: BinaryenExpressionRef,
) -> str:
    return _dec(lib.BinaryenBrOnGetName(expr))


BinaryenBrOnGetName = BrOnGetName


def BrOnSetName(
    expr: BinaryenExpressionRef,
    name_str: str,
) -> None:
    lib.BinaryenBrOnSetName(expr, _enc(name_str))


BinaryenBrOnSetName = BrOnSetName


def BrOnGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenBrOnGetRef(expr)


BinaryenBrOnGetRef = BrOnGetRef


def BrOnSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenBrOnSetRef(expr, ref_expr)


BinaryenBrOnSetRef = BrOnSetRef


def BrOnGetIntendedType(
    expr: BinaryenExpressionRef,
) -> BinaryenHeapType:
    return lib.BinaryenBrOnGetIntendedType(expr)


BinaryenBrOnGetIntendedType = BrOnGetIntendedType


def BrOnSetIntendedType(
    expr: BinaryenExpressionRef,
    intended_type: BinaryenHeapType,
) -> None:
    lib.BinaryenBrOnSetIntendedType(expr, intended_type)


BinaryenBrOnSetIntendedType = BrOnSetIntendedType


def StructNewGetNumOperands(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenStructNewGetNumOperands(expr)


BinaryenStructNewGetNumOperands = StructNewGetNumOperands


def StructNewGetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructNewGetOperandAt(expr, index)


BinaryenStructNewGetOperandAt = StructNewGetOperandAt


def StructNewSetOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructNewSetOperandAt(expr, index, operand_expr)


BinaryenStructNewSetOperandAt = StructNewSetOperandAt


def StructNewAppendOperand(
    expr: BinaryenExpressionRef,
    operand_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenStructNewAppendOperand(expr, operand_expr)


BinaryenStructNewAppendOperand = StructNewAppendOperand


def StructNewInsertOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    operand_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructNewInsertOperandAt(expr, index, operand_expr)


BinaryenStructNewInsertOperandAt = StructNewInsertOperandAt


def StructNewRemoveOperandAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructNewRemoveOperandAt(expr, index)


BinaryenStructNewRemoveOperandAt = StructNewRemoveOperandAt


def StructGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenStructGetGetIndex(expr)


BinaryenStructGetGetIndex = StructGetGetIndex


def StructGetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    lib.BinaryenStructGetSetIndex(expr, index)


BinaryenStructGetSetIndex = StructGetSetIndex


def StructGetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructGetGetRef(expr)


BinaryenStructGetGetRef = StructGetGetRef


def StructGetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructGetSetRef(expr, ref_expr)


BinaryenStructGetSetRef = StructGetSetRef


def StructGetIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    return lib.BinaryenStructGetIsSigned(expr)


BinaryenStructGetIsSigned = StructGetIsSigned


def StructGetSetSigned(
    expr: BinaryenExpressionRef,
    signed_: bool,
) -> None:
    lib.BinaryenStructGetSetSigned(expr, signed_)


BinaryenStructGetSetSigned = StructGetSetSigned


def StructSetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenStructSetGetIndex(expr)


BinaryenStructSetGetIndex = StructSetGetIndex


def StructSetSetIndex(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> None:
    lib.BinaryenStructSetSetIndex(expr, index)


BinaryenStructSetSetIndex = StructSetSetIndex


def StructSetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructSetGetRef(expr)


BinaryenStructSetGetRef = StructSetGetRef


def StructSetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructSetSetRef(expr, ref_expr)


BinaryenStructSetSetRef = StructSetSetRef


def StructSetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStructSetGetValue(expr)


BinaryenStructSetGetValue = StructSetGetValue


def StructSetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStructSetSetValue(expr, value_expr)


BinaryenStructSetSetValue = StructSetSetValue


def ArrayNewGetInit(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayNewGetInit(expr)


BinaryenArrayNewGetInit = ArrayNewGetInit


def ArrayNewSetInit(
    expr: BinaryenExpressionRef,
    init_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayNewSetInit(expr, init_expr)


BinaryenArrayNewSetInit = ArrayNewSetInit


def ArrayNewGetSize(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayNewGetSize(expr)


BinaryenArrayNewGetSize = ArrayNewGetSize


def ArrayNewSetSize(
    expr: BinaryenExpressionRef,
    size_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayNewSetSize(expr, size_expr)


BinaryenArrayNewSetSize = ArrayNewSetSize


def ArrayInitGetNumValues(
    expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenArrayInitGetNumValues(expr)


BinaryenArrayInitGetNumValues = ArrayInitGetNumValues


def ArrayInitGetValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayInitGetValueAt(expr, index)


BinaryenArrayInitGetValueAt = ArrayInitGetValueAt


def ArrayInitSetValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayInitSetValueAt(expr, index, value_expr)


BinaryenArrayInitSetValueAt = ArrayInitSetValueAt


def ArrayInitAppendValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> BinaryenIndex:
    return lib.BinaryenArrayInitAppendValue(expr, value_expr)


BinaryenArrayInitAppendValue = ArrayInitAppendValue


def ArrayInitInsertValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayInitInsertValueAt(expr, index, value_expr)


BinaryenArrayInitInsertValueAt = ArrayInitInsertValueAt


def ArrayInitRemoveValueAt(
    expr: BinaryenExpressionRef,
    index: BinaryenIndex,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayInitRemoveValueAt(expr, index)


BinaryenArrayInitRemoveValueAt = ArrayInitRemoveValueAt


def ArrayGetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayGetGetRef(expr)


BinaryenArrayGetGetRef = ArrayGetGetRef


def ArrayGetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayGetSetRef(expr, ref_expr)


BinaryenArrayGetSetRef = ArrayGetSetRef


def ArrayGetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayGetGetIndex(expr)


BinaryenArrayGetGetIndex = ArrayGetGetIndex


def ArrayGetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayGetSetIndex(expr, index_expr)


BinaryenArrayGetSetIndex = ArrayGetSetIndex


def ArrayGetIsSigned(
    expr: BinaryenExpressionRef,
) -> bool:
    return lib.BinaryenArrayGetIsSigned(expr)


BinaryenArrayGetIsSigned = ArrayGetIsSigned


def ArrayGetSetSigned(
    expr: BinaryenExpressionRef,
    signed_: bool,
) -> None:
    lib.BinaryenArrayGetSetSigned(expr, signed_)


BinaryenArrayGetSetSigned = ArrayGetSetSigned


def ArraySetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArraySetGetRef(expr)


BinaryenArraySetGetRef = ArraySetGetRef


def ArraySetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArraySetSetRef(expr, ref_expr)


BinaryenArraySetSetRef = ArraySetSetRef


def ArraySetGetIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArraySetGetIndex(expr)


BinaryenArraySetGetIndex = ArraySetGetIndex


def ArraySetSetIndex(
    expr: BinaryenExpressionRef,
    index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArraySetSetIndex(expr, index_expr)


BinaryenArraySetSetIndex = ArraySetSetIndex


def ArraySetGetValue(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArraySetGetValue(expr)


BinaryenArraySetGetValue = ArraySetGetValue


def ArraySetSetValue(
    expr: BinaryenExpressionRef,
    value_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArraySetSetValue(expr, value_expr)


BinaryenArraySetSetValue = ArraySetSetValue


def ArrayLenGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayLenGetRef(expr)


BinaryenArrayLenGetRef = ArrayLenGetRef


def ArrayLenSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayLenSetRef(expr, ref_expr)


BinaryenArrayLenSetRef = ArrayLenSetRef


def ArrayCopyGetDestRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetDestRef(expr)


BinaryenArrayCopyGetDestRef = ArrayCopyGetDestRef


def ArrayCopySetDestRef(
    expr: BinaryenExpressionRef,
    dest_ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetDestRef(expr, dest_ref_expr)


BinaryenArrayCopySetDestRef = ArrayCopySetDestRef


def ArrayCopyGetDestIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetDestIndex(expr)


BinaryenArrayCopyGetDestIndex = ArrayCopyGetDestIndex


def ArrayCopySetDestIndex(
    expr: BinaryenExpressionRef,
    dest_index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetDestIndex(expr, dest_index_expr)


BinaryenArrayCopySetDestIndex = ArrayCopySetDestIndex


def ArrayCopyGetSrcRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetSrcRef(expr)


BinaryenArrayCopyGetSrcRef = ArrayCopyGetSrcRef


def ArrayCopySetSrcRef(
    expr: BinaryenExpressionRef,
    src_ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetSrcRef(expr, src_ref_expr)


BinaryenArrayCopySetSrcRef = ArrayCopySetSrcRef


def ArrayCopyGetSrcIndex(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetSrcIndex(expr)


BinaryenArrayCopyGetSrcIndex = ArrayCopyGetSrcIndex


def ArrayCopySetSrcIndex(
    expr: BinaryenExpressionRef,
    src_index_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetSrcIndex(expr, src_index_expr)


BinaryenArrayCopySetSrcIndex = ArrayCopySetSrcIndex


def ArrayCopyGetLength(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenArrayCopyGetLength(expr)


BinaryenArrayCopyGetLength = ArrayCopyGetLength


def ArrayCopySetLength(
    expr: BinaryenExpressionRef,
    length_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenArrayCopySetLength(expr, length_expr)


BinaryenArrayCopySetLength = ArrayCopySetLength


def StringNewGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    return lib.BinaryenStringNewGetOp(expr)


BinaryenStringNewGetOp = StringNewGetOp


def StringNewSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringNewSetOp(expr, op)


BinaryenStringNewSetOp = StringNewSetOp


def StringNewGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetPtr(expr)


BinaryenStringNewGetPtr = StringNewGetPtr


def StringNewSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetPtr(expr, ptr_expr)


BinaryenStringNewSetPtr = StringNewSetPtr


def StringNewGetLength(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetLength(expr)


BinaryenStringNewGetLength = StringNewGetLength


def StringNewSetLength(
    expr: BinaryenExpressionRef,
    length_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetLength(expr, length_expr)


BinaryenStringNewSetLength = StringNewSetLength


def StringNewGetStart(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetStart(expr)


BinaryenStringNewGetStart = StringNewGetStart


def StringNewSetStart(
    expr: BinaryenExpressionRef,
    start_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetStart(expr, start_expr)


BinaryenStringNewSetStart = StringNewSetStart


def StringNewGetEnd(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringNewGetEnd(expr)


BinaryenStringNewGetEnd = StringNewGetEnd


def StringNewSetEnd(
    expr: BinaryenExpressionRef,
    end_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringNewSetEnd(expr, end_expr)


BinaryenStringNewSetEnd = StringNewSetEnd


def StringConstGetString(
    expr: BinaryenExpressionRef,
) -> str:
    return _dec(lib.BinaryenStringConstGetString(expr))


BinaryenStringConstGetString = StringConstGetString


def StringConstSetString(
    expr: BinaryenExpressionRef,
    string_str: str,
) -> None:
    lib.BinaryenStringConstSetString(expr, _enc(string_str))


BinaryenStringConstSetString = StringConstSetString


def StringMeasureGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    return lib.BinaryenStringMeasureGetOp(expr)


BinaryenStringMeasureGetOp = StringMeasureGetOp


def StringMeasureSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringMeasureSetOp(expr, op)


BinaryenStringMeasureSetOp = StringMeasureSetOp


def StringMeasureGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringMeasureGetRef(expr)


BinaryenStringMeasureGetRef = StringMeasureGetRef


def StringMeasureSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringMeasureSetRef(expr, ref_expr)


BinaryenStringMeasureSetRef = StringMeasureSetRef


def StringEncodeGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    return lib.BinaryenStringEncodeGetOp(expr)


BinaryenStringEncodeGetOp = StringEncodeGetOp


def StringEncodeSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringEncodeSetOp(expr, op)


BinaryenStringEncodeSetOp = StringEncodeSetOp


def StringEncodeGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncodeGetRef(expr)


BinaryenStringEncodeGetRef = StringEncodeGetRef


def StringEncodeSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEncodeSetRef(expr, ref_expr)


BinaryenStringEncodeSetRef = StringEncodeSetRef


def StringEncodeGetPtr(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncodeGetPtr(expr)


BinaryenStringEncodeGetPtr = StringEncodeGetPtr


def StringEncodeSetPtr(
    expr: BinaryenExpressionRef,
    ptr_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEncodeSetPtr(expr, ptr_expr)


BinaryenStringEncodeSetPtr = StringEncodeSetPtr


def StringEncodeGetStart(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEncodeGetStart(expr)


BinaryenStringEncodeGetStart = StringEncodeGetStart


def StringEncodeSetStart(
    expr: BinaryenExpressionRef,
    start_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEncodeSetStart(expr, start_expr)


BinaryenStringEncodeSetStart = StringEncodeSetStart


def StringConcatGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringConcatGetLeft(expr)


BinaryenStringConcatGetLeft = StringConcatGetLeft


def StringConcatSetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringConcatSetLeft(expr, left_expr)


BinaryenStringConcatSetLeft = StringConcatSetLeft


def StringConcatGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringConcatGetRight(expr)


BinaryenStringConcatGetRight = StringConcatGetRight


def StringConcatSetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringConcatSetRight(expr, right_expr)


BinaryenStringConcatSetRight = StringConcatSetRight


def StringEqGetLeft(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEqGetLeft(expr)


BinaryenStringEqGetLeft = StringEqGetLeft


def StringEqSetLeft(
    expr: BinaryenExpressionRef,
    left_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEqSetLeft(expr, left_expr)


BinaryenStringEqSetLeft = StringEqSetLeft


def StringEqGetRight(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringEqGetRight(expr)


BinaryenStringEqGetRight = StringEqGetRight


def StringEqSetRight(
    expr: BinaryenExpressionRef,
    right_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringEqSetRight(expr, right_expr)


BinaryenStringEqSetRight = StringEqSetRight


def StringAsGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    return lib.BinaryenStringAsGetOp(expr)


BinaryenStringAsGetOp = StringAsGetOp


def StringAsSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringAsSetOp(expr, op)


BinaryenStringAsSetOp = StringAsSetOp


def StringAsGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringAsGetRef(expr)


BinaryenStringAsGetRef = StringAsGetRef


def StringAsSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringAsSetRef(expr, ref_expr)


BinaryenStringAsSetRef = StringAsSetRef


def StringWTF8AdvanceGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF8AdvanceGetRef(expr)


BinaryenStringWTF8AdvanceGetRef = StringWTF8AdvanceGetRef


def StringWTF8AdvanceSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF8AdvanceSetRef(expr, ref_expr)


BinaryenStringWTF8AdvanceSetRef = StringWTF8AdvanceSetRef


def StringWTF8AdvanceGetPos(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF8AdvanceGetPos(expr)


BinaryenStringWTF8AdvanceGetPos = StringWTF8AdvanceGetPos


def StringWTF8AdvanceSetPos(
    expr: BinaryenExpressionRef,
    pos_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF8AdvanceSetPos(expr, pos_expr)


BinaryenStringWTF8AdvanceSetPos = StringWTF8AdvanceSetPos


def StringWTF8AdvanceGetBytes(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF8AdvanceGetBytes(expr)


BinaryenStringWTF8AdvanceGetBytes = StringWTF8AdvanceGetBytes


def StringWTF8AdvanceSetBytes(
    expr: BinaryenExpressionRef,
    bytes_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF8AdvanceSetBytes(expr, bytes_expr)


BinaryenStringWTF8AdvanceSetBytes = StringWTF8AdvanceSetBytes


def StringWTF16GetGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF16GetGetRef(expr)


BinaryenStringWTF16GetGetRef = StringWTF16GetGetRef


def StringWTF16GetSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF16GetSetRef(expr, ref_expr)


BinaryenStringWTF16GetSetRef = StringWTF16GetSetRef


def StringWTF16GetGetPos(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringWTF16GetGetPos(expr)


BinaryenStringWTF16GetGetPos = StringWTF16GetGetPos


def StringWTF16GetSetPos(
    expr: BinaryenExpressionRef,
    pos_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringWTF16GetSetPos(expr, pos_expr)


BinaryenStringWTF16GetSetPos = StringWTF16GetSetPos


def StringIterNextGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterNextGetRef(expr)


BinaryenStringIterNextGetRef = StringIterNextGetRef


def StringIterNextSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringIterNextSetRef(expr, ref_expr)


BinaryenStringIterNextSetRef = StringIterNextSetRef


def StringIterMoveGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    return lib.BinaryenStringIterMoveGetOp(expr)


BinaryenStringIterMoveGetOp = StringIterMoveGetOp


def StringIterMoveSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringIterMoveSetOp(expr, op)


BinaryenStringIterMoveSetOp = StringIterMoveSetOp


def StringIterMoveGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterMoveGetRef(expr)


BinaryenStringIterMoveGetRef = StringIterMoveGetRef


def StringIterMoveSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringIterMoveSetRef(expr, ref_expr)


BinaryenStringIterMoveSetRef = StringIterMoveSetRef


def StringIterMoveGetNum(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringIterMoveGetNum(expr)


BinaryenStringIterMoveGetNum = StringIterMoveGetNum


def StringIterMoveSetNum(
    expr: BinaryenExpressionRef,
    num_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringIterMoveSetNum(expr, num_expr)


BinaryenStringIterMoveSetNum = StringIterMoveSetNum


def StringSliceWTFGetOp(
    expr: BinaryenExpressionRef,
) -> BinaryenOp:
    return lib.BinaryenStringSliceWTFGetOp(expr)


BinaryenStringSliceWTFGetOp = StringSliceWTFGetOp


def StringSliceWTFSetOp(
    expr: BinaryenExpressionRef,
    op: BinaryenOp,
) -> None:
    lib.BinaryenStringSliceWTFSetOp(expr, op)


BinaryenStringSliceWTFSetOp = StringSliceWTFSetOp


def StringSliceWTFGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTFGetRef(expr)


BinaryenStringSliceWTFGetRef = StringSliceWTFGetRef


def StringSliceWTFSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceWTFSetRef(expr, ref_expr)


BinaryenStringSliceWTFSetRef = StringSliceWTFSetRef


def StringSliceWTFGetStart(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTFGetStart(expr)


BinaryenStringSliceWTFGetStart = StringSliceWTFGetStart


def StringSliceWTFSetStart(
    expr: BinaryenExpressionRef,
    start_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceWTFSetStart(expr, start_expr)


BinaryenStringSliceWTFSetStart = StringSliceWTFSetStart


def StringSliceWTFGetEnd(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceWTFGetEnd(expr)


BinaryenStringSliceWTFGetEnd = StringSliceWTFGetEnd


def StringSliceWTFSetEnd(
    expr: BinaryenExpressionRef,
    end_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceWTFSetEnd(expr, end_expr)


BinaryenStringSliceWTFSetEnd = StringSliceWTFSetEnd


def StringSliceIterGetRef(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceIterGetRef(expr)


BinaryenStringSliceIterGetRef = StringSliceIterGetRef


def StringSliceIterSetRef(
    expr: BinaryenExpressionRef,
    ref_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceIterSetRef(expr, ref_expr)


BinaryenStringSliceIterSetRef = StringSliceIterSetRef


def StringSliceIterGetNum(
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    return lib.BinaryenStringSliceIterGetNum(expr)


BinaryenStringSliceIterGetNum = StringSliceIterGetNum


def StringSliceIterSetNum(
    expr: BinaryenExpressionRef,
    num_expr: BinaryenExpressionRef,
) -> None:
    lib.BinaryenStringSliceIterSetNum(expr, num_expr)


BinaryenStringSliceIterSetNum = StringSliceIterSetNum


def AddFunction(
    module: BinaryenModuleRef,
    name: str,
    params: BinaryenType,
    results: BinaryenType,
    var_types: Optional[List[BinaryenType]],
    body: BinaryenExpressionRef,
) -> BinaryenFunctionRef:
    """
    Adds a function to the module. This is thread-safe.
    @varTypes: the types of variables. In WebAssembly, vars share
    an index space with params. In other words, params come from
    the function type, and vars are provided in this call, and
    together they are all the locals. The order is first params
    and then vars, so if you have one param it will be at index
    0 (and written $0), and if you also have 2 vars they will be
    at indexes 1 and 2, etc., that is, they share an index space.
    """
    return lib.BinaryenAddFunction(module, _enc(name), params, results, _opt_seq(var_types), _len(var_types), body)


BinaryenAddFunction = AddFunction


def GetFunction(
    module: BinaryenModuleRef,
    name: str,
) -> Optional[BinaryenFunctionRef]:
    """
    Gets a function reference by name. Returns NULL if the function does not
    exist.
    """
    return lib.BinaryenGetFunction(module, _enc(name))


BinaryenGetFunction = GetFunction


def RemoveFunction(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    """ Removes a function by name. """
    lib.BinaryenRemoveFunction(module, _enc(name))


BinaryenRemoveFunction = RemoveFunction


def GetNumFunctions(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    """ Gets the number of functions in the module. """
    return lib.BinaryenGetNumFunctions(module)


BinaryenGetNumFunctions = GetNumFunctions


def GetFunctionByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenFunctionRef:
    """ Gets the function at the specified index. """
    return lib.BinaryenGetFunctionByIndex(module, index)


BinaryenGetFunctionByIndex = GetFunctionByIndex


def AddFunctionImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    params: BinaryenType,
    results: BinaryenType,
) -> None:
    lib.BinaryenAddFunctionImport(module, _enc(internal_name), _enc(external_module_name), _enc(external_base_name), params, results)


BinaryenAddFunctionImport = AddFunctionImport


def AddTableImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
) -> None:
    lib.BinaryenAddTableImport(module, _enc(internal_name), _enc(external_module_name), _enc(external_base_name))


BinaryenAddTableImport = AddTableImport


def AddMemoryImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    shared: int,
) -> None:
    lib.BinaryenAddMemoryImport(module, _enc(internal_name), _enc(external_module_name), _enc(external_base_name), shared)


BinaryenAddMemoryImport = AddMemoryImport


def AddGlobalImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    global_type: BinaryenType,
    mutable_: bool,
) -> None:
    lib.BinaryenAddGlobalImport(module, _enc(internal_name), _enc(external_module_name), _enc(external_base_name), global_type, mutable_)


BinaryenAddGlobalImport = AddGlobalImport


def AddTagImport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_module_name: str,
    external_base_name: str,
    params: BinaryenType,
    results: BinaryenType,
) -> None:
    lib.BinaryenAddTagImport(module, _enc(internal_name), _enc(external_module_name), _enc(external_base_name), params, results)


BinaryenAddTagImport = AddTagImport


def AddFunctionExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a function export to the module. """
    return lib.BinaryenAddFunctionExport(module, _enc(internal_name), _enc(external_name))


BinaryenAddFunctionExport = AddFunctionExport


def AddTableExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a table export to the module. """
    return lib.BinaryenAddTableExport(module, _enc(internal_name), _enc(external_name))


BinaryenAddTableExport = AddTableExport


def AddMemoryExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a memory export to the module. """
    return lib.BinaryenAddMemoryExport(module, _enc(internal_name), _enc(external_name))


BinaryenAddMemoryExport = AddMemoryExport


def AddGlobalExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a global export to the module. """
    return lib.BinaryenAddGlobalExport(module, _enc(internal_name), _enc(external_name))


BinaryenAddGlobalExport = AddGlobalExport


def AddTagExport(
    module: BinaryenModuleRef,
    internal_name: str,
    external_name: str,
) -> BinaryenExportRef:
    """ Adds a tag export to the module. """
    return lib.BinaryenAddTagExport(module, _enc(internal_name), _enc(external_name))


BinaryenAddTagExport = AddTagExport


def GetExport(
    module: BinaryenModuleRef,
    external_name: str,
) -> Optional[BinaryenExportRef]:
    """
    Gets an export reference by external name. Returns NULL if the export does
    not exist.
    """
    return lib.BinaryenGetExport(module, _enc(external_name))


BinaryenGetExport = GetExport


def RemoveExport(
    module: BinaryenModuleRef,
    external_name: str,
) -> None:
    """ Removes an export by external name. """
    lib.BinaryenRemoveExport(module, _enc(external_name))


BinaryenRemoveExport = RemoveExport


def GetNumExports(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    """ Gets the number of exports in the module. """
    return lib.BinaryenGetNumExports(module)


BinaryenGetNumExports = GetNumExports


def GetExportByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenExportRef:
    """ Gets the export at the specified index. """
    return lib.BinaryenGetExportByIndex(module, index)


BinaryenGetExportByIndex = GetExportByIndex


def AddGlobal(
    module: BinaryenModuleRef,
    name: str,
    _type: BinaryenType,
    mutable_: bool,
    init: BinaryenExpressionRef,
) -> BinaryenGlobalRef:
    """ Adds a global to the module. """
    return lib.BinaryenAddGlobal(module, _enc(name), _type, mutable_, init)


BinaryenAddGlobal = AddGlobal


def GetGlobal(
    module: BinaryenModuleRef,
    name: str,
) -> Optional[BinaryenGlobalRef]:
    """ Gets a global reference by name. Returns NULL if the global does not exist. """
    return lib.BinaryenGetGlobal(module, _enc(name))


BinaryenGetGlobal = GetGlobal


def RemoveGlobal(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    """ Removes a global by name. """
    lib.BinaryenRemoveGlobal(module, _enc(name))


BinaryenRemoveGlobal = RemoveGlobal


def GetNumGlobals(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    """ Gets the number of globals in the module. """
    return lib.BinaryenGetNumGlobals(module)


BinaryenGetNumGlobals = GetNumGlobals


def GetGlobalByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenGlobalRef:
    """ Gets the global at the specified index. """
    return lib.BinaryenGetGlobalByIndex(module, index)


BinaryenGetGlobalByIndex = GetGlobalByIndex


def AddTag(
    module: BinaryenModuleRef,
    name: str,
    params: BinaryenType,
    results: BinaryenType,
) -> BinaryenTagRef:
    """ Adds a tag to the module. """
    return lib.BinaryenAddTag(module, _enc(name), params, results)


BinaryenAddTag = AddTag


def GetTag(
    module: BinaryenModuleRef,
    name: str,
) -> Optional[BinaryenTagRef]:
    """ Gets a tag reference by name. Returns NULL if the tag does not exist. """
    return lib.BinaryenGetTag(module, _enc(name))


BinaryenGetTag = GetTag


def RemoveTag(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    """ Removes a tag by name. """
    lib.BinaryenRemoveTag(module, _enc(name))


BinaryenRemoveTag = RemoveTag


def AddTable(
    module: BinaryenModuleRef,
    table: str,
    initial: BinaryenIndex,
    maximum: BinaryenIndex,
    table_type: BinaryenType,
) -> BinaryenTableRef:
    return lib.BinaryenAddTable(module, _enc(table), initial, maximum, table_type)


BinaryenAddTable = AddTable


def RemoveTable(
    module: BinaryenModuleRef,
    table: str,
) -> None:
    lib.BinaryenRemoveTable(module, _enc(table))


BinaryenRemoveTable = RemoveTable


def GetNumTables(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    return lib.BinaryenGetNumTables(module)


BinaryenGetNumTables = GetNumTables


def GetTable(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenTableRef:
    return lib.BinaryenGetTable(module, _enc(name))


BinaryenGetTable = GetTable


def GetTableByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenTableRef:
    return lib.BinaryenGetTableByIndex(module, index)


BinaryenGetTableByIndex = GetTableByIndex


def AddActiveElementSegment(
    module: BinaryenModuleRef,
    table: str,
    name: str,
    func_names: List[str],
    offset: BinaryenExpressionRef,
) -> BinaryenElementSegmentRef:
    return lib.BinaryenAddActiveElementSegment(
        module, _enc(table), _enc(name), _enc_seq(func_names), _len(func_names), offset
    )


BinaryenAddActiveElementSegment = AddActiveElementSegment


def AddPassiveElementSegment(
    module: BinaryenModuleRef,
    name: str,
    func_names: List[str],
) -> BinaryenElementSegmentRef:
    return lib.BinaryenAddPassiveElementSegment(
        module, _enc(name), _enc_seq(func_names), _len(func_names)
    )


BinaryenAddPassiveElementSegment = AddPassiveElementSegment


def RemoveElementSegment(
    module: BinaryenModuleRef,
    name: str,
) -> None:
    lib.BinaryenRemoveElementSegment(module, _enc(name))


BinaryenRemoveElementSegment = RemoveElementSegment


def GetNumElementSegments(
    module: BinaryenModuleRef,
) -> BinaryenIndex:
    return lib.BinaryenGetNumElementSegments(module)


BinaryenGetNumElementSegments = GetNumElementSegments


def GetElementSegment(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenElementSegmentRef:
    return lib.BinaryenGetElementSegment(module, _enc(name))


BinaryenGetElementSegment = GetElementSegment


def GetElementSegmentByIndex(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> BinaryenElementSegmentRef:
    return lib.BinaryenGetElementSegmentByIndex(module, index)


BinaryenGetElementSegmentByIndex = GetElementSegmentByIndex


def SetMemory(
    module: BinaryenModuleRef,
    initial: BinaryenIndex,
    maximum: BinaryenIndex,
    export_name: Optional[str],
    segments: List[bytes],
    segment_passive: List[bool],
    segment_offsets: List[BinaryenExpressionRef],
    segment_sizes: List[BinaryenIndex],
    shared: bool,
    memory64: bool,
    name: str,
) -> None:
    """
    This will create a memory, overwriting any existing memory
    Each memory has data in segments, a start offset in segmentOffsets, and a
    size in segmentSizes. exportName can be NULL
    """
    lib.BinaryenSetMemory(
        module, initial, maximum, _enc(export_name), _enc_seq(segments), segment_passive,
        _opt_seq(segment_offsets), segment_sizes, _len(segment_sizes), shared, memory64, _enc(name)
    )


BinaryenSetMemory = SetMemory


def HasMemory(
    module: BinaryenModuleRef,
) -> bool:
    return lib.BinaryenHasMemory(module)


BinaryenHasMemory = HasMemory


def MemoryGetInitial(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenIndex:
    return lib.BinaryenMemoryGetInitial(module, _enc(name))


BinaryenMemoryGetInitial = MemoryGetInitial


def MemoryHasMax(
    module: BinaryenModuleRef,
    name: str,
) -> bool:
    return lib.BinaryenMemoryHasMax(module, _enc(name))


BinaryenMemoryHasMax = MemoryHasMax


def MemoryGetMax(
    module: BinaryenModuleRef,
    name: str,
) -> BinaryenIndex:
    return lib.BinaryenMemoryGetMax(module, _enc(name))


BinaryenMemoryGetMax = MemoryGetMax


def MemoryImportGetModule(
    module: BinaryenModuleRef,
    name: str,
) -> str:
    return _dec(lib.BinaryenMemoryImportGetModule(module, _enc(name)))


BinaryenMemoryImportGetModule = MemoryImportGetModule


def MemoryImportGetBase(
    module: BinaryenModuleRef,
    name: str,
) -> str:
    return _dec(lib.BinaryenMemoryImportGetBase(module, _enc(name)))


BinaryenMemoryImportGetBase = MemoryImportGetBase


def MemoryIsShared(
    module: BinaryenModuleRef,
    name: str,
) -> bool:
    return lib.BinaryenMemoryIsShared(module, _enc(name))


BinaryenMemoryIsShared = MemoryIsShared


def MemoryIs64(
    module: BinaryenModuleRef,
    name: str,
) -> bool:
    return lib.BinaryenMemoryIs64(module, _enc(name))


BinaryenMemoryIs64 = MemoryIs64


def GetNumMemorySegments(
    module: BinaryenModuleRef,
) -> int:
    return lib.BinaryenGetNumMemorySegments(module)


BinaryenGetNumMemorySegments = GetNumMemorySegments


def GetMemorySegmentByteOffset(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
) -> int:
    return lib.BinaryenGetMemorySegmentByteOffset(module, _id)


BinaryenGetMemorySegmentByteOffset = GetMemorySegmentByteOffset


def GetMemorySegmentByteLength(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
) -> int:
    return lib.BinaryenGetMemorySegmentByteLength(module, _id)


BinaryenGetMemorySegmentByteLength = GetMemorySegmentByteLength


def GetMemorySegmentPassive(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
) -> bool:
    return lib.BinaryenGetMemorySegmentPassive(module, _id)


BinaryenGetMemorySegmentPassive = GetMemorySegmentPassive


def CopyMemorySegmentData(
    module: BinaryenModuleRef,
    _id: BinaryenIndex,
) -> bytes:
    dim = lib.BinaryenGetMemorySegmentByteLength(module, _id)
    _buffer = ffi.new(f'char[{dim}]')
    lib.BinaryenCopyMemorySegmentData(module, _id, _buffer)
    return bytes(ffi.buffer(_buffer))


BinaryenCopyMemorySegmentData = CopyMemorySegmentData


def SetStart(
    module: BinaryenModuleRef,
    start: BinaryenFunctionRef,
) -> None:
    lib.BinaryenSetStart(module, start)


BinaryenSetStart = SetStart


def ModuleGetFeatures(
    module: BinaryenModuleRef,
) -> BinaryenFeatures:
    """ These control what features are allowed when validation and in passes. """
    return lib.BinaryenModuleGetFeatures(module)


BinaryenModuleGetFeatures = ModuleGetFeatures


def ModuleSetFeatures(
    module: BinaryenModuleRef,
    features: BinaryenFeatures,
) -> None:
    lib.BinaryenModuleSetFeatures(module, features)


BinaryenModuleSetFeatures = ModuleSetFeatures


def ModuleParse(
    text: str,
) -> BinaryenModuleRef:
    """ Parse a module in s-expression text format """
    return lib.BinaryenModuleParse(_enc(text))


BinaryenModuleParse = ModuleParse


def ModulePrint(
    module: BinaryenModuleRef,
) -> None:
    """ Print a module to stdout in s-expression text format. Useful for debugging. """
    lib.BinaryenModulePrint(module)


BinaryenModulePrint = ModulePrint


def ModulePrintStackIR(
    module: BinaryenModuleRef,
    optimize: bool,
) -> None:
    """ Print a module to stdout in stack IR text format. Useful for debugging. """
    lib.BinaryenModulePrintStackIR(module, optimize)


BinaryenModulePrintStackIR = ModulePrintStackIR


def ModulePrintAsmjs(
    module: BinaryenModuleRef,
) -> None:
    """ Print a module to stdout in asm.js syntax. """
    lib.BinaryenModulePrintAsmjs(module)


BinaryenModulePrintAsmjs = ModulePrintAsmjs


def ModuleValidate(
    module: BinaryenModuleRef,
) -> bool:
    """
    Validate a module, showing errors on problems.
    @return 0 if an error occurred, 1 if validated succesfully
    """
    return lib.BinaryenModuleValidate(module)


BinaryenModuleValidate = ModuleValidate


def ModuleOptimize(
    module: BinaryenModuleRef,
) -> None:
    """
    Runs the standard optimization passes on the module. Uses the currently set
    global optimize and shrink level.
    """
    lib.BinaryenModuleOptimize(module)


BinaryenModuleOptimize = ModuleOptimize


def ModuleUpdateMaps(
    module: BinaryenModuleRef,
) -> None:
    """
    Updates the internal name mapping logic in a module. This must be called
    after renaming module elements.
    """
    lib.BinaryenModuleUpdateMaps(module)


BinaryenModuleUpdateMaps = ModuleUpdateMaps


def GetOptimizeLevel() -> int:
    """
    Gets the currently set optimize level. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -O1, -O2 (default), etc.
    """
    return lib.BinaryenGetOptimizeLevel()


BinaryenGetOptimizeLevel = GetOptimizeLevel


def SetOptimizeLevel(
    level: int,
) -> None:
    """
    Sets the optimization level to use. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -O1, -O2 (default), etc.
    """
    lib.BinaryenSetOptimizeLevel(level)


BinaryenSetOptimizeLevel = SetOptimizeLevel


def GetShrinkLevel() -> int:
    """
    Gets the currently set shrink level. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -Os (default), -Oz.
    """
    return lib.BinaryenGetShrinkLevel()


BinaryenGetShrinkLevel = GetShrinkLevel


def SetShrinkLevel(
    level: int,
) -> None:
    """
    Sets the shrink level to use. Applies to all modules, globally.
    0, 1, 2 correspond to -O0, -Os (default), -Oz.
    """
    lib.BinaryenSetShrinkLevel(level)


BinaryenSetShrinkLevel = SetShrinkLevel


def GetDebugInfo() -> bool:
    """
    Gets whether generating debug information is currently enabled or not.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetDebugInfo()


BinaryenGetDebugInfo = GetDebugInfo


def SetDebugInfo(
    on: bool,
) -> None:
    """
    Enables or disables debug information in emitted binaries.
    Applies to all modules, globally.
    """
    lib.BinaryenSetDebugInfo(on)


BinaryenSetDebugInfo = SetDebugInfo


def GetLowMemoryUnused() -> bool:
    """
    Gets whether the low 1K of memory can be considered unused when optimizing.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetLowMemoryUnused()


BinaryenGetLowMemoryUnused = GetLowMemoryUnused


def SetLowMemoryUnused(
    on: bool,
) -> None:
    """
    Enables or disables whether the low 1K of memory can be considered unused
    when optimizing. Applies to all modules, globally.
    """
    lib.BinaryenSetLowMemoryUnused(on)


BinaryenSetLowMemoryUnused = SetLowMemoryUnused


def GetZeroFilledMemory() -> bool:
    """ Gets whether to assume that an imported memory is zero-initialized. """
    return lib.BinaryenGetZeroFilledMemory()


BinaryenGetZeroFilledMemory = GetZeroFilledMemory


def SetZeroFilledMemory(
    on: bool,
) -> None:
    """
    Enables or disables whether to assume that an imported memory is
    zero-initialized.
    """
    lib.BinaryenSetZeroFilledMemory(on)


BinaryenSetZeroFilledMemory = SetZeroFilledMemory


def GetFastMath() -> bool:
    """
    Gets whether fast math optimizations are enabled, ignoring for example
    corner cases of floating-point math like NaN changes.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetFastMath()


BinaryenGetFastMath = GetFastMath


def SetFastMath(
    value: bool,
) -> None:
    """
    Enables or disables fast math optimizations, ignoring for example
    corner cases of floating-point math like NaN changes.
    Applies to all modules, globally.
    """
    lib.BinaryenSetFastMath(value)


BinaryenSetFastMath = SetFastMath


def GetPassArgument(
    name: str,
) -> str:
    """
    Gets the value of the specified arbitrary pass argument.
    Applies to all modules, globally.
    """
    return _dec(lib.BinaryenGetPassArgument(_enc(name)))


BinaryenGetPassArgument = GetPassArgument


def SetPassArgument(
    name: str,
    value: str,
) -> None:
    """
    Sets the value of the specified arbitrary pass argument. Removes the
    respective argument if `value` is NULL. Applies to all modules, globally.
    """
    lib.BinaryenSetPassArgument(_enc(name), _enc(value))


BinaryenSetPassArgument = SetPassArgument


def ClearPassArguments() -> None:
    """
    Clears all arbitrary pass arguments.
    Applies to all modules, globally.
    """
    lib.BinaryenClearPassArguments()


BinaryenClearPassArguments = ClearPassArguments


def GetAlwaysInlineMaxSize() -> BinaryenIndex:
    """
    Gets the function size at which we always inline.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetAlwaysInlineMaxSize()


BinaryenGetAlwaysInlineMaxSize = GetAlwaysInlineMaxSize


def SetAlwaysInlineMaxSize(
    size: BinaryenIndex,
) -> None:
    """
    Sets the function size at which we always inline.
    Applies to all modules, globally.
    """
    lib.BinaryenSetAlwaysInlineMaxSize(size)


BinaryenSetAlwaysInlineMaxSize = SetAlwaysInlineMaxSize


def GetFlexibleInlineMaxSize() -> BinaryenIndex:
    """
    Gets the function size which we inline when functions are lightweight.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetFlexibleInlineMaxSize()


BinaryenGetFlexibleInlineMaxSize = GetFlexibleInlineMaxSize


def SetFlexibleInlineMaxSize(
    size: BinaryenIndex,
) -> None:
    """
    Sets the function size which we inline when functions are lightweight.
    Applies to all modules, globally.
    """
    lib.BinaryenSetFlexibleInlineMaxSize(size)


BinaryenSetFlexibleInlineMaxSize = SetFlexibleInlineMaxSize


def GetOneCallerInlineMaxSize() -> BinaryenIndex:
    """
    Gets the function size which we inline when there is only one caller.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetOneCallerInlineMaxSize()


BinaryenGetOneCallerInlineMaxSize = GetOneCallerInlineMaxSize


def SetOneCallerInlineMaxSize(
    size: BinaryenIndex,
) -> None:
    """
    Sets the function size which we inline when there is only one caller.
    Applies to all modules, globally.
    """
    lib.BinaryenSetOneCallerInlineMaxSize(size)


BinaryenSetOneCallerInlineMaxSize = SetOneCallerInlineMaxSize


def GetAllowInliningFunctionsWithLoops() -> bool:
    """
    Gets whether functions with loops are allowed to be inlined.
    Applies to all modules, globally.
    """
    return lib.BinaryenGetAllowInliningFunctionsWithLoops()


BinaryenGetAllowInliningFunctionsWithLoops = GetAllowInliningFunctionsWithLoops


def SetAllowInliningFunctionsWithLoops(
    enabled: bool,
) -> None:
    """
    Sets whether functions with loops are allowed to be inlined.
    Applies to all modules, globally.
    """
    lib.BinaryenSetAllowInliningFunctionsWithLoops(enabled)


BinaryenSetAllowInliningFunctionsWithLoops = SetAllowInliningFunctionsWithLoops


def ModuleRunPasses(
    module: BinaryenModuleRef,
    passes: List[str],
) -> None:
    """
    Runs the specified passes on the module. Uses the currently set global
    optimize and shrink level.
    """
    lib.BinaryenModuleRunPasses(module, _enc_seq(passes), _len(passes))


BinaryenModuleRunPasses = ModuleRunPasses


def ModuleAutoDrop(
    module: BinaryenModuleRef,
) -> None:
    """
    Auto-generate drop() operations where needed. This lets you generate code
    without worrying about where they are needed. (It is more efficient to do it
    yourself, but simpler to use autodrop).
    """
    lib.BinaryenModuleAutoDrop(module)


BinaryenModuleAutoDrop = ModuleAutoDrop


def ModuleWrite(
    module: BinaryenModuleRef,
    output_size: int,
) -> Tuple[bytes, int]:
    """
    Serialize a module into binary form. Uses the currently set global debugInfo
    option.
    @return how many bytes were written. This will be less than or equal to
    outputSize
    """
    _output = ffi.new(f'char[{output_size}]')
    written = lib.BinaryenModuleWrite(module, _output, output_size)
    return bytes(ffi.buffer(_output)), written


BinaryenModuleWrite = ModuleWrite


def ModuleWriteText(
    module: BinaryenModuleRef,
    output_size: int,
) -> Tuple[str, int]:
    """
    Serialize a module in s-expression text format.
    @return how many bytes were written. This will be less than or equal to
    outputSize
    """
    _output = ffi.new(f'char[{output_size}]')
    written = lib.BinaryenModuleWriteText(module, _output, output_size)
    return ffi.string(_output).decode(), written


BinaryenModuleWriteText = ModuleWriteText


def ModuleWriteStackIR(
    module: BinaryenModuleRef,
    output: str,
    output_size: int,
    optimize: bool,
) -> int:
    """
    Serialize a module in stack IR text format.
    @return how many bytes were written. This will be less than or equal to
    outputSize
    """
    return lib.BinaryenModuleWriteStackIR(module, _enc(output), output_size, optimize)


BinaryenModuleWriteStackIR = ModuleWriteStackIR


def ModuleWriteWithSourceMap(
    module: BinaryenModuleRef,
    url: str,
    output: str,
    output_size: int,
    source_map: str,
    source_map_size: int,
) -> BinaryenBufferSizes:
    """
    Serialize a module into binary form including its source map. Uses the
    currently set global debugInfo option.
    @returns how many bytes were written. This will be less than or equal to
    outputSize
    """
    return lib.BinaryenModuleWriteWithSourceMap(module, _enc(url), _enc(output), output_size, _enc(source_map), source_map_size)


BinaryenModuleWriteWithSourceMap = ModuleWriteWithSourceMap


def ModuleAllocateAndWrite(
    module: BinaryenModuleRef,
    source_map_url: str,
) -> BinaryenModuleAllocateAndWriteResult:
    """
    Serializes a module into binary form, optionally including its source map if
    sourceMapUrl has been specified. Uses the currently set global debugInfo
    option. Differs from BinaryenModuleWrite in that it implicitly allocates
    appropriate buffers using malloc(), and expects the user to free() them
    manually once not needed anymore.
    """
    return lib.BinaryenModuleAllocateAndWrite(module, _enc(source_map_url))


BinaryenModuleAllocateAndWrite = ModuleAllocateAndWrite


def ModuleAllocateAndWriteText(
    module: BinaryenModuleRef,
) -> str:
    """
    Serialize a module in s-expression form. Implicity allocates the returned
    char* with malloc(), and expects the user to free() them manually
    once not needed anymore.
    """
    return _dec(lib.BinaryenModuleAllocateAndWriteText(module))


BinaryenModuleAllocateAndWriteText = ModuleAllocateAndWriteText


def ModuleAllocateAndWriteStackIR(
    module: BinaryenModuleRef,
    optimize: bool,
) -> str:
    """
    Serialize a module in stack IR form. Implicitly allocates the returned
    char* with malloc(), and expects the user to free() them manually
    once not needed anymore.
    """
    return _dec(lib.BinaryenModuleAllocateAndWriteStackIR(module, optimize))


BinaryenModuleAllocateAndWriteStackIR = ModuleAllocateAndWriteStackIR


def ModuleRead(
    _input: bytes,
    input_size: int,
) -> BinaryenModuleRef:
    """ Deserialize a module from binary form. """
    return lib.BinaryenModuleRead(_input, input_size)


BinaryenModuleRead = ModuleRead


def ModuleInterpret(
    module: BinaryenModuleRef,
) -> None:
    """
    Execute a module in the Binaryen interpreter. This will create an instance of
    the module, run it in the interpreter - which means running the start method
    - and then destroying the instance.
    """
    lib.BinaryenModuleInterpret(module)


BinaryenModuleInterpret = ModuleInterpret


def ModuleAddDebugInfoFileName(
    module: BinaryenModuleRef,
    filename: str,
) -> BinaryenIndex:
    """ Adds a debug info file name to the module and returns its index. """
    return lib.BinaryenModuleAddDebugInfoFileName(module, _enc(filename))


BinaryenModuleAddDebugInfoFileName = ModuleAddDebugInfoFileName


def ModuleGetDebugInfoFileName(
    module: BinaryenModuleRef,
    index: BinaryenIndex,
) -> str:
    """
    Gets the name of the debug info file at the specified index. Returns `NULL`
    if it does not exist.
    """
    return _dec(lib.BinaryenModuleGetDebugInfoFileName(module, index))


BinaryenModuleGetDebugInfoFileName = ModuleGetDebugInfoFileName


def FunctionGetName(
    func: BinaryenFunctionRef,
) -> str:
    """ Gets the name of the specified `Function`. """
    return _dec(lib.BinaryenFunctionGetName(func))


BinaryenFunctionGetName = FunctionGetName


def FunctionGetParams(
    func: BinaryenFunctionRef,
) -> BinaryenType:
    """
    Gets the type of the parameter at the specified index of the specified
    `Function`.
    """
    return lib.BinaryenFunctionGetParams(func)


BinaryenFunctionGetParams = FunctionGetParams


def FunctionGetResults(
    func: BinaryenFunctionRef,
) -> BinaryenType:
    """ Gets the result type of the specified `Function`. """
    return lib.BinaryenFunctionGetResults(func)


BinaryenFunctionGetResults = FunctionGetResults


def FunctionGetNumVars(
    func: BinaryenFunctionRef,
) -> BinaryenIndex:
    """ Gets the number of additional locals within the specified `Function`. """
    return lib.BinaryenFunctionGetNumVars(func)


BinaryenFunctionGetNumVars = FunctionGetNumVars


def FunctionGetVar(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
) -> BinaryenType:
    """
    Gets the type of the additional local at the specified index within the
    specified `Function`.
    """
    return lib.BinaryenFunctionGetVar(func, index)


BinaryenFunctionGetVar = FunctionGetVar


def FunctionGetNumLocals(
    func: BinaryenFunctionRef,
) -> BinaryenIndex:
    """ Gets the number of locals within the specified function. Includes parameters. """
    return lib.BinaryenFunctionGetNumLocals(func)


BinaryenFunctionGetNumLocals = FunctionGetNumLocals


def FunctionHasLocalName(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
) -> bool:
    """ Tests if the local at the specified index has a name. """
    return lib.BinaryenFunctionHasLocalName(func, index)


BinaryenFunctionHasLocalName = FunctionHasLocalName


def FunctionGetLocalName(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
) -> str:
    """ Gets the name of the local at the specified index. """
    return _dec(lib.BinaryenFunctionGetLocalName(func, index))


BinaryenFunctionGetLocalName = FunctionGetLocalName


def FunctionSetLocalName(
    func: BinaryenFunctionRef,
    index: BinaryenIndex,
    name: str,
) -> None:
    """ Sets the name of the local at the specified index. """
    lib.BinaryenFunctionSetLocalName(func, index, _enc(name))


BinaryenFunctionSetLocalName = FunctionSetLocalName


def FunctionGetBody(
    func: BinaryenFunctionRef,
) -> BinaryenExpressionRef:
    """ Gets the body of the specified `Function`. """
    return lib.BinaryenFunctionGetBody(func)


BinaryenFunctionGetBody = FunctionGetBody


def FunctionSetBody(
    func: BinaryenFunctionRef,
    body: BinaryenExpressionRef,
) -> None:
    """ Sets the body of the specified `Function`. """
    lib.BinaryenFunctionSetBody(func, body)


BinaryenFunctionSetBody = FunctionSetBody


def FunctionOptimize(
    func: BinaryenFunctionRef,
    module: BinaryenModuleRef,
) -> None:
    """
    Runs the standard optimization passes on the function. Uses the currently set
    global optimize and shrink level.
    """
    lib.BinaryenFunctionOptimize(func, module)


BinaryenFunctionOptimize = FunctionOptimize


def FunctionRunPasses(
    func: BinaryenFunctionRef,
    module: BinaryenModuleRef,
    passes: List[str],
) -> None:
    """
    Runs the specified passes on the function. Uses the currently set global
    optimize and shrink level.
    """
    lib.BinaryenFunctionRunPasses(func, module, _enc_seq(passes), _len(passes))


BinaryenFunctionRunPasses = FunctionRunPasses


def FunctionSetDebugLocation(
    func: BinaryenFunctionRef,
    expr: BinaryenExpressionRef,
    file_index: BinaryenIndex,
    line_number: BinaryenIndex,
    column_number: BinaryenIndex,
) -> None:
    """
    Sets the debug location of the specified `Expression` within the specified
    `Function`.
    """
    lib.BinaryenFunctionSetDebugLocation(func, expr, file_index, line_number, column_number)


BinaryenFunctionSetDebugLocation = FunctionSetDebugLocation


def TableGetName(
    table: BinaryenTableRef,
) -> str:
    """ Gets the name of the specified `Table`. """
    return _dec(lib.BinaryenTableGetName(table))


BinaryenTableGetName = TableGetName


def TableSetName(
    table: BinaryenTableRef,
    name: str,
) -> None:
    """ Sets the name of the specified `Table`. """
    lib.BinaryenTableSetName(table, _enc(name))


BinaryenTableSetName = TableSetName


def TableGetInitial(
    table: BinaryenTableRef,
) -> BinaryenIndex:
    """ Gets the initial number of pages of the specified `Table`. """
    return lib.BinaryenTableGetInitial(table)


BinaryenTableGetInitial = TableGetInitial


def TableSetInitial(
    table: BinaryenTableRef,
    initial: BinaryenIndex,
) -> None:
    """ Sets the initial number of pages of the specified `Table`. """
    lib.BinaryenTableSetInitial(table, initial)


BinaryenTableSetInitial = TableSetInitial


def TableHasMax(
    table: BinaryenTableRef,
) -> bool:
    """ Tests whether the specified `Table` has a maximum number of pages. """
    return lib.BinaryenTableHasMax(table)


BinaryenTableHasMax = TableHasMax


def TableGetMax(
    table: BinaryenTableRef,
) -> BinaryenIndex:
    """ Gets the maximum number of pages of the specified `Table`. """
    return lib.BinaryenTableGetMax(table)


BinaryenTableGetMax = TableGetMax


def TableSetMax(
    table: BinaryenTableRef,
    _max: BinaryenIndex,
) -> None:
    """ Sets the maximum number of pages of the specified `Table`. """
    lib.BinaryenTableSetMax(table, _max)


BinaryenTableSetMax = TableSetMax


def ElementSegmentGetName(
    elem: BinaryenElementSegmentRef,
) -> str:
    """ Gets the name of the specified `ElementSegment`. """
    return _dec(lib.BinaryenElementSegmentGetName(elem))


BinaryenElementSegmentGetName = ElementSegmentGetName


def ElementSegmentSetName(
    elem: BinaryenElementSegmentRef,
    name: str,
) -> None:
    """ Sets the name of the specified `ElementSegment`. """
    lib.BinaryenElementSegmentSetName(elem, _enc(name))


BinaryenElementSegmentSetName = ElementSegmentSetName


def ElementSegmentGetTable(
    elem: BinaryenElementSegmentRef,
) -> str:
    """ Gets the table name of the specified `ElementSegment`. """
    return _dec(lib.BinaryenElementSegmentGetTable(elem))


BinaryenElementSegmentGetTable = ElementSegmentGetTable


def ElementSegmentSetTable(
    elem: BinaryenElementSegmentRef,
    table: str,
) -> None:
    """ Sets the table name of the specified `ElementSegment`. """
    lib.BinaryenElementSegmentSetTable(elem, _enc(table))


BinaryenElementSegmentSetTable = ElementSegmentSetTable


def ElementSegmentGetOffset(
    elem: BinaryenElementSegmentRef,
) -> BinaryenExpressionRef:
    """ Gets the segment offset in case of active segments """
    return lib.BinaryenElementSegmentGetOffset(elem)


BinaryenElementSegmentGetOffset = ElementSegmentGetOffset


def ElementSegmentGetLength(
    elem: BinaryenElementSegmentRef,
) -> BinaryenIndex:
    """ Gets the length of items in the segment """
    return lib.BinaryenElementSegmentGetLength(elem)


BinaryenElementSegmentGetLength = ElementSegmentGetLength


def ElementSegmentGetData(
    elem: BinaryenElementSegmentRef,
    data_id: BinaryenIndex,
) -> str:
    """ Gets the item at the specified index """
    return _dec(lib.BinaryenElementSegmentGetData(elem, data_id))


BinaryenElementSegmentGetData = ElementSegmentGetData


def ElementSegmentIsPassive(
    elem: BinaryenElementSegmentRef,
) -> bool:
    """ Returns true if the specified elem segment is passive """
    return lib.BinaryenElementSegmentIsPassive(elem)


BinaryenElementSegmentIsPassive = ElementSegmentIsPassive


def GlobalGetName(
    _global: BinaryenGlobalRef,
) -> str:
    """ Gets the name of the specified `Global`. """
    return _dec(lib.BinaryenGlobalGetName(_global))


BinaryenGlobalGetName = GlobalGetName


def GlobalGetType(
    _global: BinaryenGlobalRef,
) -> BinaryenType:
    """
    Gets the name of the `GlobalType` associated with the specified `Global`. May
    be `NULL` if the signature is implicit.
    """
    return lib.BinaryenGlobalGetType(_global)


BinaryenGlobalGetType = GlobalGetType


def GlobalIsMutable(
    _global: BinaryenGlobalRef,
) -> bool:
    """ Returns true if the specified `Global` is mutable. """
    return lib.BinaryenGlobalIsMutable(_global)


BinaryenGlobalIsMutable = GlobalIsMutable


def GlobalGetInitExpr(
    _global: BinaryenGlobalRef,
) -> BinaryenExpressionRef:
    """ Gets the initialization expression of the specified `Global`. """
    return lib.BinaryenGlobalGetInitExpr(_global)


BinaryenGlobalGetInitExpr = GlobalGetInitExpr


def TagGetName(
    tag: BinaryenTagRef,
) -> str:
    """ Gets the name of the specified `Tag`. """
    return _dec(lib.BinaryenTagGetName(tag))


BinaryenTagGetName = TagGetName


def TagGetParams(
    tag: BinaryenTagRef,
) -> BinaryenType:
    """ Gets the parameters type of the specified `Tag`. """
    return lib.BinaryenTagGetParams(tag)


BinaryenTagGetParams = TagGetParams


def TagGetResults(
    tag: BinaryenTagRef,
) -> BinaryenType:
    """ Gets the results type of the specified `Tag`. """
    return lib.BinaryenTagGetResults(tag)


BinaryenTagGetResults = TagGetResults


def FunctionImportGetModule(
    _import: BinaryenFunctionRef,
) -> str:
    """ Gets the external module name of the specified import. """
    return _dec(lib.BinaryenFunctionImportGetModule(_import))


BinaryenFunctionImportGetModule = FunctionImportGetModule


def TableImportGetModule(
    _import: BinaryenTableRef,
) -> str:
    return _dec(lib.BinaryenTableImportGetModule(_import))


BinaryenTableImportGetModule = TableImportGetModule


def GlobalImportGetModule(
    _import: BinaryenGlobalRef,
) -> str:
    return _dec(lib.BinaryenGlobalImportGetModule(_import))


BinaryenGlobalImportGetModule = GlobalImportGetModule


def TagImportGetModule(
    _import: BinaryenTagRef,
) -> str:
    return _dec(lib.BinaryenTagImportGetModule(_import))


BinaryenTagImportGetModule = TagImportGetModule


def FunctionImportGetBase(
    _import: BinaryenFunctionRef,
) -> str:
    """ Gets the external base name of the specified import. """
    return _dec(lib.BinaryenFunctionImportGetBase(_import))


BinaryenFunctionImportGetBase = FunctionImportGetBase


def TableImportGetBase(
    _import: BinaryenTableRef,
) -> str:
    return _dec(lib.BinaryenTableImportGetBase(_import))


BinaryenTableImportGetBase = TableImportGetBase


def GlobalImportGetBase(
    _import: BinaryenGlobalRef,
) -> str:
    return _dec(lib.BinaryenGlobalImportGetBase(_import))


BinaryenGlobalImportGetBase = GlobalImportGetBase


def TagImportGetBase(
    _import: BinaryenTagRef,
) -> str:
    return _dec(lib.BinaryenTagImportGetBase(_import))


BinaryenTagImportGetBase = TagImportGetBase


def ExportGetKind(
    export_: BinaryenExportRef,
) -> BinaryenExternalKind:
    """ Gets the external kind of the specified export. """
    return lib.BinaryenExportGetKind(export_)


BinaryenExportGetKind = ExportGetKind


def ExportGetName(
    export_: BinaryenExportRef,
) -> str:
    """ Gets the external name of the specified export. """
    return _dec(lib.BinaryenExportGetName(export_))


BinaryenExportGetName = ExportGetName


def ExportGetValue(
    export_: BinaryenExportRef,
) -> str:
    """ Gets the internal name of the specified export. """
    return _dec(lib.BinaryenExportGetValue(export_))


BinaryenExportGetValue = ExportGetValue


def AddCustomSection(
    module: BinaryenModuleRef,
    name: str,
    contents: str,
    contents_size: BinaryenIndex,
) -> None:
    lib.BinaryenAddCustomSection(module, _enc(name), _enc(contents), contents_size)


BinaryenAddCustomSection = AddCustomSection


def SideEffectNone() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectNone()


BinaryenSideEffectNone = SideEffectNone


def SideEffectBranches() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectBranches()


BinaryenSideEffectBranches = SideEffectBranches


def SideEffectCalls() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectCalls()


BinaryenSideEffectCalls = SideEffectCalls


def SideEffectReadsLocal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsLocal()


BinaryenSideEffectReadsLocal = SideEffectReadsLocal


def SideEffectWritesLocal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesLocal()


BinaryenSideEffectWritesLocal = SideEffectWritesLocal


def SideEffectReadsGlobal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsGlobal()


BinaryenSideEffectReadsGlobal = SideEffectReadsGlobal


def SideEffectWritesGlobal() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesGlobal()


BinaryenSideEffectWritesGlobal = SideEffectWritesGlobal


def SideEffectReadsMemory() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsMemory()


BinaryenSideEffectReadsMemory = SideEffectReadsMemory


def SideEffectWritesMemory() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesMemory()


BinaryenSideEffectWritesMemory = SideEffectWritesMemory


def SideEffectReadsTable() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectReadsTable()


BinaryenSideEffectReadsTable = SideEffectReadsTable


def SideEffectWritesTable() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectWritesTable()


BinaryenSideEffectWritesTable = SideEffectWritesTable


def SideEffectImplicitTrap() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectImplicitTrap()


BinaryenSideEffectImplicitTrap = SideEffectImplicitTrap


def SideEffectTrapsNeverHappen() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectTrapsNeverHappen()


BinaryenSideEffectTrapsNeverHappen = SideEffectTrapsNeverHappen


def SideEffectIsAtomic() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectIsAtomic()


BinaryenSideEffectIsAtomic = SideEffectIsAtomic


def SideEffectThrows() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectThrows()


BinaryenSideEffectThrows = SideEffectThrows


def SideEffectDanglingPop() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectDanglingPop()


BinaryenSideEffectDanglingPop = SideEffectDanglingPop


def SideEffectAny() -> BinaryenSideEffects:
    return lib.BinaryenSideEffectAny()


BinaryenSideEffectAny = SideEffectAny


def ExpressionGetSideEffects(
    expr: BinaryenExpressionRef,
    module: BinaryenModuleRef,
) -> BinaryenSideEffects:
    return lib.BinaryenExpressionGetSideEffects(expr, module)


BinaryenExpressionGetSideEffects = ExpressionGetSideEffects


def RelooperCreate(
    module: BinaryenModuleRef,
) -> RelooperRef:
    """ Create a relooper instance """
    return lib.RelooperCreate(module)


def RelooperAddBlock(
    relooper: RelooperRef,
    code: BinaryenExpressionRef,
) -> RelooperBlockRef:
    """ Create a basic block that ends with nothing, or with some simple branching """
    return lib.RelooperAddBlock(relooper, code)


def RelooperAddBranch(
    _from: RelooperBlockRef,
    to: RelooperBlockRef,
    condition: Optional[BinaryenExpressionRef],
    code: Optional[BinaryenExpressionRef],
) -> None:
    """
    Create a branch to another basic block
    The branch can have code on it, that is executed as the branch happens. this
    is useful for phis. otherwise, code can be NULL
    """
    lib.RelooperAddBranch(_from, to, _opt(condition), _opt(code))


def RelooperAddBlockWithSwitch(
    relooper: RelooperRef,
    code: BinaryenExpressionRef,
    condition: BinaryenExpressionRef,
) -> RelooperBlockRef:
    """ Create a basic block that ends a switch on a condition """
    return lib.RelooperAddBlockWithSwitch(relooper, code, condition)


def RelooperAddBranchForSwitch(
    _from: RelooperBlockRef,
    to: RelooperBlockRef,
    indexes: Optional[List[BinaryenIndex]],
    code: Optional[BinaryenExpressionRef],
) -> None:
    """
    Create a switch-style branch to another basic block. The block's switch table
    will have these indexes going to that target
    """
    lib.RelooperAddBranchForSwitch(_from, to, _opt_seq(indexes), _len(indexes), _opt(code))


def RelooperRenderAndDispose(
    relooper: RelooperRef,
    entry: RelooperBlockRef,
    label_helper: BinaryenIndex,
) -> BinaryenExpressionRef:
    """
    Generate structed wasm control flow from the CFG of blocks and branches that
    were created on this relooper instance. This returns the rendered output, and
    also disposes of the relooper and its blocks and branches, as they are no
    longer needed.
    @param labelHelper To render irreducible control flow, we may need a helper
    variable to guide us to the right target label. This value should be
    an index of an i32 local variable that is free for us to use.
    """
    return lib.RelooperRenderAndDispose(relooper, entry, label_helper)


def ExpressionRunnerFlagsDefault() -> ExpressionRunnerFlags:
    """
    By default, just evaluate the expression, i.e. all we want to know is whether
    it computes down to a concrete value, where it is not necessary to preserve
    side effects like those of a `local.tee`.
    """
    return lib.ExpressionRunnerFlagsDefault()


def ExpressionRunnerFlagsPreserveSideeffects() -> ExpressionRunnerFlags:
    """
    Be very careful to preserve any side effects. For example, if we are
    intending to replace the expression with a constant afterwards, even if we
    can technically evaluate down to a constant, we still cannot replace the
    expression if it also sets a local, which must be preserved in this scenario
    so subsequent code keeps functioning.
    """
    return lib.ExpressionRunnerFlagsPreserveSideeffects()


def ExpressionRunnerFlagsTraverseCalls() -> ExpressionRunnerFlags:
    """
    Traverse through function calls, attempting to compute their concrete value.
    Must not be used in function-parallel scenarios, where the called function
    might be concurrently modified, leading to undefined behavior. Traversing
    another function reuses all of this runner's flags.
    """
    return lib.ExpressionRunnerFlagsTraverseCalls()


def ExpressionRunnerCreate(
    module: BinaryenModuleRef,
    flags: ExpressionRunnerFlags,
    max_depth: BinaryenIndex,
    max_loop_iterations: BinaryenIndex,
) -> ExpressionRunnerRef:
    """ Creates an ExpressionRunner instance """
    return lib.ExpressionRunnerCreate(module, flags, max_depth, max_loop_iterations)


def ExpressionRunnerSetLocalValue(
    runner: ExpressionRunnerRef,
    index: BinaryenIndex,
    value: BinaryenExpressionRef,
) -> bool:
    """
    Sets a known local value to use. Order matters if expressions have side
    effects. For example, if the expression also sets a local, this side effect
    will also happen (not affected by any flags). Returns `true` if the
    expression actually evaluates to a constant.
    """
    return lib.ExpressionRunnerSetLocalValue(runner, index, value)


def ExpressionRunnerSetGlobalValue(
    runner: ExpressionRunnerRef,
    name: str,
    value: BinaryenExpressionRef,
) -> bool:
    """
    Sets a known global value to use. Order matters if expressions have side
    effects. For example, if the expression also sets a local, this side effect
    will also happen (not affected by any flags). Returns `true` if the
    expression actually evaluates to a constant.
    """
    return lib.ExpressionRunnerSetGlobalValue(runner, _enc(name), value)


def ExpressionRunnerRunAndDispose(
    runner: ExpressionRunnerRef,
    expr: BinaryenExpressionRef,
) -> BinaryenExpressionRef:
    """
    Runs the expression and returns the constant value expression it evaluates
    to, if any. Otherwise returns `NULL`. Also disposes the runner.
    """
    return lib.ExpressionRunnerRunAndDispose(runner, expr)


def TypeBuilderErrorReasonSelfSupertype() -> TypeBuilderErrorReason:
    """ Indicates a cycle in the supertype relation. """
    return lib.TypeBuilderErrorReasonSelfSupertype()


def TypeBuilderErrorReasonInvalidSupertype() -> TypeBuilderErrorReason:
    """ Indicates that the declared supertype of a type is invalid. """
    return lib.TypeBuilderErrorReasonInvalidSupertype()


def TypeBuilderErrorReasonForwardSupertypeReference() -> TypeBuilderErrorReason:
    """ Indicates that the declared supertype is an invalid forward reference. """
    return lib.TypeBuilderErrorReasonForwardSupertypeReference()


def TypeBuilderErrorReasonForwardChildReference() -> TypeBuilderErrorReason:
    """ Indicates that a child of a type is an invalid forward reference. """
    return lib.TypeBuilderErrorReasonForwardChildReference()


def TypeBuilderCreate(
    size: BinaryenIndex,
) -> TypeBuilderRef:
    """
    Constructs a new type builder that allows for the construction of recursive
    types. Contains a table of `size` mutable heap types.
    """
    return lib.TypeBuilderCreate(size)


def TypeBuilderGrow(
    builder: TypeBuilderRef,
    count: BinaryenIndex,
) -> None:
    """ Grows the backing table of the type builder by `count` slots. """
    lib.TypeBuilderGrow(builder, count)


def TypeBuilderGetSize(
    builder: TypeBuilderRef,
) -> BinaryenIndex:
    """ Gets the size of the backing table of the type builder. """
    return lib.TypeBuilderGetSize(builder)


def TypeBuilderSetBasicHeapType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    basic_heap_type: BinaryenBasicHeapType,
) -> None:
    """
    Sets the heap type at index `index` to a basic heap type. Must not be used in
    nominal mode.
    """
    lib.TypeBuilderSetBasicHeapType(builder, index, basic_heap_type)


def TypeBuilderSetSignatureType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    param_types: BinaryenType,
    result_types: BinaryenType,
) -> None:
    """
    Sets the heap type at index `index` to a concrete signature type. Expects
    temporary tuple types if multiple parameter and/or result types include
    temporary types.
    """
    lib.TypeBuilderSetSignatureType(builder, index, param_types, result_types)


def TypeBuilderSetStructType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    field_types: List[BinaryenType],
    field_packed_types: List[BinaryenPackedType],
    field_mutables: List[bool],
) -> None:
    """ Sets the heap type at index `index` to a concrete struct type. """
    lib.TypeBuilderSetStructType(builder, index, field_types, field_packed_types, field_mutables, _len(field_mutables))


def TypeBuilderSetArrayType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    element_type: BinaryenType,
    element_packed_type: BinaryenPackedType,
    element_mutable: int,
) -> None:
    """ Sets the heap type at index `index` to a concrete array type. """
    lib.TypeBuilderSetArrayType(builder, index, element_type, element_packed_type, element_mutable)


def TypeBuilderIsBasic(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
) -> bool:
    """ Tests if the heap type at index `index` is a basic heap type. """
    return lib.TypeBuilderIsBasic(builder, index)


def TypeBuilderGetBasic(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
) -> BinaryenBasicHeapType:
    """ Gets the basic heap type at index `index`. """
    return lib.TypeBuilderGetBasic(builder, index)


def TypeBuilderGetTempHeapType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
) -> BinaryenHeapType:
    """
    Gets the temporary heap type to use at index `index`. Temporary heap types
    may only be used to construct temporary types using the type builder.
    """
    return lib.TypeBuilderGetTempHeapType(builder, index)


def TypeBuilderGetTempTupleType(
    builder: TypeBuilderRef,
    types: List[BinaryenType],
) -> BinaryenType:
    """ Gets a temporary tuple type for use with and owned by the type builder. """
    return lib.TypeBuilderGetTempTupleType(builder, types, _len(types))


def TypeBuilderGetTempRefType(
    builder: TypeBuilderRef,
    heap_type: BinaryenHeapType,
    nullable: int,
) -> BinaryenType:
    """ Gets a temporary reference type for use with and owned by the type builder. """
    return lib.TypeBuilderGetTempRefType(builder, heap_type, nullable)


def TypeBuilderSetSubType(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    super_type: BinaryenHeapType,
) -> None:
    """ Sets the type at `index` to be a subtype of the given super type. """
    lib.TypeBuilderSetSubType(builder, index, super_type)


def TypeBuilderCreateRecGroup(
    builder: TypeBuilderRef,
    index: BinaryenIndex,
    length: BinaryenIndex,
) -> None:
    """
    Creates a new recursion group in the range `index` inclusive to `index +
    length` exclusive. Recursion groups must not overlap.
    """
    lib.TypeBuilderCreateRecGroup(builder, index, length)


def TypeBuilderBuildAndDispose(
    builder: TypeBuilderRef,
    heap_types: List[BinaryenHeapType],
) -> Tuple[bool, BinaryenIndex, TypeBuilderErrorReason]:
    """
    Builds the heap type hierarchy and disposes the builder. Returns `false` and
    populates `errorIndex` and `errorReason` on failure.
    """
    dim = lib.TypeBuilderGetSize(builder)
    _error_index = ffi.new('BinaryenIndex*')
    _error_reason = ffi.new('TypeBuilderErrorReason*')
    _heap_types = ffi.new(f'BinaryenHeapType[{dim}]')
    result = lib.TypeBuilderBuildAndDispose(builder, _heap_types, _error_index, _error_reason)
    heap_types[:] = _heap_types
    return (
        result,
        ffi.cast(ffi.typeof('uint32_t *'), _error_index)[0],
        ffi.cast(ffi.typeof('uint32_t *'), _error_reason)[0]
    )


def ModuleSetTypeName(
    module: BinaryenModuleRef,
    heap_type: BinaryenHeapType,
    name: str,
) -> None:
    """
    Sets the textual name of a compound `heapType`. Has no effect if the type
    already has a canonical name.
    """
    lib.BinaryenModuleSetTypeName(module, heap_type, _enc(name))


BinaryenModuleSetTypeName = ModuleSetTypeName


def ModuleSetFieldName(
    module: BinaryenModuleRef,
    heap_type: BinaryenHeapType,
    index: BinaryenIndex,
    name: str,
) -> None:
    """ Sets the field name of a struct `heapType` at index `index`. """
    lib.BinaryenModuleSetFieldName(module, heap_type, index, _enc(name))


BinaryenModuleSetFieldName = ModuleSetFieldName


def SetColorsEnabled(
    enabled: bool,
) -> None:
    """ Enable or disable coloring for the Wasm printer """
    lib.BinaryenSetColorsEnabled(enabled)


BinaryenSetColorsEnabled = SetColorsEnabled


def AreColorsEnabled() -> bool:
    """ Query whether color is enable for the Wasm printer """
    return lib.BinaryenAreColorsEnabled()


BinaryenAreColorsEnabled = AreColorsEnabled
