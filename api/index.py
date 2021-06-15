# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/3 16:55

import json
from urllib import parse
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler

from api.baidu.api.api import *
from api.google.api.api import *
from api.tools.api.api import *
from api.weibo.api.api import *


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            params = dict(parse.parse_qsl(urlparse(self.path).query))
            if 'api' in params:
                api = str(params['api'])
                del params['api']
                data = eval("{0}".format(api))(params)
            else:
                data = {'error': '请输入API'}
        except Exception as e:
            data = {'error': str(e)}

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        if isinstance(data, bytes):
            res = data
        elif isinstance(data, dict) or isinstance(data, list):
            res = json.dumps(data).encode('utf-8')
        else:
            res = str(data).encode('urf-8')

        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(res)
        return