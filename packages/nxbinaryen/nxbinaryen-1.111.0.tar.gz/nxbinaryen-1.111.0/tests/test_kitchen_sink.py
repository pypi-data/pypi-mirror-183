# Manually curated port of binaryen/test/example/c-api-kitchen-sink.c (49fb2e23bb3c932389f23fdda33a32d034ca9a0c)
# https://github.com/WebAssembly/binaryen/blob/49fb2e23bb3c932389f23fdda33a32d034ca9a0c/test/example/c-api-kitchen-sink.c

import sys

from nxbinaryen.capi import *


# TODO: Redirect all prints (including stdout from libbinaryen) to kitchen_sink.txt,
#  so we can compare it w/ original c-kitchen-sink.txt from the same release (critical)
def printf(fmt: str, *values):
    fmt = fmt.replace('%zd', '%d').replace('\n', '')
    print(fmt % values)


puts = print


def abort():
    sys.exit(1)


# -------- c-api-kitchen-sink.c --------

v128_bytes = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])


def makeUnary(module: BinaryenModuleRef, op: BinaryenOp, inputType: BinaryenType) -> BinaryenExpressionRef:
    if inputType == BinaryenTypeInt32():
        return BinaryenUnary(
            module, op, BinaryenConst(module, BinaryenLiteralInt32(-10)))
    if inputType == BinaryenTypeInt64():
        return BinaryenUnary(
            module, op, BinaryenConst(module, BinaryenLiteralInt64(-22)))
    if inputType == BinaryenTypeFloat32():
        return BinaryenUnary(
            module, op, BinaryenConst(module, BinaryenLiteralFloat32(-33.612)))  # -33.612f
    if inputType == BinaryenTypeFloat64():
        return BinaryenUnary(
            module, op, BinaryenConst(module, BinaryenLiteralFloat64(-9005.841)))
    if inputType == BinaryenTypeVec128():
        return BinaryenUnary(
            module, op, BinaryenConst(module, BinaryenLiteralVec128(v128_bytes)))

    abort()


def makeBinary(module: BinaryenModuleRef, op: BinaryenOp, type: BinaryenType) -> BinaryenExpressionRef:
    if type == BinaryenTypeInt32():
        # use temp vars to ensure optimization doesn't change the order of
        # operation in our trace recording
        temp = BinaryenConst(module, BinaryenLiteralInt32(-11))
        return BinaryenBinary(
            module, op, BinaryenConst(module, BinaryenLiteralInt32(-10)), temp)

    if type == BinaryenTypeInt64():
        temp = BinaryenConst(module, BinaryenLiteralInt64(-23))
        return BinaryenBinary(
            module, op, BinaryenConst(module, BinaryenLiteralInt64(-22)), temp)

    if type == BinaryenTypeFloat32():
        temp = BinaryenConst(module, BinaryenLiteralFloat32(-62.5))  # -62.5f
        return BinaryenBinary(
            module,
            op,
            BinaryenConst(module, BinaryenLiteralFloat32(-33.612)),  # -33.612f
            temp)

    if type == BinaryenTypeFloat64():
        temp = BinaryenConst(module, BinaryenLiteralFloat64(-9007.333))
        return BinaryenBinary(
            module,
            op,
            BinaryenConst(module, BinaryenLiteralFloat64(-9005.841)),
            temp)

    if type == BinaryenTypeVec128():
        temp = BinaryenConst(module, BinaryenLiteralVec128(v128_bytes))
        return BinaryenBinary(
            module,
            op,
            BinaryenConst(module, BinaryenLiteralVec128(v128_bytes)),
            temp)

    abort()


def makeInt32(module: BinaryenModuleRef, x: int) -> BinaryenExpressionRef:
    return BinaryenConst(module, BinaryenLiteralInt32(x))


def makeFloat32(module: BinaryenModuleRef, x: float) -> BinaryenExpressionRef:
    return BinaryenConst(module, BinaryenLiteralFloat32(x))


def makeInt64(module: BinaryenModuleRef, x: int) -> BinaryenExpressionRef:
    return BinaryenConst(module, BinaryenLiteralInt64(x))


def makeFloat64(module: BinaryenModuleRef, x: float) -> BinaryenExpressionRef:  # double
    return BinaryenConst(module, BinaryenLiteralFloat64(x))


def makeVec128(module: BinaryenModuleRef, bytes: bytes) -> BinaryenExpressionRef:  # int8_t const*
    return BinaryenConst(module, BinaryenLiteralVec128(bytes))


def makeSomething(module: BinaryenModuleRef) -> BinaryenExpressionRef:
    return makeInt32(module, 1337)


def makeDroppedInt32(module: BinaryenModuleRef, x: int) -> BinaryenExpressionRef:
    return BinaryenDrop(module, BinaryenConst(module, BinaryenLiteralInt32(x)))


def makeSIMDExtract(module: BinaryenModuleRef, op: BinaryenOp) -> BinaryenExpressionRef:
    return BinaryenSIMDExtract(module, op, makeVec128(module, v128_bytes), 0)


def makeSIMDReplace(module: BinaryenModuleRef, op: BinaryenOp, type: BinaryenType) -> BinaryenExpressionRef:
    val = None
    if type == BinaryenTypeInt32():
        val = makeInt32(module, 42)

    if type == BinaryenTypeInt64():
        val = makeInt64(module, 42)

    if type == BinaryenTypeFloat32():
        val = makeFloat32(module, 42.)

    if type == BinaryenTypeFloat64():
        val = makeFloat64(module, 42.)

    if not val:
        abort()

    return BinaryenSIMDReplace(
        module, op, makeVec128(module, v128_bytes), 0, val)


def makeSIMDShuffle(module: BinaryenModuleRef) -> BinaryenExpressionRef:
    left = makeVec128(module, v128_bytes)
    right = makeVec128(module, v128_bytes)
    return BinaryenSIMDShuffle(module, left, right, bytes([0] * 16))  # (uint8_t[16])


def makeSIMDTernary(module: BinaryenModuleRef, op: BinaryenOp) -> BinaryenExpressionRef:
    a = makeVec128(module, v128_bytes)
    b = makeVec128(module, v128_bytes)
    c = makeVec128(module, v128_bytes)
    return BinaryenSIMDTernary(module, op, a, b, c)


def makeSIMDShift(module: BinaryenModuleRef, op: BinaryenOp) -> BinaryenExpressionRef:
    vec = makeVec128(module, v128_bytes)
    return BinaryenSIMDShift(module, op, vec, makeInt32(module, 1))


def makeMemoryInit(module: BinaryenModuleRef) -> BinaryenExpressionRef:
    dest = makeInt32(module, 1024)
    offset = makeInt32(module, 0)
    size = makeInt32(module, 12)
    return BinaryenMemoryInit(module, 0, dest, offset, size, '0')


def makeDataDrop(module: BinaryenModuleRef) -> BinaryenExpressionRef:
    return BinaryenDataDrop(module, 0)


def makeMemoryCopy(module: BinaryenModuleRef) -> BinaryenExpressionRef:
    dest = makeInt32(module, 2048)
    source = makeInt32(module, 1024)
    size = makeInt32(module, 12)
    return BinaryenMemoryCopy(module, dest, source, size, '0', '0')


def makeMemoryFill(module: BinaryenModuleRef) -> BinaryenExpressionRef:
    dest = makeInt32(module, 0)
    value = makeInt32(module, 42)
    size = makeInt32(module, 1024)
    return BinaryenMemoryFill(module, dest, value, size, '0')


# tests

