from typing import Optional, List, Any

from nxbinaryen.binaryen import ffi

__all__ = [
    '_enc', '_enc_seq', '_opt', '_opt_seq', '_len', '_dec',
]


def _enc(value: Optional[str]) -> bytes | ffi.CData:
    if value is None:
        return ffi.NULL
    if isinstance(value, bytes):
        return value
    return value.encode()


def _enc_seq(values: List[str | bytes]) -> Any:
    return [ffi.from_buffer(_enc(item)) for item in values]


def _opt(value: Optional[Any]) -> Any | ffi.CData:
    return ffi.NULL if value is None else value


def _opt_seq(value: Optional[List[Any]]) -> List[Any] | ffi.CData:
    if value is None:
        return ffi.NULL
    if not isinstance(value, list):
        return [value]
    # TODO: Should we avoid list recreate? Seems doable
    # TODO: What's the best type to wrap? Can be a tuple?
    return [_opt(item) for item in value]


def _len(value: Optional[List[Any]]) -> int:
    if value is None:
        return 0
    if isinstance(value, list):
        return len(value)
    return 1


def _dec(value: ffi.CData) -> str:
    return ffi.string(value).decode()
