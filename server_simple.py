# -*- coding: utf-8 -

# from gevent import monkey
# monkey.patch_all()

# import grpc._cython.cygrpc
# grpc._cython.cygrpc.init_grpc_gevent()

from gevent import monkey
monkey.patch_all()

import grpc._cython.cygrpc
grpc._cython.cygrpc.init_grpc_gevent()

import os
import time
import grpc
from concurrent import futures


import settings
from protoclasses import api_pb2_grpc
from api import ArghusServerServicer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RPCServer(object):
    def __init__(self, addr, worker_connections):
        self.server = grpc.server(futures.ThreadPoolExecutor(
            max_workers=worker_connections))
        api_pb2_grpc.add_ServerApiServicer_to_server(
            ArghusServerServicer(), self.server)
        self.server.add_insecure_port(addr)

    def start(self):
        self.server.start()
        # ConsulClient().register([])

    def stop(self, grace=5):
        self.server.stop(grace)


if __name__ == '__main__':
    os.environ['GRPC_ENABLE_FORK_SUPPORT'] = 'False'
    server = RPCServer(settings.ADDR, settings.CONN)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
