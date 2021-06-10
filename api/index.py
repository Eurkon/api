# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/3 16:55

import json
from urllib import parse
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler

from api.baidu.api.api import *
from api.weibo.api.api import *
from api.google.api.api import *


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            params = dict(parse.parse_qsl(urlparse(self.path).query))
            api = params['api']
            del params['api']
            data = eval("{0}".format(api))(params)
        except Exception as e:
            data = json.dumps({'error': str(e)}).encode('utf-8')

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(data)
        return

if __name__ == '__main__':
    print(google_translate({'from': '英语', 'to': '中文', 'content': 'Hello World'}))