# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from protoclasses import api_pb2, api_pb2_grpc


class ArghusServerServicer(api_pb2_grpc.ServerApiServicer):
    total = 0
    cur_time = pre_time = None

    def api_upload_metrics(self, request, context):
        # print(request)
        self.total += 1
        if self.pre_time is None:
            self.pre_time = datetime.now()
        self.cur_time = datetime.now()
        if self.cur_time - self.pre_time >= timedelta(seconds=1):
            print('api upload total time is %s at %s' % (self.total, self.cur_time))
            self.pre_time = self.cur_time
            self.total = 0
        return api_pb2.SimpleResp(code=40000, msg='')