def test_types():
    valueType: BinaryenType = 0xdeadbeef

    none: BinaryenType = BinaryenTypeNone()
    printf('BinaryenTypeNone: %zd\n', none)
    assert (BinaryenTypeArity(none) == 0)
    valueType = BinaryenTypeExpand(none)
    assert (not valueType)

    unreachable: BinaryenType = BinaryenTypeUnreachable()
    printf('BinaryenTypeUnreachable: %zd\n', unreachable)
    assert (BinaryenTypeArity(unreachable) == 1)
    valueType = BinaryenTypeExpand(unreachable)
    assert (valueType[0] == unreachable)

    i32: BinaryenType = BinaryenTypeInt32()
    printf('BinaryenTypeInt32: %zd\n', i32)
    assert (BinaryenTypeArity(i32) == 1)
    valueType = BinaryenTypeExpand(i32)
    assert (valueType[0] == i32)

    i64: BinaryenType = BinaryenTypeInt64()
    printf('BinaryenTypeInt64: %zd\n', i64)
    assert (BinaryenTypeArity(i64) == 1)
    valueType = BinaryenTypeExpand(i64)
    assert (valueType[0] == i64)

    f32: BinaryenType = BinaryenTypeFloat32()
    printf('BinaryenTypeFloat32: %zd\n', f32)
    assert (BinaryenTypeArity(f32) == 1)
    valueType = BinaryenTypeExpand(f32)
    assert (valueType[0] == f32)

    f64 = BinaryenTypeFloat64()
    printf('BinaryenTypeFloat64: %zd\n', f64)
    assert (BinaryenTypeArity(f64) == 1)
    valueType = BinaryenTypeExpand(f64)
    assert (valueType[0] == f64)

    v128 = BinaryenTypeVec128()
    printf('BinaryenTypeVec128: %zd\n', v128)
    assert (BinaryenTypeArity(v128) == 1)
    valueType = BinaryenTypeExpand(v128)
    assert (valueType[0] == v128)

    funcref = BinaryenTypeFuncref()
    printf('BinaryenTypeFuncref: (ptr)\n')
    assert (funcref == BinaryenTypeFuncref())
    assert (BinaryenTypeArity(funcref) == 1)
    valueType = BinaryenTypeExpand(funcref)
    assert (valueType[0] == funcref)

    externref = BinaryenTypeExternref()
    printf('BinaryenTypeExternref: (ptr)\n')
    assert (externref == BinaryenTypeExternref())
    assert (BinaryenTypeArity(externref) == 1)
    valueType = BinaryenTypeExpand(externref)
    assert (valueType[0] == externref)

    anyref = BinaryenTypeAnyref()
    printf('BinaryenTypeAnyref: (ptr)\n')
    assert (anyref == BinaryenTypeAnyref())
    assert (BinaryenTypeArity(anyref) == 1)
    valueType = BinaryenTypeExpand(anyref)
    assert (valueType[0] == anyref)

    eqref = BinaryenTypeEqref()
    printf('BinaryenTypeEqref: (ptr)\n')
    assert (eqref == BinaryenTypeEqref())
    assert (BinaryenTypeArity(eqref) == 1)
    valueType = BinaryenTypeExpand(eqref)
    assert (valueType[0] == eqref)

    i31ref = BinaryenTypeI31ref()
    printf('BinaryenTypeI31ref: (ptr)\n')
    assert (i31ref == BinaryenTypeI31ref())
    assert (BinaryenTypeArity(i31ref) == 1)
    valueType = BinaryenTypeExpand(i31ref)
    assert (valueType[0] == i31ref)

    dataref = BinaryenTypeDataref()
    printf('BinaryenTypeDataref: (ptr)\n')
    assert (dataref == BinaryenTypeDataref())
    assert (BinaryenTypeArity(dataref) == 1)
    valueType = BinaryenTypeExpand(dataref)
    assert (valueType[0] == dataref)

    arrayref = BinaryenTypeArrayref()
    printf('BinaryenTypeArrayref: (ptr)\n')
    assert (arrayref == BinaryenTypeArrayref())
    assert (BinaryenTypeArity(arrayref) == 1)
    valueType = BinaryenTypeExpand(arrayref)
    assert (valueType[0] == arrayref)

    stringref = BinaryenTypeStringref()
    printf('BinaryenTypeStringref: (ptr)\n')
    assert (BinaryenTypeArity(stringref) == 1)
    valueType = BinaryenTypeExpand(stringref)
    assert (valueType[0] == stringref)

    stringview_wtf8_ = BinaryenTypeStringviewWTF8()
    printf('BinaryenTypeStringviewWTF8: (ptr)\n')
    assert (BinaryenTypeArity(stringview_wtf8_) == 1)
    valueType = BinaryenTypeExpand(stringview_wtf8_)
    assert (valueType[0] == stringview_wtf8_)

    stringview_wtf16_ = BinaryenTypeStringviewWTF16()
    printf('BinaryenTypeStringviewWTF16: (ptr)\n')
    assert (BinaryenTypeArity(stringview_wtf16_) == 1)
    valueType = BinaryenTypeExpand(stringview_wtf16_)
    assert (valueType[0] == stringview_wtf16_)

    stringview_iter_ = BinaryenTypeStringviewIter()
    printf('BinaryenTypeStringviewIter: (ptr)\n')
    assert (BinaryenTypeArity(stringview_iter_) == 1)
    valueType = BinaryenTypeExpand(stringview_iter_)
    assert (valueType[0] == stringview_iter_)

    nullref = BinaryenTypeNullref()
    printf('BinaryenTypeNullref: (ptr)\n')
    assert (BinaryenTypeArity(nullref) == 1)
    valueType = BinaryenTypeExpand(nullref)
    assert (valueType[0] == nullref)

    nullexternref = BinaryenTypeNullExternref()
    printf('BinaryenTypeNullExternref: (ptr)\n')
    assert (BinaryenTypeArity(nullexternref) == 1)
    valueType = BinaryenTypeExpand(nullexternref)
    assert (valueType[0] == nullexternref)

    nullfuncref = BinaryenTypeNullFuncref()
    printf('BinaryenTypeNullFuncref: (ptr)\n')
    assert (BinaryenTypeArity(nullfuncref) == 1)
    valueType = BinaryenTypeExpand(nullfuncref)
    assert (valueType[0] == nullfuncref)

    printf('BinaryenTypeAuto: %zd\n', BinaryenTypeAuto())

    pair = [i32, i32]

    i32_pair = BinaryenTypeCreate(pair)
    assert (BinaryenTypeArity(i32_pair) == 2)
    pair = BinaryenTypeExpand(i32_pair)
    assert (pair[0] == i32 and pair[1] == i32)

    duplicate_pair = BinaryenTypeCreate(pair)
    assert (duplicate_pair == i32_pair)

    pair[0] = pair[1] = f32
    float_pair = BinaryenTypeCreate(pair)
    assert (float_pair != i32_pair)

    notPacked = BinaryenPackedTypeNotPacked()
    printf('BinaryenPackedTypeNotPacked: %d\n', notPacked)
    i8 = BinaryenPackedTypeInt8()
    printf('BinaryenPackedTypeInt8: %d\n', i8)
    i16 = BinaryenPackedTypeInt16()
    printf('BinaryenPackedTypeInt16: %d\n', i16)

    printf('BinaryenHeapTypeExt: %zd\n', BinaryenHeapTypeExt())
    printf('BinaryenHeapTypeFunc: %zd\n', BinaryenHeapTypeFunc())
    printf('BinaryenHeapTypeAny: %zd\n', BinaryenHeapTypeAny())
    printf('BinaryenHeapTypeEq: %zd\n', BinaryenHeapTypeEq())
    printf('BinaryenHeapTypeI31: %zd\n', BinaryenHeapTypeI31())
    printf('BinaryenHeapTypeData: %zd\n', BinaryenHeapTypeData())
    printf('BinaryenHeapTypeArray: %zd\n', BinaryenHeapTypeArray())
    printf('BinaryenHeapTypeString: %zd\n', BinaryenHeapTypeString())
    printf('BinaryenHeapTypeStringviewWTF8: %zd\n',
           BinaryenHeapTypeStringviewWTF8())
    printf('BinaryenHeapTypeStringviewWTF16: %zd\n',
           BinaryenHeapTypeStringviewWTF16())
    printf('BinaryenHeapTypeStringviewIter: %zd\n',
           BinaryenHeapTypeStringviewIter())
    printf('BinaryenHeapTypeNone: %zd\n', BinaryenHeapTypeNone())
    printf('BinaryenHeapTypeNoext: %zd\n', BinaryenHeapTypeNoext())
    printf('BinaryenHeapTypeNofunc: %zd\n', BinaryenHeapTypeNofunc())

    assert (not BinaryenHeapTypeIsBottom(BinaryenHeapTypeExt()))
    assert (BinaryenHeapTypeIsBottom(BinaryenHeapTypeNoext()))
    assert (BinaryenHeapTypeGetBottom(BinaryenHeapTypeExt()) ==
            BinaryenHeapTypeNoext())

    eq = BinaryenTypeGetHeapType(eqref)
    assert (eq == BinaryenHeapTypeEq())
    ref_null_eq = BinaryenTypeFromHeapType(eq, True)
    assert (BinaryenTypeGetHeapType(ref_null_eq) == eq)
    assert (BinaryenTypeIsNullable(ref_null_eq))
    ref_eq = BinaryenTypeFromHeapType(eq, False)
    assert (ref_eq != ref_null_eq)
    assert (BinaryenTypeGetHeapType(ref_eq) == eq)
    assert (not BinaryenTypeIsNullable(ref_eq))


def test_features():
    printf('BinaryenFeatureMVP: %d\n', BinaryenFeatureMVP())
    printf('BinaryenFeatureAtomics: %d\n', BinaryenFeatureAtomics())
    printf('BinaryenFeatureBulkMemory: %d\n', BinaryenFeatureBulkMemory())
    printf('BinaryenFeatureMutableGlobals: %d\n',
           BinaryenFeatureMutableGlobals())
    printf('BinaryenFeatureNontrappingFPToInt: %d\n',
           BinaryenFeatureNontrappingFPToInt())
    printf('BinaryenFeatureSignExt: %d\n', BinaryenFeatureSignExt())
    printf('BinaryenFeatureSIMD128: %d\n', BinaryenFeatureSIMD128())
    printf('BinaryenFeatureExceptionHandling: %d\n',
           BinaryenFeatureExceptionHandling())
    printf('BinaryenFeatureTailCall: %d\n', BinaryenFeatureTailCall())
    printf('BinaryenFeatureReferenceTypes: %d\n',
           BinaryenFeatureReferenceTypes())
    printf('BinaryenFeatureMultivalue: %d\n', BinaryenFeatureMultivalue())
    printf('BinaryenFeatureGC: %d\n', BinaryenFeatureGC())
    printf('BinaryenFeatureMemory64: %d\n', BinaryenFeatureMemory64())
    printf('BinaryenFeatureRelaxedSIMD: %d\n', BinaryenFeatureRelaxedSIMD())
    printf('BinaryenFeatureExtendedConst: %d\n', BinaryenFeatureExtendedConst())
    printf('BinaryenFeatureStrings: %d\n', BinaryenFeatureStrings())
    printf('BinaryenFeatureAll: %d\n', BinaryenFeatureAll())


