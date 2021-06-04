# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/3 16:57

import json
import requests
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs


def get_data(params):
    """重定向请求百度统计，解决跨域问题

    Args:
        params (dict): 参数字典，包括 site_id, access_token 等

    Returns:
        百度统计返回的 json
    """
    url = 'https://openapi.baidu.com/rest/2.0/tongji/report/getData?'
    req = requests.post(url=url, data=params)
    data = req.json()
    return data


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        params = parse_qs(path.split('?')[1])
        data = get_data(params)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return