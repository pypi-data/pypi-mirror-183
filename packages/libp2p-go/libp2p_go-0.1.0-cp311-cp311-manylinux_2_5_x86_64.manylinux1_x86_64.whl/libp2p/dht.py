import asyncio
from ctypes import *
from libp2p import Host
from libp2p.utils import *

lib = load_library()


class DHT(SimpleFreeMixin):
    lib.dht_new.argtypes = [c_size_t, MsgpackArg, ]
    lib.dht_new.restype = MsgpackBody
    _INIT = lib.dht_new
    lib.dht_delete.argtypes = [c_size_t, ]
    _FREE = lib.dht_delete
    lib.dht_bootstrap.argtypes = [c_size_t, ]
    lib.dht_bootstrap.restype = MsgpackBody
    _BOOTSTRAP = lib.dht_bootstrap
    lib.dht_defaultBootstrapPeers.restype = MsgpackBody
    _DEFAULT_BOOTSTRAP_PEERS = lib.dht_defaultBootstrapPeers

    def __init__(self, host: Host):
        result: MsgpackBody = self._INIT(host.handle, MsgpackArg.from_dict(dict()))
        result.raise_error()
        self.handle = result.handles.first()
        self.loop: asyncio.AbstractEventLoop = host.io_loop

    def bootstrap(self):
        result: MsgpackBody = self._BOOTSTRAP(self.handle)
        result.raise_error()

    @classmethod
    def defaultBootstrapPeers(cls) -> list[str]:
        result: MsgpackBody = cls._DEFAULT_BOOTSTRAP_PEERS()
        result.raise_error()
        return result.strings


__all__ = ['DHT']
