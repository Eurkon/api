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
        path = str(urlparse(self.path))
        print(path)
        params = dict(parse.parse_qsl(urlparse(self.path).query))
        if len(params) > 0:
            try:
                api = params['api']
                del params['api']
                data = eval("{0}".format(api))(params)
            except Exception as e:
                data = json.dumps({'error': e}).encode('utf-8')

            if isinstance(data, bytes):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')

            elif isinstance(data, str):
                self.send_response(301)
                self.send_header('Location', data)
                if data.endswith('.png'):
                    self.send_header('Content-type', 'image/png')
                elif data.endswith('.jpg'):
                    self.send_header('Content-type', 'image/jpeg')
                elif data.endswith('.html'):
                    self.send_header('Content-type', 'text/html')
                elif data.endswith('.xml'):
                    self.send_header('Content-type', 'application/xml')
                elif data.endswith('.pdf'):
                    self.send_header('Content-type', 'application/pdf')
                elif data.endswith('.txt'):
                    self.send_header('Content-type', 'application/octet-stream')
                else:
                    self.send_header('Content-type', 'text/plain')
            else:
                self.send_header('Content-type', 'text/plain')

            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            if isinstance(data, bytes):
                self.wfile.write(data)
        else:

            if path.endswith('.png'):
                self.send_header('Content-type', 'image/png')
            elif path.endswith('.jpg'):
                self.send_header('Content-type', 'image/jpeg')
            elif path.endswith('.html'):
                self.send_header('Content-type', 'text/html')
            elif path.endswith('.xml'):
                self.send_header('Content-type', 'application/xml')
            elif path.endswith('.pdf'):
                self.send_header('Content-type', 'application/pdf')
            elif path.endswith('.txt'):
                self.send_header('Content-type', 'application/octet-stream')
            else:
                self.send_header('Content-type', 'text/plain')
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
        return
