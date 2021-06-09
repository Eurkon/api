# -*- coding: utf-8 -*-
# @Author    : Eurkon
# @Date      : 2021/6/5 10:19

import json
import requests


def baidu_tongji(params):
    """重定向请求百度统计，解决跨域问题

    Args:
        params (dict): 参数字典，包括 site_id, access_token 等

    Returns:
        百度统计返回的 json
    """
    url = 'https://openapi.baidu.com/rest/2.0/tongji/report/getData?'
    req = requests.post(url=url, data=params)
    data = req.json()

    return json.dumps(data).encode('utf-8')