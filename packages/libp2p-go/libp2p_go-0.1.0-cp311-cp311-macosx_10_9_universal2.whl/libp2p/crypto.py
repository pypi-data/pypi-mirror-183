import enum
from typing import Self
from ctypes import *
from libp2p.utils import *


lib = load_library()


KeyType = enum.Enum('KeyType', ['RSA', 'Ed25519', 'Secp256k1', 'ECDSA', ], start=0)


class PrivKey(SimpleFreeMixin):
    lib.privkey_delete.argtypes = [c_size_t, ]
    _FREE = lib.privkey_delete
    lib.crypto_marshalPrivateKey.argtypes = [c_size_t, ]
    lib.crypto_marshalPrivateKey.restype = MsgpackBody
    _MARSHAL = lib.crypto_marshalPrivateKey
    lib.crypto_unmarshalPrivateKey.argtypes = [c_size_t, POINTER(c_ubyte), ]
    lib.crypto_unmarshalPrivateKey.restype = MsgpackBody
    _UNMARSHAL = lib.crypto_unmarshalPrivateKey

    def __init__(self, handle: int):
        self.handle = handle

    def marshal(self) -> bytes:
        result: MsgpackBody = self._MARSHAL(self.handle)
        result.raise_error()
        return result.bytes.first()

    @classmethod
    def unmarshal(cls, data: bytes) -> Self:
        buffer = (c_ubyte * len(data)).from_buffer(bytearray(data))
        result: MsgpackBody = cls._UNMARSHAL(len(data), buffer)
        result.raise_error()
        return PrivKey(result.handles.first())


class PubKey(SimpleFreeMixin):
    lib.pubkey_delete.argtypes = [c_size_t, ]
    _FREE = lib.pubkey_delete
    lib.crypto_marshalPublicKey.argtypes = [c_size_t, ]
    lib.crypto_marshalPublicKey.restype = MsgpackBody
    _MARSHAL = lib.crypto_marshalPublicKey
    lib.crypto_unmarshalPublicKey.argtypes = [c_size_t, POINTER(c_ubyte), ]
    lib.crypto_unmarshalPublicKey.restype = MsgpackBody
    _UNMARSHAL = lib.crypto_unmarshalPublicKey

    def __init__(self, handle: int):
        self.handle = handle

    def marshal(self) -> bytes:
        result: MsgpackBody = self._MARSHAL(self.handle)
        result.raise_error()
        return result.bytes.first()

    @classmethod
    def unmarshal(cls, data: bytes) -> Self:
        buffer = (c_ubyte * len(data)).from_buffer(bytearray(data))
        result: MsgpackBody = cls._UNMARSHAL(len(data), buffer)
        result.raise_error()
        return PubKey(result.handles.first())


lib.crypto_generateKeyPairWithReader.argtypes = [c_longlong, c_longlong, c_longlong, ]
lib.crypto_generateKeyPairWithReader.restype = MsgpackBody
_GENERATE_KEYPAIR_WITH_READER = lib.crypto_generateKeyPairWithReader
lib.crypto_generateKeyPair.argtypes = [c_longlong, c_longlong, ]
lib.crypto_generateKeyPair.restype = MsgpackBody
_GENERATE_KEYPAIR = lib.crypto_generateKeyPair


def crypto_generate_keypair_with_reader(typ: KeyType, bits: int, randseed: int) -> tuple[PrivKey, PubKey]:
    result: MsgpackBody = _GENERATE_KEYPAIR_WITH_READER(typ.value, bits, randseed)
    result.raise_error()
    handles = result.handles
    priv, pub = handles.take(2)
    return PrivKey(priv), PubKey(pub)


def crypto_generate_keypair(typ: KeyType, bits: int) -> tuple[PrivKey, PubKey]:
    result: MsgpackBody = _GENERATE_KEYPAIR(typ.value, bits)
    result.raise_error()
    handles = result.handles
    priv, pub = handles.take(2)
    return PrivKey(priv), PubKey(pub)


__all__ = [
    'KeyType',
    'PrivKey',
    'PubKey',
    'crypto_generate_keypair_with_reader',
    'crypto_generate_keypair',
]
