# -*- coding: utf-8 -*-

import sys
import os
import time
import grpc
from concurrent import futures
from datetime import datetime, timedelta

#import gevent

import settings
from protoclasses import api_pb2, api_pb2_grpc
from api import ArghusServerServicer


# import sys
# import time
# import logging
# import queue
# 
# import grpc
# 
# import demo_pb2
# import demo_pb2_grpc
# 
# queue = queue.Queue()


# def gen_content(name):
#     queue.put(name)
#     while True:
#         content = queue.get()
#         code = 0 if content == name else 1
#         yield demo_pb2.AgentToServer(code=code, content=content)


def run():
    while True:
        p = datetime.now()
        channel = grpc.insecure_channel('localhost:6200')
        stub = api_pb2_grpc.ServerApiStub(channel)
        for i in range(10000000):
            a = api_pb2.ApiMetricsMessage(token="11", service_name="33")
            stub.api_upload_metrics(a)
            # if datetime.now() - p > timedelta(seconds=60):
            #     break
        channel.close()
        # with grpc.insecure_channel('localhost:6100') as channel:
        #     stub = api_pb2_grpc.ServerApiStub(channel)
        #     for i in range(1):
        #         a = api_pb2.ApiMetricsMessage(token="11", service_name="33")
        #         stub.api_upload_metrics(a)

        # it = stub.TransferCommands(gen_content(name))
        # try:
        #     for r in it:
        #         print('Command: {}'.format(r.content))
        #         # 假装在处理
        #         # time.sleep(1)
        #         # queue.put('ok from {}'.format(name))
        # except grpc._channel._Rendezvous as err:
        #     print(err) 

if __name__ == '__main__':
    # logging.basicConfig()
    run()