def test_core():
    # Module creation
    module = BinaryenModuleCreate()

    # Literals and consts
    constI32 = BinaryenConst(module, BinaryenLiteralInt32(1))
    constI64 = BinaryenConst(module, BinaryenLiteralInt64(2))
    constF32 = BinaryenConst(module, BinaryenLiteralFloat32(3.14))
    constF64 = BinaryenConst(module, BinaryenLiteralFloat64(2.1828))
    # TODO: constF32Bits = BinaryenConst(module, BinaryenLiteralFloat32Bits(0xffff1234))            # smth w/ overflow
    # TODO: constF64Bits = BinaryenConst(module, BinaryenLiteralFloat64Bits(0xffff12345678abcdLL))  # smth w/ overflow
    constV128 = BinaryenConst(module, BinaryenLiteralVec128(v128_bytes))

    switchValueNames = ['the-value']
    switchBodyNames = ['the-nothing']

    callOperands2 = [makeInt32(module, 13), makeFloat64(module, 3.7)]
    callOperands4 = [
        makeInt32(module, 13),
        makeInt64(module, 37),
        makeFloat32(module, 1.3),  # 1.3f
        makeFloat64(module, 3.7),
    ]
    callOperands4b = [
        makeInt32(module, 13),
        makeInt64(module, 37),
        makeFloat32(module, 1.3),  # 1.3f
        makeFloat64(module, 3.7)
    ]
    tupleElements4a = [
        makeInt32(module, 13),
        makeInt64(module, 37),
        makeFloat32(module, 1.3),  # 1.3f
        makeFloat64(module, 3.7)
    ]
    tupleElements4b = [
        makeInt32(module, 13),
        makeInt64(module, 37),
        makeFloat32(module, 1.3),  # 1.3f
        makeFloat64(module, 3.7)
    ]
    iIfF_ = [
        BinaryenTypeInt32(),
        BinaryenTypeInt64(),
        BinaryenTypeFloat32(),
        BinaryenTypeFloat64()
    ]
    iIfF = BinaryenTypeCreate(iIfF_)

    temp1 = makeInt32(module, 1)
    temp2 = makeInt32(module, 2)
    temp3 = makeInt32(module, 3)
    temp4 = makeInt32(module, 4)
    temp5 = makeInt32(module, 5)
    temp6 = makeInt32(module, 0)
    temp7 = makeInt32(module, 1)
    temp8 = makeInt32(module, 0)
    temp9 = makeInt32(module, 1)
    temp10 = makeInt32(module, 1)
    temp11 = makeInt32(module, 3)
    temp12 = makeInt32(module, 5)
    temp13 = makeInt32(module, 10)
    temp14 = makeInt32(module, 11)
    temp15 = makeInt32(module, 110)
    temp16 = makeInt64(module, 111)

    externrefExpr = BinaryenRefNull(module, BinaryenTypeNullExternref())
    funcrefExpr = BinaryenRefNull(module, BinaryenTypeNullFuncref())
    funcrefExpr = BinaryenRefFunc(module, 'kitchen()sinker', BinaryenTypeFuncref())
    i31refExpr = BinaryenI31New(module, makeInt32(module, 1))

    # Tags
    BinaryenAddTag(module, 'a-tag', BinaryenTypeInt32(), BinaryenTypeNone())
    BinaryenAddTable(module, 'tab', 0, 100, BinaryenTypeFuncref())

    # Exception handling
    # (try
    #   (do
    #     (throw $a-tag (i32.const 0))
    #   )
    #   (catch $a-tag
    #     (drop (i32 pop))
    #   )
    #   (catch_all)
    # )
    tryBody = BinaryenThrow(
        module, 'a-tag', [makeInt32(module, 0)])
    catchBody = BinaryenDrop(module, BinaryenPop(module, BinaryenTypeInt32()))
    catchAllBody = BinaryenNop(module)
    catchTags = ['a-tag']
    catchBodies = [catchBody, catchAllBody]
    emptyCatchTags = []
    emptyCatchBodies = []
    nopCatchBody = [BinaryenNop(module)]

    i32 = BinaryenTypeInt32()
    i64 = BinaryenTypeInt64()
    f32 = BinaryenTypeFloat32()
    f64 = BinaryenTypeFloat64()
    v128 = BinaryenTypeVec128()
    # i8Array
    # i16Array
    # i32Struct

    tb = TypeBuilderCreate(3)
    TypeBuilderSetArrayType(
        tb, 0, BinaryenTypeInt32(), BinaryenPackedTypeInt8(), True)
    TypeBuilderSetArrayType(
        tb, 1, BinaryenTypeInt32(), BinaryenPackedTypeInt16(), True)
    TypeBuilderSetStructType(
        tb,
        2,
        [BinaryenTypeInt32()],
        [BinaryenPackedTypeNotPacked()],
        [True])

    result, errorIndex, errorReason = TypeBuilderBuildAndDispose(tb, builtHeapTypes := [])
    i8Array = BinaryenTypeFromHeapType(builtHeapTypes[0], True)
    i16Array = BinaryenTypeFromHeapType(builtHeapTypes[1], True)
    i32Struct = BinaryenTypeFromHeapType(builtHeapTypes[2], True)

    # Memory. Add it before creating any memory-using instructions.

    segments = [b'hello, world', b'I am passive']
    segmentPassive = [False, True]
    segmentOffsets = [
        BinaryenConst(module, BinaryenLiteralInt32(10)), None
    ]
    segmentSizes = [12, 12]
    BinaryenSetMemory(module,
                      1,
                      256,
                      'mem',
                      segments,
                      segmentPassive,
                      segmentOffsets,
                      segmentSizes,
                      True,
                      False,
                      '0')

    valueList = [
        # Unary
        makeUnary(module, BinaryenClzInt32(), i32),
        makeUnary(module, BinaryenCtzInt64(), i64),
        makeUnary(module, BinaryenPopcntInt32(), i32),
        makeUnary(module, BinaryenNegFloat32(), f32),
        makeUnary(module, BinaryenAbsFloat64(), f64),
        makeUnary(module, BinaryenCeilFloat32(), f32),
        makeUnary(module, BinaryenFloorFloat64(), f64),
        makeUnary(module, BinaryenTruncFloat32(), f32),
        makeUnary(module, BinaryenNearestFloat32(), f32),
        makeUnary(module, BinaryenSqrtFloat64(), f64),
        makeUnary(module, BinaryenEqZInt32(), i32),
        makeUnary(module, BinaryenExtendSInt32(), i32),
        makeUnary(module, BinaryenExtendUInt32(), i32),
        makeUnary(module, BinaryenWrapInt64(), i64),
        makeUnary(module, BinaryenTruncSFloat32ToInt32(), f32),
        makeUnary(module, BinaryenTruncSFloat32ToInt64(), f32),
        makeUnary(module, BinaryenTruncUFloat32ToInt32(), f32),
        makeUnary(module, BinaryenTruncUFloat32ToInt64(), f32),
        makeUnary(module, BinaryenTruncSFloat64ToInt32(), f64),
        makeUnary(module, BinaryenTruncSFloat64ToInt64(), f64),
        makeUnary(module, BinaryenTruncUFloat64ToInt32(), f64),
        makeUnary(module, BinaryenTruncUFloat64ToInt64(), f64),
        makeUnary(module, BinaryenTruncSatSFloat32ToInt32(), f32),
        makeUnary(module, BinaryenTruncSatSFloat32ToInt64(), f32),
        makeUnary(module, BinaryenTruncSatUFloat32ToInt32(), f32),
        makeUnary(module, BinaryenTruncSatUFloat32ToInt64(), f32),
        makeUnary(module, BinaryenTruncSatSFloat64ToInt32(), f64),
        makeUnary(module, BinaryenTruncSatSFloat64ToInt64(), f64),
        makeUnary(module, BinaryenTruncSatUFloat64ToInt32(), f64),
        makeUnary(module, BinaryenTruncSatUFloat64ToInt64(), f64),
        makeUnary(module, BinaryenReinterpretFloat32(), f32),
        makeUnary(module, BinaryenReinterpretFloat64(), f64),
        makeUnary(module, BinaryenConvertSInt32ToFloat32(), i32),
        makeUnary(module, BinaryenConvertSInt32ToFloat64(), i32),
        makeUnary(module, BinaryenConvertUInt32ToFloat32(), i32),
        makeUnary(module, BinaryenConvertUInt32ToFloat64(), i32),
        makeUnary(module, BinaryenConvertSInt64ToFloat32(), i64),
        makeUnary(module, BinaryenConvertSInt64ToFloat64(), i64),
        makeUnary(module, BinaryenConvertUInt64ToFloat32(), i64),
        makeUnary(module, BinaryenConvertUInt64ToFloat64(), i64),
        makeUnary(module, BinaryenPromoteFloat32(), f32),
        makeUnary(module, BinaryenDemoteFloat64(), f64),
        makeUnary(module, BinaryenReinterpretInt32(), i32),
        makeUnary(module, BinaryenReinterpretInt64(), i64),
        makeUnary(module, BinaryenSplatVecI8x16(), i32),
        makeUnary(module, BinaryenSplatVecI16x8(), i32),
        makeUnary(module, BinaryenSplatVecI32x4(), i32),
        makeUnary(module, BinaryenSplatVecI64x2(), i64),
        makeUnary(module, BinaryenSplatVecF32x4(), f32),
        makeUnary(module, BinaryenSplatVecF64x2(), f64),
        makeUnary(module, BinaryenNotVec128(), v128),
        makeUnary(module, BinaryenAnyTrueVec128(), v128),
        makeUnary(module, BinaryenPopcntVecI8x16(), v128),
        makeUnary(module, BinaryenAbsVecI8x16(), v128),
        makeUnary(module, BinaryenNegVecI8x16(), v128),
        makeUnary(module, BinaryenAllTrueVecI8x16(), v128),
        makeUnary(module, BinaryenBitmaskVecI8x16(), v128),
        makeUnary(module, BinaryenAbsVecI16x8(), v128),
        makeUnary(module, BinaryenNegVecI16x8(), v128),
        makeUnary(module, BinaryenAllTrueVecI16x8(), v128),
        makeUnary(module, BinaryenBitmaskVecI16x8(), v128),
        makeUnary(module, BinaryenAbsVecI32x4(), v128),
        makeUnary(module, BinaryenNegVecI32x4(), v128),
        makeUnary(module, BinaryenAllTrueVecI32x4(), v128),
        makeUnary(module, BinaryenBitmaskVecI32x4(), v128),
        makeUnary(module, BinaryenAbsVecI64x2(), v128),
        makeUnary(module, BinaryenNegVecI64x2(), v128),
        makeUnary(module, BinaryenAllTrueVecI64x2(), v128),
        makeUnary(module, BinaryenBitmaskVecI64x2(), v128),
        makeUnary(module, BinaryenAbsVecF32x4(), v128),
        makeUnary(module, BinaryenNegVecF32x4(), v128),
        makeUnary(module, BinaryenSqrtVecF32x4(), v128),
        makeUnary(module, BinaryenAbsVecF64x2(), v128),
        makeUnary(module, BinaryenNegVecF64x2(), v128),
        makeUnary(module, BinaryenSqrtVecF64x2(), v128),
        makeUnary(module, BinaryenTruncSatSVecF32x4ToVecI32x4(), v128),
        makeUnary(module, BinaryenTruncSatUVecF32x4ToVecI32x4(), v128),
        makeUnary(module, BinaryenConvertSVecI32x4ToVecF32x4(), v128),
        makeUnary(module, BinaryenConvertUVecI32x4ToVecF32x4(), v128),
        makeUnary(module, BinaryenExtendLowSVecI8x16ToVecI16x8(), v128),
        makeUnary(module, BinaryenExtendHighSVecI8x16ToVecI16x8(), v128),
        makeUnary(module, BinaryenExtendLowUVecI8x16ToVecI16x8(), v128),
        makeUnary(module, BinaryenExtendHighUVecI8x16ToVecI16x8(), v128),
        makeUnary(module, BinaryenExtendLowSVecI16x8ToVecI32x4(), v128),
        makeUnary(module, BinaryenExtendHighSVecI16x8ToVecI32x4(), v128),
        makeUnary(module, BinaryenExtendLowUVecI16x8ToVecI32x4(), v128),
        makeUnary(module, BinaryenExtendHighUVecI16x8ToVecI32x4(), v128),
        makeUnary(module, BinaryenExtendLowSVecI32x4ToVecI64x2(), v128),
        makeUnary(module, BinaryenExtendHighSVecI32x4ToVecI64x2(), v128),
        makeUnary(module, BinaryenExtendLowUVecI32x4ToVecI64x2(), v128),
        makeUnary(module, BinaryenExtendHighUVecI32x4ToVecI64x2(), v128),
        makeUnary(module, BinaryenConvertLowSVecI32x4ToVecF64x2(), v128),
        makeUnary(module, BinaryenConvertLowUVecI32x4ToVecF64x2(), v128),
        makeUnary(module, BinaryenTruncSatZeroSVecF64x2ToVecI32x4(), v128),
        makeUnary(module, BinaryenTruncSatZeroUVecF64x2ToVecI32x4(), v128),
        makeUnary(module, BinaryenDemoteZeroVecF64x2ToVecF32x4(), v128),
        makeUnary(module, BinaryenPromoteLowVecF32x4ToVecF64x2(), v128),
        # Binary
        makeBinary(module, BinaryenAddInt32(), i32),
        makeBinary(module, BinaryenSubFloat64(), f64),
        makeBinary(module, BinaryenDivSInt32(), i32),
        makeBinary(module, BinaryenDivUInt64(), i64),
        makeBinary(module, BinaryenRemSInt64(), i64),
        makeBinary(module, BinaryenRemUInt32(), i32),
        makeBinary(module, BinaryenAndInt32(), i32),
        makeBinary(module, BinaryenOrInt64(), i64),
        makeBinary(module, BinaryenXorInt32(), i32),
        makeBinary(module, BinaryenShlInt64(), i64),
        makeBinary(module, BinaryenShrUInt64(), i64),
        makeBinary(module, BinaryenShrSInt32(), i32),
        makeBinary(module, BinaryenRotLInt32(), i32),
        makeBinary(module, BinaryenRotRInt64(), i64),
        makeBinary(module, BinaryenDivFloat32(), f32),
        makeBinary(module, BinaryenCopySignFloat64(), f64),
        makeBinary(module, BinaryenMinFloat32(), f32),
        makeBinary(module, BinaryenMaxFloat64(), f64),
        makeBinary(module, BinaryenEqInt32(), i32),
        makeBinary(module, BinaryenNeFloat32(), f32),
        makeBinary(module, BinaryenLtSInt32(), i32),
        makeBinary(module, BinaryenLtUInt64(), i64),
        makeBinary(module, BinaryenLeSInt64(), i64),
        makeBinary(module, BinaryenLeUInt32(), i32),
        makeBinary(module, BinaryenGtSInt64(), i64),
        makeBinary(module, BinaryenGtUInt32(), i32),
        makeBinary(module, BinaryenGeSInt32(), i32),
        makeBinary(module, BinaryenGeUInt64(), i64),
        makeBinary(module, BinaryenLtFloat32(), f32),
        makeBinary(module, BinaryenLeFloat64(), f64),
        makeBinary(module, BinaryenGtFloat64(), f64),
        makeBinary(module, BinaryenGeFloat32(), f32),
        makeBinary(module, BinaryenEqVecI8x16(), v128),
        makeBinary(module, BinaryenNeVecI8x16(), v128),
        makeBinary(module, BinaryenLtSVecI8x16(), v128),
        makeBinary(module, BinaryenLtUVecI8x16(), v128),
        makeBinary(module, BinaryenGtSVecI8x16(), v128),
        makeBinary(module, BinaryenGtUVecI8x16(), v128),
        makeBinary(module, BinaryenLeSVecI8x16(), v128),
        makeBinary(module, BinaryenLeUVecI8x16(), v128),
        makeBinary(module, BinaryenGeSVecI8x16(), v128),
        makeBinary(module, BinaryenGeUVecI8x16(), v128),
        makeBinary(module, BinaryenEqVecI16x8(), v128),
        makeBinary(module, BinaryenNeVecI16x8(), v128),
        makeBinary(module, BinaryenLtSVecI16x8(), v128),
        makeBinary(module, BinaryenLtUVecI16x8(), v128),
        makeBinary(module, BinaryenGtSVecI16x8(), v128),
        makeBinary(module, BinaryenGtUVecI16x8(), v128),
        makeBinary(module, BinaryenLeSVecI16x8(), v128),
        makeBinary(module, BinaryenLeUVecI16x8(), v128),
        makeBinary(module, BinaryenGeSVecI16x8(), v128),
        makeBinary(module, BinaryenGeUVecI16x8(), v128),
        makeBinary(module, BinaryenEqVecI32x4(), v128),
        makeBinary(module, BinaryenNeVecI32x4(), v128),
        makeBinary(module, BinaryenLtSVecI32x4(), v128),
        makeBinary(module, BinaryenLtUVecI32x4(), v128),
        makeBinary(module, BinaryenGtSVecI32x4(), v128),
        makeBinary(module, BinaryenGtUVecI32x4(), v128),
        makeBinary(module, BinaryenLeSVecI32x4(), v128),
        makeBinary(module, BinaryenLeUVecI32x4(), v128),
        makeBinary(module, BinaryenGeSVecI32x4(), v128),
        makeBinary(module, BinaryenGeUVecI32x4(), v128),
        makeBinary(module, BinaryenEqVecI64x2(), v128),
        makeBinary(module, BinaryenNeVecI64x2(), v128),
        makeBinary(module, BinaryenLtSVecI64x2(), v128),
        makeBinary(module, BinaryenGtSVecI64x2(), v128),
        makeBinary(module, BinaryenLeSVecI64x2(), v128),
        makeBinary(module, BinaryenGeSVecI64x2(), v128),
        makeBinary(module, BinaryenEqVecF32x4(), v128),
        makeBinary(module, BinaryenNeVecF32x4(), v128),
        makeBinary(module, BinaryenLtVecF32x4(), v128),
        makeBinary(module, BinaryenGtVecF32x4(), v128),
        makeBinary(module, BinaryenLeVecF32x4(), v128),
        makeBinary(module, BinaryenGeVecF32x4(), v128),
        makeBinary(module, BinaryenEqVecF64x2(), v128),
        makeBinary(module, BinaryenNeVecF64x2(), v128),
        makeBinary(module, BinaryenLtVecF64x2(), v128),
        makeBinary(module, BinaryenGtVecF64x2(), v128),
        makeBinary(module, BinaryenLeVecF64x2(), v128),
        makeBinary(module, BinaryenGeVecF64x2(), v128),
        makeBinary(module, BinaryenAndVec128(), v128),
        makeBinary(module, BinaryenOrVec128(), v128),
        makeBinary(module, BinaryenXorVec128(), v128),
        makeBinary(module, BinaryenAndNotVec128(), v128),
        makeBinary(module, BinaryenAddVecI8x16(), v128),
        makeBinary(module, BinaryenAddSatSVecI8x16(), v128),
        makeBinary(module, BinaryenAddSatUVecI8x16(), v128),
        makeBinary(module, BinaryenSubVecI8x16(), v128),
        makeBinary(module, BinaryenSubSatSVecI8x16(), v128),
        makeBinary(module, BinaryenSubSatUVecI8x16(), v128),
        makeBinary(module, BinaryenMinSVecI8x16(), v128),
        makeBinary(module, BinaryenMinUVecI8x16(), v128),
        makeBinary(module, BinaryenMaxSVecI8x16(), v128),
        makeBinary(module, BinaryenMaxUVecI8x16(), v128),
        makeBinary(module, BinaryenAvgrUVecI8x16(), v128),
        makeBinary(module, BinaryenAddVecI16x8(), v128),
        makeBinary(module, BinaryenAddSatSVecI16x8(), v128),
        makeBinary(module, BinaryenAddSatUVecI16x8(), v128),
        makeBinary(module, BinaryenSubVecI16x8(), v128),
        makeBinary(module, BinaryenSubSatSVecI16x8(), v128),
        makeBinary(module, BinaryenSubSatUVecI16x8(), v128),
        makeBinary(module, BinaryenMulVecI16x8(), v128),
        makeBinary(module, BinaryenMinSVecI16x8(), v128),
        makeBinary(module, BinaryenMinUVecI16x8(), v128),
        makeBinary(module, BinaryenMaxSVecI16x8(), v128),
        makeBinary(module, BinaryenMaxUVecI16x8(), v128),
        makeBinary(module, BinaryenAvgrUVecI16x8(), v128),
        makeBinary(module, BinaryenQ15MulrSatSVecI16x8(), v128),
        makeBinary(module, BinaryenExtMulLowSVecI16x8(), v128),
        makeBinary(module, BinaryenExtMulHighSVecI16x8(), v128),
        makeBinary(module, BinaryenExtMulLowUVecI16x8(), v128),
        makeBinary(module, BinaryenExtMulHighUVecI16x8(), v128),
        makeBinary(module, BinaryenAddVecI32x4(), v128),
        makeBinary(module, BinaryenSubVecI32x4(), v128),
        makeBinary(module, BinaryenMulVecI32x4(), v128),
        makeBinary(module, BinaryenAddVecI64x2(), v128),
        makeBinary(module, BinaryenSubVecI64x2(), v128),
        makeBinary(module, BinaryenMulVecI64x2(), v128),
        makeBinary(module, BinaryenExtMulLowSVecI64x2(), v128),
        makeBinary(module, BinaryenExtMulHighSVecI64x2(), v128),
        makeBinary(module, BinaryenExtMulLowUVecI64x2(), v128),
        makeBinary(module, BinaryenExtMulHighUVecI64x2(), v128),
        makeBinary(module, BinaryenAddVecF32x4(), v128),
        makeBinary(module, BinaryenSubVecF32x4(), v128),
        makeBinary(module, BinaryenMulVecF32x4(), v128),
        makeBinary(module, BinaryenMinSVecI32x4(), v128),
        makeBinary(module, BinaryenMinUVecI32x4(), v128),
        makeBinary(module, BinaryenMaxSVecI32x4(), v128),
        makeBinary(module, BinaryenMaxUVecI32x4(), v128),
        makeBinary(module, BinaryenDotSVecI16x8ToVecI32x4(), v128),
        makeBinary(module, BinaryenExtMulLowSVecI32x4(), v128),
        makeBinary(module, BinaryenExtMulHighSVecI32x4(), v128),
        makeBinary(module, BinaryenExtMulLowUVecI32x4(), v128),
        makeBinary(module, BinaryenExtMulHighUVecI32x4(), v128),
        makeBinary(module, BinaryenDivVecF32x4(), v128),
        makeBinary(module, BinaryenMinVecF32x4(), v128),
        makeBinary(module, BinaryenMaxVecF32x4(), v128),
        makeBinary(module, BinaryenPMinVecF32x4(), v128),
        makeBinary(module, BinaryenPMaxVecF32x4(), v128),
        makeUnary(module, BinaryenCeilVecF32x4(), v128),
        makeUnary(module, BinaryenFloorVecF32x4(), v128),
        makeUnary(module, BinaryenTruncVecF32x4(), v128),
        makeUnary(module, BinaryenNearestVecF32x4(), v128),
        makeBinary(module, BinaryenAddVecF64x2(), v128),
        makeBinary(module, BinaryenSubVecF64x2(), v128),
        makeBinary(module, BinaryenMulVecF64x2(), v128),
        makeBinary(module, BinaryenDivVecF64x2(), v128),
        makeBinary(module, BinaryenMinVecF64x2(), v128),
        makeBinary(module, BinaryenMaxVecF64x2(), v128),
        makeBinary(module, BinaryenPMinVecF64x2(), v128),
        makeBinary(module, BinaryenPMaxVecF64x2(), v128),
        makeUnary(module, BinaryenCeilVecF64x2(), v128),
        makeUnary(module, BinaryenFloorVecF64x2(), v128),
        makeUnary(module, BinaryenTruncVecF64x2(), v128),
        makeUnary(module, BinaryenNearestVecF64x2(), v128),
        makeUnary(module, BinaryenExtAddPairwiseSVecI8x16ToI16x8(), v128),
        makeUnary(module, BinaryenExtAddPairwiseUVecI8x16ToI16x8(), v128),
        makeUnary(module, BinaryenExtAddPairwiseSVecI16x8ToI32x4(), v128),
        makeUnary(module, BinaryenExtAddPairwiseUVecI16x8ToI32x4(), v128),
        makeBinary(module, BinaryenNarrowSVecI16x8ToVecI8x16(), v128),
        makeBinary(module, BinaryenNarrowUVecI16x8ToVecI8x16(), v128),
        makeBinary(module, BinaryenNarrowSVecI32x4ToVecI16x8(), v128),
        makeBinary(module, BinaryenNarrowUVecI32x4ToVecI16x8(), v128),
        makeBinary(module, BinaryenSwizzleVecI8x16(), v128),
        # SIMD lane manipulation
        makeSIMDExtract(module, BinaryenExtractLaneSVecI8x16()),
        makeSIMDExtract(module, BinaryenExtractLaneUVecI8x16()),
        makeSIMDExtract(module, BinaryenExtractLaneSVecI16x8()),
        makeSIMDExtract(module, BinaryenExtractLaneUVecI16x8()),
        makeSIMDExtract(module, BinaryenExtractLaneVecI32x4()),
        makeSIMDExtract(module, BinaryenExtractLaneVecI64x2()),
        makeSIMDExtract(module, BinaryenExtractLaneVecF32x4()),
        makeSIMDExtract(module, BinaryenExtractLaneVecF64x2()),
        makeSIMDReplace(module, BinaryenReplaceLaneVecI8x16(), i32),
        makeSIMDReplace(module, BinaryenReplaceLaneVecI16x8(), i32),
        makeSIMDReplace(module, BinaryenReplaceLaneVecI32x4(), i32),
        makeSIMDReplace(module, BinaryenReplaceLaneVecI64x2(), i64),
        makeSIMDReplace(module, BinaryenReplaceLaneVecF32x4(), f32),
        makeSIMDReplace(module, BinaryenReplaceLaneVecF64x2(), f64),
        # SIMD shift
        makeSIMDShift(module, BinaryenShlVecI8x16()),
        makeSIMDShift(module, BinaryenShrSVecI8x16()),
        makeSIMDShift(module, BinaryenShrUVecI8x16()),
        makeSIMDShift(module, BinaryenShlVecI16x8()),
        makeSIMDShift(module, BinaryenShrSVecI16x8()),
        makeSIMDShift(module, BinaryenShrUVecI16x8()),
        makeSIMDShift(module, BinaryenShlVecI32x4()),
        makeSIMDShift(module, BinaryenShrSVecI32x4()),
        makeSIMDShift(module, BinaryenShrUVecI32x4()),
        makeSIMDShift(module, BinaryenShlVecI64x2()),
        makeSIMDShift(module, BinaryenShrSVecI64x2()),
        makeSIMDShift(module, BinaryenShrUVecI64x2()),
        # SIMD load
        BinaryenSIMDLoad(
            module, BinaryenLoad8SplatVec128(), 0, 1, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad16SplatVec128(), 16, 1, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad32SplatVec128(), 16, 4, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad64SplatVec128(), 0, 4, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad8x8SVec128(), 0, 8, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad8x8UVec128(), 0, 8, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad16x4SVec128(), 0, 8, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad16x4UVec128(), 0, 8, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad32x2SVec128(), 0, 8, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad32x2UVec128(), 0, 8, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad32ZeroVec128(), 0, 4, makeInt32(module, 128), '0'),
        BinaryenSIMDLoad(
            module, BinaryenLoad64ZeroVec128(), 0, 8, makeInt32(module, 128), '0'),
        # SIMD load/store lane
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenLoad8LaneVec128(),
                                  0,
                                  1,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenLoad16LaneVec128(),
                                  0,
                                  2,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenLoad32LaneVec128(),
                                  0,
                                  4,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenLoad64LaneVec128(),
                                  0,
                                  8,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenStore8LaneVec128(),
                                  0,
                                  1,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenStore16LaneVec128(),
                                  0,
                                  2,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenStore32LaneVec128(),
                                  0,
                                  4,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        BinaryenSIMDLoadStoreLane(module,
                                  BinaryenStore64LaneVec128(),
                                  0,
                                  8,
                                  0,
                                  makeInt32(module, 128),
                                  makeVec128(module, v128_bytes),
                                  '0'),
        # Other SIMD
        makeSIMDShuffle(module),
        makeSIMDTernary(module, BinaryenBitselectVec128()),
        # Bulk memory
        makeMemoryInit(module),
        makeDataDrop(module),
        makeMemoryCopy(module),
        makeMemoryFill(module),
        # All the rest
        # TODO: The last arg was -1, Auto or None? Double check buffer overflow
        BinaryenBlock(module, None, None, BinaryenTypeAuto()),  # block with no name and no type
        BinaryenIf(module, temp1, temp2, temp3),
        BinaryenIf(module, temp4, temp5, None),
        BinaryenLoop(module, 'in', makeInt32(module, 0)),
        BinaryenLoop(module, None, makeInt32(module, 0)),
        BinaryenBreak(module, 'the-value', temp6, temp7),
        BinaryenBreak(module, 'the-nothing', makeInt32(module, 2), None),
        BinaryenBreak(module, 'the-value', None, makeInt32(module, 3)),
        BinaryenBreak(module, 'the-nothing', None, None),
        BinaryenSwitch(module, switchValueNames, 'the-value', temp8, temp9),
        BinaryenSwitch(
            module, switchBodyNames, 'the-nothing', makeInt32(module, 2), None),
        BinaryenUnary(
            module,
            BinaryenEqZInt32(),  # check the output type of the call node
            BinaryenCall(
                module, 'kitchen()sinker', callOperands4, BinaryenTypeInt32())),
        BinaryenUnary(module,
                      BinaryenEqZInt32(),  # check the output type of the call node
                      BinaryenUnary(module,
                                    BinaryenTruncSFloat32ToInt32(),
                                    BinaryenCall(module,
                                                 'an-imported',
                                                 callOperands2,
                                                 BinaryenTypeFloat32()))),
        BinaryenUnary(module,
                      BinaryenEqZInt32(),  # check the output type of the call node
                      BinaryenCallIndirect(module,
                                           'tab',
                                           makeInt32(module, 2449),
                                           callOperands4b,
                                           iIfF,
                                           BinaryenTypeInt32())),
        BinaryenDrop(module, BinaryenLocalGet(module, 0, BinaryenTypeInt32())),
        BinaryenLocalSet(module, 0, makeInt32(module, 101)),
        BinaryenDrop(
            module,
            BinaryenLocalTee(module, 0, makeInt32(module, 102), BinaryenTypeInt32())),
        BinaryenLoad(
            module, 4, False, 0, 0, BinaryenTypeInt32(), makeInt32(module, 1), '0'),
        BinaryenLoad(
            module, 2, True, 2, 1, BinaryenTypeInt64(), makeInt32(module, 8), '0'),
        BinaryenLoad(
            module, 4, False, 0, 0, BinaryenTypeFloat32(), makeInt32(module, 2), '0'),
        BinaryenLoad(
            module, 8, False, 2, 8, BinaryenTypeFloat64(), makeInt32(module, 9), '0'),
        BinaryenStore(module, 4, 0, 0, temp13, temp14, BinaryenTypeInt32(), '0'),
        BinaryenStore(module, 8, 2, 4, temp15, temp16, BinaryenTypeInt64(), '0'),
        BinaryenSelect(module, temp10, temp11, temp12, BinaryenTypeAuto()),
        BinaryenReturn(module, makeInt32(module, 1337)),
        # Tail call
        BinaryenReturnCall(
            module, 'kitchen()sinker', callOperands4, BinaryenTypeInt32()),
        BinaryenReturnCallIndirect(module,
                                   'tab',
                                   makeInt32(module, 2449),
                                   callOperands4b,
                                   iIfF,
                                   BinaryenTypeInt32()),
        # Reference types
        BinaryenRefIs(module, BinaryenRefIsNull(), externrefExpr),
        BinaryenRefIs(module, BinaryenRefIsNull(), funcrefExpr),
        BinaryenSelect(
            module,
            temp10,
            BinaryenRefNull(module, BinaryenTypeNullFuncref()),
            BinaryenRefFunc(module, 'kitchen()sinker', BinaryenTypeFuncref()),
            BinaryenTypeFuncref()),
        # GC
        BinaryenRefEq(module,
                      BinaryenRefNull(module, BinaryenTypeNullref()),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefIs(module,
                      BinaryenRefIsFunc(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefIs(module,
                      BinaryenRefIsData(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefIs(module,
                      BinaryenRefIsI31(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefAs(module,
                      BinaryenRefAsNonNull(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefAs(module,
                      BinaryenRefAsFunc(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefAs(module,
                      BinaryenRefAsData(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefAs(module,
                      BinaryenRefAsI31(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        BinaryenRefAs(module,
                      BinaryenRefAsExternInternalize(),
                      BinaryenRefNull(module, BinaryenTypeNullExternref())),
        BinaryenRefAs(module,
                      BinaryenRefAsExternExternalize(),
                      BinaryenRefNull(module, BinaryenTypeNullref())),
        # Exception handling
        BinaryenTry(module, None, tryBody, catchTags, catchBodies, None),
        # (try $try_outer
        #   (do
        #     (try
        #       (do
        #         (throw $a-tag (i32.const 0))
        #       )
        #       (delegate $try_outer)
        #     )
        #   )
        #   (catch_all)
        # )
        BinaryenTry(module,
                    'try_outer',
                    BinaryenTry(module,
                                None,
                                tryBody,
                                emptyCatchTags,
                                emptyCatchBodies,
                                'try_outer'),
                    emptyCatchTags,
                    nopCatchBody,
                    None),
        # Atomics
        BinaryenAtomicStore(
            module,
            4,
            0,
            temp6,
            BinaryenAtomicLoad(module, 4, 0, BinaryenTypeInt32(), temp6, '0'),
            BinaryenTypeInt32(),
            '0'),
        BinaryenDrop(module,
                     BinaryenAtomicWait(
                         module, temp6, temp6, temp16, BinaryenTypeInt32(), '0')),
        BinaryenDrop(module, BinaryenAtomicNotify(module, temp6, temp6, '0')),
        BinaryenAtomicFence(module),
        # Tuples
        BinaryenTupleMake(module, tupleElements4a),
        BinaryenTupleExtract(
            module, BinaryenTupleMake(module, tupleElements4b), 2),
        # Pop
        BinaryenPop(module, BinaryenTypeInt32()),
        BinaryenPop(module, BinaryenTypeInt64()),
        BinaryenPop(module, BinaryenTypeFloat32()),
        BinaryenPop(module, BinaryenTypeFloat64()),
        BinaryenPop(module, BinaryenTypeFuncref()),
        BinaryenPop(module, BinaryenTypeExternref()),
        BinaryenPop(module, iIfF),
        # Memory
        BinaryenMemorySize(module, '0', False),
        BinaryenMemoryGrow(module, makeInt32(module, 0), '0', False),
        # GC
        BinaryenI31New(module, makeInt32(module, 0)),
        BinaryenI31Get(module, i31refExpr, True),
        BinaryenI31Get(module, BinaryenI31New(module, makeInt32(module, 2)), False),
        BinaryenRefTest(module,
            BinaryenGlobalGet(module, 'i8Array-global', i8Array), BinaryenTypeGetHeapType(i8Array)),
        BinaryenRefCast(module,
            BinaryenGlobalGet(module, 'i8Array-global', i8Array), BinaryenTypeGetHeapType(i8Array)),
        BinaryenStructNew(module, None, BinaryenTypeGetHeapType(i32Struct)),
        BinaryenStructNew(module,
                          [makeInt32(module, 0)],
                          BinaryenTypeGetHeapType(i32Struct)),
        BinaryenStructGet(module,
                          0,
                          BinaryenGlobalGet(module, 'i32Struct-global', i32Struct),
                          BinaryenTypeInt32(),
                          False),
        BinaryenStructSet(module,
                          0,
                          BinaryenGlobalGet(module, 'i32Struct-global', i32Struct),
                          makeInt32(module, 0)),
        BinaryenArrayNew(
            module, BinaryenTypeGetHeapType(i8Array), makeInt32(module, 3), None),
        BinaryenArrayNew(module,
                         BinaryenTypeGetHeapType(i8Array),
                         makeInt32(module, 3),
                         makeInt32(module, 42)),
        BinaryenArrayInit(module,
                          BinaryenTypeGetHeapType(i8Array),
                          [
                              makeInt32(module, 1),
                              makeInt32(module, 2),
                              makeInt32(module, 3),
                          ]),
        BinaryenArrayGet(module,
                         BinaryenGlobalGet(module, 'i8Array-global', i8Array),
                         makeInt32(module, 0),
                         BinaryenTypeInt32(),
                         True),
        BinaryenArraySet(module,
                         BinaryenGlobalGet(module, 'i8Array-global', i8Array),
                         makeInt32(module, 0),
                         makeInt32(module, 42)),
        BinaryenArrayLen(module,
                         BinaryenGlobalGet(module, 'i8Array-global', i8Array)),
        BinaryenArrayCopy(module,
                          BinaryenGlobalGet(module, 'i8Array-global', i8Array),
                          makeInt32(module, 0),
                          BinaryenGlobalGet(module, 'i8Array-global', i8Array),
                          makeInt32(module, 1),
                          makeInt32(module, 2)),
        # Strings
        BinaryenStringNew(module,
                          BinaryenStringNewUTF8(),
                          makeInt32(module, 0),
                          makeInt32(module, 0),
                          None,
                          None),
        BinaryenStringNew(module,
                          BinaryenStringNewWTF8(),
                          makeInt32(module, 0),
                          makeInt32(module, 0),
                          None,
                          None),
        BinaryenStringNew(module,
                          BinaryenStringNewReplace(),
                          makeInt32(module, 0),
                          makeInt32(module, 0),
                          None,
                          None),
        BinaryenStringNew(module,
                          BinaryenStringNewWTF16(),
                          makeInt32(module, 0),
                          makeInt32(module, 0),
                          None,
                          None),
        BinaryenStringNew(module,
                          BinaryenStringNewUTF8Array(),
                          BinaryenGlobalGet(module, 'i8Array-global', i8Array),
                          None,
                          makeInt32(module, 0),
                          makeInt32(module, 0)),
        BinaryenStringNew(module,
                          BinaryenStringNewWTF8Array(),
                          BinaryenGlobalGet(module, 'i8Array-global', i8Array),
                          None,
                          makeInt32(module, 0),
                          makeInt32(module, 0)),
        BinaryenStringNew(module,
                          BinaryenStringNewReplaceArray(),
                          BinaryenGlobalGet(module, 'i8Array-global', i8Array),
                          None,
                          makeInt32(module, 0),
                          makeInt32(module, 0)),
        BinaryenStringNew(module,
                          BinaryenStringNewWTF16Array(),
                          BinaryenGlobalGet(module, 'i16Array-global', i8Array),
                          None,
                          makeInt32(module, 0),
                          makeInt32(module, 0)),
        BinaryenStringConst(module, 'hello world'),
        BinaryenStringMeasure(
            module,
            BinaryenStringMeasureUTF8(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringMeasure(
            module,
            BinaryenStringMeasureWTF8(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringMeasure(
            module,
            BinaryenStringMeasureWTF16(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringMeasure(
            module,
            BinaryenStringMeasureIsUSV(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringMeasure(
            module,
            BinaryenStringMeasureWTF16View(),
            BinaryenStringAs(
                module,
                BinaryenStringAsWTF16(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()))),
        BinaryenStringEncode(
            module,
            BinaryenStringEncodeUTF8(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            makeInt32(module, 0),
            None),
        BinaryenStringEncode(
            module,
            BinaryenStringEncodeWTF8(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            makeInt32(module, 0),
            None),
        BinaryenStringEncode(
            module,
            BinaryenStringEncodeWTF16(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            makeInt32(module, 0),
            None),
        BinaryenStringEncode(
            module,
            BinaryenStringEncodeUTF8Array(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            BinaryenGlobalGet(module, 'i8Array-global', i8Array),
            makeInt32(module, 0)),
        BinaryenStringEncode(
            module,
            BinaryenStringEncodeWTF8Array(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            BinaryenGlobalGet(module, 'i8Array-global', i8Array),
            makeInt32(module, 0)),
        BinaryenStringEncode(
            module,
            BinaryenStringEncodeWTF16Array(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            BinaryenGlobalGet(module, 'i16Array-global', i16Array),
            makeInt32(module, 0)),
        BinaryenStringConcat(
            module,
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringEq(
            module,
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringAs(
            module,
            BinaryenStringAsWTF8(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringAs(
            module,
            BinaryenStringAsWTF16(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringAs(
            module,
            BinaryenStringAsIter(),
            BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
        BinaryenStringWTF8Advance(
            module,
            BinaryenStringAs(
                module,
                BinaryenStringAsWTF8(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
            makeInt32(module, 0),
            makeInt32(module, 0)),
        BinaryenStringWTF16Get(
            module,
            BinaryenStringAs(
                module,
                BinaryenStringAsWTF16(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
            makeInt32(module, 0)),
        BinaryenStringIterNext(
            module,
            BinaryenStringAs(
                module,
                BinaryenStringAsIter(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref()))),
        BinaryenStringIterMove(
            module,
            BinaryenStringIterMoveAdvance(),
            BinaryenStringAs(
                module,
                BinaryenStringAsIter(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
            makeInt32(module, 1)),
        BinaryenStringIterMove(
            module,
            BinaryenStringIterMoveRewind(),
            BinaryenStringAs(
                module,
                BinaryenStringAsIter(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
            makeInt32(module, 1)),
        BinaryenStringSliceWTF(
            module,
            BinaryenStringSliceWTF8(),
            BinaryenStringAs(
                module,
                BinaryenStringAsWTF8(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
            makeInt32(module, 0),
            makeInt32(module, 0)),
        BinaryenStringSliceWTF(
            module,
            BinaryenStringSliceWTF16(),
            BinaryenStringAs(
                module,
                BinaryenStringAsWTF16(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
            makeInt32(module, 0),
            makeInt32(module, 0)),
        BinaryenStringSliceIter(
            module,
            BinaryenStringAs(
                module,
                BinaryenStringAsIter(),
                BinaryenGlobalGet(module, 'string-global', BinaryenTypeStringref())),
            makeInt32(module, 0)),
        # Other
        BinaryenNop(module),
        BinaryenUnreachable(module),
    ]

    BinaryenExpressionPrint(
        valueList[3])  # test printing a standalone expression

    # Make the main body of the function. and one block with a return value, one
    # without
    value = BinaryenBlock(module,
                          'the-value',
                          valueList,
                          BinaryenTypeAuto())
    droppedValue = BinaryenDrop(module, value)
    # TODO: The last arg was -1, Auto or None? Double check buffer overflow
    nothing = BinaryenBlock(module, 'the-nothing', droppedValue, BinaryenTypeAuto())
    bodyList = [nothing, makeInt32(module, 42)]
    body = BinaryenBlock(module, 'the-body', bodyList, BinaryenTypeAuto())

    # Create the function
    localTypes = [BinaryenTypeInt32(), BinaryenTypeExternref()]
    sinker = BinaryenAddFunction(
        module, 'kitchen()sinker', iIfF, BinaryenTypeInt32(), localTypes, body)

    # Globals

    BinaryenAddGlobal(
        module, 'a-global', BinaryenTypeInt32(), False, makeInt32(module, 7))
    BinaryenAddGlobal(module,
                      'a-mutable-global',
                      BinaryenTypeFloat32(),
                      True,
                      makeFloat32(module, 7.5))
    BinaryenAddGlobal(
        module,
        'i8Array-global',
        i8Array,
        True,
        BinaryenArrayNew(
            module, BinaryenTypeGetHeapType(i8Array), makeInt32(module, 0), None))
    BinaryenAddGlobal(
        module,
        'i16Array-global',
        i16Array,
        True,
        BinaryenArrayNew(
            module, BinaryenTypeGetHeapType(i16Array), makeInt32(module, 0), None))
    BinaryenAddGlobal(
        module,
        'i32Struct-global',
        i32Struct,
        True,
        BinaryenStructNew(module, None, BinaryenTypeGetHeapType(i32Struct)))
    BinaryenAddGlobal(module,
                      'string-global',
                      BinaryenTypeStringref(),
                      True,
                      BinaryenStringConst(module, ''))

    # Imports

    iF_ = [BinaryenTypeInt32(), BinaryenTypeFloat64()]
    iF = BinaryenTypeCreate(iF_)
    BinaryenAddFunctionImport(
        module, 'an-imported', 'module', 'base', iF, BinaryenTypeFloat32())

    # Exports

    BinaryenAddFunctionExport(module, 'kitchen()sinker', 'kitchen_sinker')

    # Function table. One per module
    funcNames = [BinaryenFunctionGetName(sinker)]
    BinaryenAddTable(module, '0', 1, 1, BinaryenTypeFuncref())
    BinaryenAddActiveElementSegment(
        module,
        '0',
        '0',
        funcNames,
        BinaryenConst(module, BinaryenLiteralInt32(0)))
    BinaryenAddPassiveElementSegment(module, 'passive', funcNames)
    BinaryenAddPassiveElementSegment(module, 'p2', funcNames)
    BinaryenRemoveElementSegment(module, 'p2')

    funcrefExpr1 = BinaryenRefFunc(module, 'kitchen()sinker', BinaryenTypeFuncref())

    BinaryenExpressionPrint(BinaryenTableSet(
        module, '0', BinaryenConst(module, BinaryenLiteralInt32(0)), funcrefExpr1))

    funcrefExpr2 = BinaryenTableGet(module,
                                    '0',
                                    BinaryenConst(module, BinaryenLiteralInt32(0)),
                                    BinaryenTypeFuncref())

    BinaryenExpressionPrint(funcrefExpr2)

    tablesize = BinaryenTableSize(module, '0')
    BinaryenExpressionPrint(tablesize)

    table = BinaryenTableSizeGetTable(tablesize)
    BinaryenTableSizeSetTable(tablesize, table)

    valueExpr = BinaryenRefNull(module, BinaryenTypeNullFuncref())
    sizeExpr = makeInt32(module, 0)
    growExpr = BinaryenTableGrow(module, '0', valueExpr, sizeExpr)
    BinaryenExpressionPrint(growExpr)

    # Start function. One per module

    starter = BinaryenAddFunction(module,
                                  'starter',
                                  BinaryenTypeNone(),
                                  BinaryenTypeNone(),
                                  None,
                                  BinaryenNop(module))
    BinaryenSetStart(module, starter)

    # A bunch of our code needs drop(), auto-add it
    BinaryenModuleAutoDrop(module)

    features = BinaryenFeatureAll()
    BinaryenModuleSetFeatures(module, features)
    assert (BinaryenModuleGetFeatures(module) == features)

    # Print it out
    BinaryenModulePrint(module)

    # Verify it validates
    assert (BinaryenModuleValidate(module))

    # Clean up the module, which owns all the objects we created above
    BinaryenModuleDispose(module)


def test_unreachable():
    module = BinaryenModuleCreate()
    body = BinaryenCallIndirect(module,
                                'invalid-table',
                                BinaryenUnreachable(module),
                                None,
                                BinaryenTypeNone(),
                                BinaryenTypeInt64())
    fn = BinaryenAddFunction(module,
                             'unreachable-fn',
                             BinaryenTypeNone(),
                             BinaryenTypeInt32(),
                             None,
                             body)

    assert (BinaryenModuleValidate(module))
    BinaryenModulePrint(module)
    BinaryenModuleDispose(module)


def makeCallCheck(module: BinaryenModuleRef, x: int) -> BinaryenExpressionRef:
    callOperands = [makeInt32(module, x)]
    return BinaryenCall(module, 'check', callOperands, BinaryenTypeNone())


def test_relooper():
    module = BinaryenModuleCreate()
    localTypes = [BinaryenTypeInt32()]

    BinaryenAddFunctionImport(module,
                              'check',
                              'module',
                              'check',
                              BinaryenTypeInt32(),
                              BinaryenTypeNone())

    # trivial: just one block
    relooper = RelooperCreate(module)
    block = RelooperAddBlock(relooper, makeCallCheck(module, 1337))
    body = RelooperRenderAndDispose(relooper, block, 0)
    sinker = BinaryenAddFunction(module,
                                 'just-one-block',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # two blocks
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    RelooperAddBranch(
        block0, block1, None, None)  # no condition, no code on branch
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'two-blocks',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # two blocks with code between them
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    RelooperAddBranch(
        block0, block1, None, makeDroppedInt32(module, 77))  # code on branch
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'two-blocks-plus-code',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # two blocks in a loop
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    RelooperAddBranch(block0, block1, None, None)
    RelooperAddBranch(block1, block0, None, None)
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'loop',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # two blocks in a loop with codes
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    RelooperAddBranch(block0, block1, None, makeDroppedInt32(module, 33))
    RelooperAddBranch(block1, block0, None, makeDroppedInt32(module, -66))
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'loop-plus-code',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # split
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    RelooperAddBranch(block0, block1, makeInt32(module, 55), None)
    RelooperAddBranch(block0, block2, None, None)
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'split',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # split + code
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    temp = makeDroppedInt32(module, 10)
    RelooperAddBranch(block0, block1, makeInt32(module, 55), temp)
    RelooperAddBranch(block0, block2, None, makeDroppedInt32(module, 20))
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'split-plus-code',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # if
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    RelooperAddBranch(block0, block1, makeInt32(module, 55), None)
    RelooperAddBranch(block0, block2, None, None)
    RelooperAddBranch(block1, block2, None, None)
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'if',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # if + code
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    temp = makeDroppedInt32(module, -1)
    RelooperAddBranch(block0, block1, makeInt32(module, 55), temp)
    RelooperAddBranch(block0, block2, None, makeDroppedInt32(module, -2))
    RelooperAddBranch(block1, block2, None, makeDroppedInt32(module, -3))
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'if-plus-code',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # if-else
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    block3 = RelooperAddBlock(relooper, makeCallCheck(module, 3))
    RelooperAddBranch(block0, block1, makeInt32(module, 55), None)
    RelooperAddBranch(block0, block2, None, None)
    RelooperAddBranch(block1, block3, None, None)
    RelooperAddBranch(block2, block3, None, None)
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'if-else',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # loop+tail
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    RelooperAddBranch(block0, block1, None, None)
    RelooperAddBranch(block1, block0, makeInt32(module, 10), None)
    RelooperAddBranch(block1, block2, None, None)
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'loop-tail',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # nontrivial loop + phi to head
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    block3 = RelooperAddBlock(relooper, makeCallCheck(module, 3))
    block4 = RelooperAddBlock(relooper, makeCallCheck(module, 4))
    block5 = RelooperAddBlock(relooper, makeCallCheck(module, 5))
    block6 = RelooperAddBlock(relooper, makeCallCheck(module, 6))
    RelooperAddBranch(block0, block1, None, makeDroppedInt32(module, 10))
    RelooperAddBranch(block1, block2, makeInt32(module, -2), None)
    RelooperAddBranch(block1, block6, None, makeDroppedInt32(module, 20))
    RelooperAddBranch(block2, block3, makeInt32(module, -6), None)
    RelooperAddBranch(block2, block1, None, makeDroppedInt32(module, 30))
    RelooperAddBranch(block3, block4, makeInt32(module, -10), None)
    RelooperAddBranch(block3, block5, None, None)
    RelooperAddBranch(block4, block5, None, None)
    RelooperAddBranch(block5, block6, None, makeDroppedInt32(module, 40))
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'nontrivial-loop-plus-phi-to-head',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # switch
    relooper = RelooperCreate(module)
    temp = makeInt32(module, -99)
    block0 = RelooperAddBlockWithSwitch(relooper, makeCallCheck(module, 0), temp)
    # TODO: this example is not very good, the blocks should end in a |return|
    # as otherwise they
    #       fall through to each other. A relooper block should end in
    #       something that stops control flow, if it doesn't have branches
    #       going out
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    block3 = RelooperAddBlock(relooper, makeCallCheck(module, 3))
    to_block1 = [2, 5]
    RelooperAddBranchForSwitch(block0, block1, to_block1, None)
    to_block2 = [4]
    RelooperAddBranchForSwitch(
        block0, block2, to_block2, makeDroppedInt32(module, 55))
    RelooperAddBranchForSwitch(block0, block3, None, None)
    body = RelooperRenderAndDispose(relooper, block0, 0)
    sinker = BinaryenAddFunction(module,
                                 'switch',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # duff's device
    relooper = RelooperCreate(module)
    block0 = RelooperAddBlock(relooper, makeCallCheck(module, 0))
    block1 = RelooperAddBlock(relooper, makeCallCheck(module, 1))
    block2 = RelooperAddBlock(relooper, makeCallCheck(module, 2))
    RelooperAddBranch(block0, block1, makeInt32(module, 10), None)
    RelooperAddBranch(block0, block2, None, None)
    RelooperAddBranch(block1, block2, None, None)
    RelooperAddBranch(block2, block1, None, None)
    body = RelooperRenderAndDispose(relooper, block0, 3)  # use $3 as the helper var
    localTypes = [
        BinaryenTypeInt32(),
        BinaryenTypeInt32(),
        BinaryenTypeInt64(),
        BinaryenTypeInt32(),
        BinaryenTypeFloat32(),
        BinaryenTypeFloat64(),
        BinaryenTypeInt32()
    ]
    sinker = BinaryenAddFunction(module,
                                 'duffs-device',
                                 BinaryenTypeNone(),
                                 BinaryenTypeNone(),
                                 localTypes,
                                 body)

    # return in a block
    relooper = RelooperCreate(module)
    listList = [
        makeCallCheck(module, 42),
        BinaryenReturn(module, makeInt32(module, 1337))
    ]
    # TODO: The last arg was -1, Auto or None? Double check buffer overflow
    list = BinaryenBlock(module, 'the-list', listList, BinaryenTypeAuto())
    block = RelooperAddBlock(relooper, list)
    body = RelooperRenderAndDispose(relooper, block, 0)
    sinker = BinaryenAddFunction(module,
                                 'return',
                                 BinaryenTypeNone(),
                                 BinaryenTypeInt32(),
                                 localTypes[0:1],  # TODO: Manual fix due to size=1 in the original test
                                 body)

    printf('raw:\n')
    BinaryenModulePrint(module)

    assert (BinaryenModuleValidate(module))

    BinaryenModuleOptimize(module)

    assert (BinaryenModuleValidate(module))

    printf('optimized:\n')
    BinaryenModulePrint(module)

    BinaryenModuleDispose(module)


def test_binaries():
    # char buffer[1024]
    # size_t size

    # create a module and write it to binary
    module = BinaryenModuleCreate()
    ii_ = [BinaryenTypeInt32(), BinaryenTypeInt32()]
    ii = BinaryenTypeCreate(ii_)
    x = BinaryenLocalGet(module, 0, BinaryenTypeInt32())
    y = BinaryenLocalGet(module, 1, BinaryenTypeInt32())
    add = BinaryenBinary(module, BinaryenAddInt32(), x, y)
    adder = BinaryenAddFunction(
        module, 'adder', ii, BinaryenTypeInt32(), None, add)
    BinaryenSetDebugInfo(True)  # include names section
    buffer, size = BinaryenModuleWrite(module, 1024)  # write out the module
    BinaryenSetDebugInfo(False)
    BinaryenModuleDispose(module)

    assert (size > 0)
    assert (size < 512)  # this is a tiny module

    # read the module from the binary
    module = BinaryenModuleRead(buffer, size)

    # validate, print, and free
    assert (BinaryenModuleValidate(module))
    printf('module loaded from binary form:\n')
    BinaryenModulePrint(module)

    # write the s-expr representation of the module.
    buffer, _ = BinaryenModuleWriteText(module, 1024)
    printf('module s-expr printed (in memory):\n%s\n', buffer)

    # writ the s-expr representation to a pointer which is managed by the
    # caller
    text = BinaryenModuleAllocateAndWriteText(module)
    printf('module s-expr printed (in memory, caller-owned):\n%s\n', text)
    # TODO: Redundant in Python, free(text)

    BinaryenModuleDispose(module)


def test_interpret():
    # create a simple module with a start method that prints a number, and
    # interpret it, printing that number.
    module = BinaryenModuleCreate()

    iparams = [BinaryenTypeInt32()]
    BinaryenAddFunctionImport(module,
                              'print-i32',
                              'spectest',
                              'print',
                              BinaryenTypeInt32(),
                              BinaryenTypeNone())

    callOperands = [makeInt32(module, 1234)]
    call = BinaryenCall(module, 'print-i32', callOperands, BinaryenTypeNone())
    starter = BinaryenAddFunction(
        module, 'starter', BinaryenTypeNone(), BinaryenTypeNone(), None, call)
    BinaryenSetStart(module, starter)

    BinaryenModulePrint(module)
    assert (BinaryenModuleValidate(module))
    BinaryenModuleInterpret(module)
    BinaryenModuleDispose(module)


def test_nonvalid():
    # create a module that fails to validate
    module = BinaryenModuleCreate()

    localTypes = [BinaryenTypeInt32()]
    func = BinaryenAddFunction(
        module,
        'func',
        BinaryenTypeNone(),
        BinaryenTypeNone(),
        localTypes,
        BinaryenLocalSet(module, 0, makeInt64(module, 1234))  # wrong type!
    )

    BinaryenModulePrint(module)
    printf('validation: %d\n', BinaryenModuleValidate(module))

    BinaryenModuleDispose(module)


def test_color_status():
    # save old state
    old_state = BinaryenAreColorsEnabled()

    # Check that we can set the state to both {0, 1}
    for flag in (False, True):
        BinaryenSetColorsEnabled(flag)
        assert (BinaryenAreColorsEnabled() == flag)

    BinaryenSetColorsEnabled(old_state)


def test_for_each():
    module = BinaryenModuleCreate()
    fns = [
        BinaryenAddFunction(module,
                            'fn0',
                            BinaryenTypeNone(),
                            BinaryenTypeNone(),
                            None,
                            BinaryenNop(module)),
        BinaryenAddFunction(module,
                            'fn1',
                            BinaryenTypeNone(),
                            BinaryenTypeNone(),
                            None,
                            BinaryenNop(module)),
        BinaryenAddFunction(module,
                            'fn2',
                            BinaryenTypeNone(),
                            BinaryenTypeNone(),
                            None,
                            BinaryenNop(module)),
    ]
    for idx in range(BinaryenGetNumFunctions(module)):
        assert (BinaryenGetFunctionByIndex(module, idx) == fns[idx])

    exps = [
        BinaryenAddFunctionExport(module, 'fn0', 'export0'),
        BinaryenAddFunctionExport(module, 'fn1', 'export1'),
        BinaryenAddFunctionExport(module, 'fn2', 'export2'),
    ]
    for idx in range(BinaryenGetNumExports(module)):
        assert (BinaryenGetExportByIndex(module, idx) == exps[idx])

    segments = [b'hello, world', b'segment data 2']
    expected_offsets = [10, 125]
    segmentPassive = [False, False]
    segmentSizes = [12, 14]

    segmentOffsets = [
        BinaryenConst(module, BinaryenLiteralInt32(expected_offsets[0])),
        BinaryenGlobalGet(module, 'a-global', BinaryenTypeInt32())
    ]
    BinaryenSetMemory(module,
                      1,
                      256,
                      'mem',
                      segments,
                      segmentPassive,
                      segmentOffsets,
                      segmentSizes,
                      False,
                      False,
                      '0')
    BinaryenAddGlobal(module,
                      'a-global',
                      BinaryenTypeInt32(),
                      False,
                      makeInt32(module, expected_offsets[1]))

    for idx in range(BinaryenGetNumMemorySegments(module)):
        assert (BinaryenGetMemorySegmentByteOffset(module, idx) == expected_offsets[idx])
        assert (BinaryenGetMemorySegmentByteLength(module, idx) == segmentSizes[idx])
        out = BinaryenCopyMemorySegmentData(module, idx)
        assert (segments[idx] == out)

    funcNames = [
        BinaryenFunctionGetName(fns[0]),
        BinaryenFunctionGetName(fns[1]),
        BinaryenFunctionGetName(fns[2])
    ]

    constExprRef = BinaryenConst(module, BinaryenLiteralInt32(0))
    BinaryenAddTable(module, '0', 1, 1, BinaryenTypeFuncref())
    BinaryenAddActiveElementSegment(
        module, '0', '0', funcNames, constExprRef)
    assert (1 == BinaryenGetNumElementSegments(module))
    segment = BinaryenGetElementSegmentByIndex(module, 0)
    assert (constExprRef == BinaryenElementSegmentGetOffset(segment))

    for idx in range(BinaryenElementSegmentGetLength(segment)):
        res = BinaryenElementSegmentGetData(segment, idx)
        assert (funcNames[idx] == res)

    BinaryenModulePrint(module)
    BinaryenModuleDispose(module)


def test_func_opt():
    module = BinaryenModuleCreate()
    ii_ = [BinaryenTypeInt32(), BinaryenTypeInt32()]
    ii = BinaryenTypeCreate(ii_)
    x = BinaryenConst(module, BinaryenLiteralInt32(1))
    y = BinaryenConst(module, BinaryenLiteralInt32(3))
    add = BinaryenBinary(module, BinaryenAddInt32(), x, y)
    adder = BinaryenAddFunction(
        module, 'adder', BinaryenTypeNone(), BinaryenTypeInt32(), None, add)

    puts('module with a function to optimize:')
    BinaryenModulePrint(module)

    assert (BinaryenModuleValidate(module))

    BinaryenFunctionOptimize(adder, module)

    assert (BinaryenModuleValidate(module))

    puts('optimized:')
    BinaryenModulePrint(module)

    BinaryenModuleDispose(module)


def test_typesystem():
    defaultTypeSystem = BinaryenGetTypeSystem()
    assert (defaultTypeSystem == BinaryenTypeSystemEquirecursive())
    printf('BinaryenTypeSystemEquirecursive: %d\n',
           BinaryenTypeSystemEquirecursive())
    BinaryenSetTypeSystem(BinaryenTypeSystemNominal())
    assert (BinaryenGetTypeSystem() == BinaryenTypeSystemNominal())
    printf('BinaryenTypeSystemNominal: %d\n', BinaryenTypeSystemNominal())
    BinaryenSetTypeSystem(BinaryenTypeSystemIsorecursive())
    assert (BinaryenGetTypeSystem() == BinaryenTypeSystemIsorecursive())
    printf('BinaryenTypeSystemIsorecursive: %d\n',
           BinaryenTypeSystemIsorecursive())
    BinaryenSetTypeSystem(defaultTypeSystem)


def test_typebuilder():
    defaultTypeSystem = BinaryenGetTypeSystem()
    BinaryenSetTypeSystem(BinaryenTypeSystemIsorecursive())

    printf('TypeBuilderErrorReasonSelfSupertype: %d\n',
           TypeBuilderErrorReasonSelfSupertype())
    printf('TypeBuilderErrorReasonInvalidSupertype: %d\n',
           TypeBuilderErrorReasonInvalidSupertype())
    printf('TypeBuilderErrorReasonForwardSupertypeReference: %d\n',
           TypeBuilderErrorReasonForwardSupertypeReference())
    printf('TypeBuilderErrorReasonForwardChildReference: %d\n',
           TypeBuilderErrorReasonForwardChildReference())

    builder = TypeBuilderCreate(0)
    assert (TypeBuilderGetSize(builder) == 0)
    TypeBuilderGrow(builder, 5)
    assert (TypeBuilderGetSize(builder) == 5)

    # Create a recursive array of its own type
    tempArrayIndex = 0
    tempArrayHeapType = TypeBuilderGetTempHeapType(builder, tempArrayIndex)
    tempArrayType = TypeBuilderGetTempRefType(builder, tempArrayHeapType, True)
    TypeBuilderSetArrayType(builder,
                            tempArrayIndex,
                            tempArrayType,
                            BinaryenPackedTypeNotPacked(),
                            True)

    # Create a recursive struct with a field of its own type
    tempStructIndex = 1
    tempStructHeapType = TypeBuilderGetTempHeapType(builder, tempStructIndex)
    tempStructType = TypeBuilderGetTempRefType(builder, tempStructHeapType, True)

    fieldTypes = [tempStructType]
    fieldPackedTypes = [BinaryenPackedTypeNotPacked()]
    fieldMutables = [True]
    TypeBuilderSetStructType(
        builder, tempStructIndex, fieldTypes, fieldPackedTypes, fieldMutables)

    # Create a recursive signature with parameter and result including its own
    # type
    tempSignatureIndex = 2
    tempSignatureHeapType = TypeBuilderGetTempHeapType(builder, tempSignatureIndex)
    tempSignatureType = TypeBuilderGetTempRefType(builder, tempSignatureHeapType, True)

    paramTypes = [tempSignatureType, tempArrayType]
    TypeBuilderSetSignatureType(
        builder,
        tempSignatureIndex,
        TypeBuilderGetTempTupleType(builder, paramTypes),  # (BinaryenType*)
        tempSignatureType)

    # Create a basic heap type
    tempBasicIndex = 3
    TypeBuilderSetBasicHeapType(
        builder, 3, BinaryenTypeGetHeapType(BinaryenTypeEqref()))
    assert (TypeBuilderIsBasic(builder, tempBasicIndex))
    assert (TypeBuilderGetBasic(builder, tempBasicIndex) ==
            BinaryenTypeGetHeapType(BinaryenTypeEqref()))
    assert (not TypeBuilderIsBasic(builder, tempArrayIndex))
    assert (not TypeBuilderIsBasic(builder, tempStructIndex))
    assert (not TypeBuilderIsBasic(builder, tempSignatureIndex))

    # Create a subtype (with an additional immutable packed field)
    tempSubStructIndex = 4
    tempSubStructHeapType = TypeBuilderGetTempHeapType(builder, tempSubStructIndex)
    tempSubStructType = TypeBuilderGetTempRefType(builder, tempSubStructHeapType, True)

    fieldTypes = [tempStructType, BinaryenTypeInt32()]  # must repeat existing fields
    fieldPackedTypes = [BinaryenPackedTypeNotPacked(), BinaryenPackedTypeInt8()]
    fieldMutables = [True, False]
    TypeBuilderSetStructType(builder,
                             tempSubStructIndex,
                             fieldTypes,
                             fieldPackedTypes,
                             fieldMutables)

    TypeBuilderSetSubType(builder, tempSubStructIndex, tempStructHeapType)

    # TODO: Rtts (post-MVP?)

    # Build the type hierarchy and dispose the builder
    # BinaryenHeapType heapTypes[5]
    # BinaryenIndex errorIndex
    # TypeBuilderErrorReason errorReason
    didBuildAndDispose, errorIndex, errorReason = TypeBuilderBuildAndDispose(builder, heapTypes := [])
    assert didBuildAndDispose

    arrayHeapType = heapTypes[tempArrayIndex]
    assert (not BinaryenHeapTypeIsBasic(arrayHeapType))
    assert (not BinaryenHeapTypeIsSignature(arrayHeapType))
    assert (not BinaryenHeapTypeIsStruct(arrayHeapType))
    assert (BinaryenHeapTypeIsArray(arrayHeapType))
    assert (not BinaryenHeapTypeIsBottom(arrayHeapType))
    assert (BinaryenHeapTypeIsSubType(arrayHeapType, BinaryenHeapTypeArray()))
    arrayType = BinaryenTypeFromHeapType(arrayHeapType, True)
    assert (BinaryenArrayTypeGetElementType(arrayHeapType) == arrayType)
    assert (BinaryenArrayTypeGetElementPackedType(arrayHeapType) ==
            BinaryenPackedTypeNotPacked())
    assert (BinaryenArrayTypeIsElementMutable(arrayHeapType))

    structHeapType = heapTypes[tempStructIndex]
    assert (not BinaryenHeapTypeIsBasic(structHeapType))
    assert (not BinaryenHeapTypeIsSignature(structHeapType))
    assert (BinaryenHeapTypeIsStruct(structHeapType))
    assert (not BinaryenHeapTypeIsArray(structHeapType))
    assert (not BinaryenHeapTypeIsBottom(structHeapType))
    assert (BinaryenHeapTypeIsSubType(structHeapType, BinaryenHeapTypeData()))
    structType = BinaryenTypeFromHeapType(structHeapType, True)
    assert (BinaryenStructTypeGetNumFields(structHeapType) == 1)
    assert (BinaryenStructTypeGetFieldType(structHeapType, 0) == structType)
    assert (BinaryenStructTypeGetFieldPackedType(structHeapType, 0) ==
            BinaryenPackedTypeNotPacked())
    assert (BinaryenStructTypeIsFieldMutable(structHeapType, 0))

    signatureHeapType = heapTypes[tempSignatureIndex]
    assert (not BinaryenHeapTypeIsBasic(signatureHeapType))
    assert (BinaryenHeapTypeIsSignature(signatureHeapType))
    assert (not BinaryenHeapTypeIsStruct(signatureHeapType))
    assert (not BinaryenHeapTypeIsArray(signatureHeapType))
    assert (not BinaryenHeapTypeIsBottom(signatureHeapType))
    assert (BinaryenHeapTypeIsSubType(signatureHeapType, BinaryenHeapTypeFunc()))
    signatureType = BinaryenTypeFromHeapType(signatureHeapType, True)
    signatureParams = BinaryenSignatureTypeGetParams(signatureHeapType)
    assert (BinaryenTypeArity(signatureParams) == 2)
    # expandedSignatureParams[2]
    expandedSignatureParams = BinaryenTypeExpand(signatureParams)
    assert (expandedSignatureParams[0] == signatureType)
    assert (expandedSignatureParams[1] == arrayType)
    signatureResults = BinaryenSignatureTypeGetResults(signatureHeapType)
    assert (BinaryenTypeArity(signatureResults) == 1)
    assert (signatureResults == signatureType)

    basicHeapType = heapTypes[tempBasicIndex]  # = eq
    assert (BinaryenHeapTypeIsBasic(basicHeapType))
    assert (not BinaryenHeapTypeIsSignature(basicHeapType))
    assert (not BinaryenHeapTypeIsStruct(basicHeapType))
    assert (not BinaryenHeapTypeIsArray(basicHeapType))
    assert (not BinaryenHeapTypeIsBottom(basicHeapType))
    assert (BinaryenHeapTypeIsSubType(basicHeapType, BinaryenHeapTypeAny()))
    basicType = BinaryenTypeFromHeapType(basicHeapType, True)

    subStructHeapType = heapTypes[tempSubStructIndex]
    assert (not BinaryenHeapTypeIsBasic(subStructHeapType))
    assert (not BinaryenHeapTypeIsSignature(subStructHeapType))
    assert (BinaryenHeapTypeIsStruct(subStructHeapType))
    assert (not BinaryenHeapTypeIsArray(subStructHeapType))
    assert (not BinaryenHeapTypeIsBottom(subStructHeapType))
    assert (BinaryenHeapTypeIsSubType(subStructHeapType, BinaryenHeapTypeData()))
    assert (BinaryenHeapTypeIsSubType(subStructHeapType, structHeapType))
    subStructType = BinaryenTypeFromHeapType(subStructHeapType, True)
    assert (BinaryenStructTypeGetNumFields(subStructHeapType) == 2)
    assert (BinaryenStructTypeGetFieldType(subStructHeapType, 0) == structType)
    assert (BinaryenStructTypeGetFieldType(subStructHeapType, 1) ==
            BinaryenTypeInt32())
    assert (BinaryenStructTypeGetFieldPackedType(subStructHeapType, 0) ==
            BinaryenPackedTypeNotPacked())
    assert (BinaryenStructTypeGetFieldPackedType(subStructHeapType, 1) ==
            BinaryenPackedTypeInt8())
    assert (BinaryenStructTypeIsFieldMutable(subStructHeapType, 0))
    assert (not BinaryenStructTypeIsFieldMutable(subStructHeapType, 1))

    # Build a simple test module, validate and print it
    module = BinaryenModuleCreate()
    BinaryenModuleSetTypeName(module, arrayHeapType, 'SomeArray')
    BinaryenModuleSetTypeName(module, structHeapType, 'SomeStruct')
    BinaryenModuleSetFieldName(module, structHeapType, 0, 'SomeField')
    BinaryenModuleSetTypeName(module, signatureHeapType, 'SomeSignature')
    BinaryenModuleSetTypeName(module, basicHeapType, 'does-nothing')
    BinaryenModuleSetTypeName(module, subStructHeapType, 'SomeSubStruct')
    BinaryenModuleSetFieldName(module, subStructHeapType, 0, 'SomeField')
    BinaryenModuleSetFieldName(module, subStructHeapType, 1, 'SomePackedField')
    BinaryenModuleSetFeatures(
        module, BinaryenFeatureReferenceTypes() | BinaryenFeatureGC())

    varTypes = [arrayType, structType, signatureType, basicType, subStructType]
    BinaryenAddFunction(module,
                        'test',
                        BinaryenTypeNone(),
                        BinaryenTypeNone(),
                        varTypes,
                        BinaryenNop(module))

    didValidate = BinaryenModuleValidate(module)
    assert didValidate
    printf('module with recursive GC types:\n')
    BinaryenModulePrint(module)
    BinaryenModuleDispose(module)

    BinaryenSetTypeSystem(defaultTypeSystem)


def main():
    test_types()
    test_features()
    test_core()
    test_unreachable()
    test_relooper()
    test_binaries()
    test_interpret()
    test_nonvalid()
    test_color_status()
    test_for_each()
    test_func_opt()
    test_typesystem()
    test_typebuilder()


if __name__ == '__main__':
    main()
