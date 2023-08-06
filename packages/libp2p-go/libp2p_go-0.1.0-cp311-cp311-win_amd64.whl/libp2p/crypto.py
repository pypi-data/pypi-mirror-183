import enum
from ctypes import *
from libp2p.utils import *


lib = load_library()


KeyType = enum.Enum('KeyType', ['RSA', 'Ed25519', 'Secp256k1', 'ECDSA', ], start=0)


class PrivKey(SimpleFreeMixin):
    lib.privkey_delete.argtypes = [c_size_t, ]
    _FREE = lib.privkey_delete

    def __init__(self, handle: int):
        self.handle = handle


class PubKey(SimpleFreeMixin):
    lib.pubkey_delete.argtypes = [c_size_t, ]
    _FREE = lib.pubkey_delete

    def __init__(self, handle: int):
        self.handle = handle


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
