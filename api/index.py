# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/3 16:55

import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler

from api.weibo.api import *
from api.weibo.api import *


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        try:
            params = parse_qs(self.path.split('?')[1])
            api = params['api']
            del params['api']
            data = eval("{0}".format(api))(params)
        except Exception as e:
            data = {'error': str(e)}

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
