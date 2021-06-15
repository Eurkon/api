# -*- coding: utf-8 -*-
# @Author    : Eurkon
# @Date      : 2021/6/5 10:19

import requests


def baidu_tongji(params):
    """重定向请求百度统计，解决跨域问题

    Args:
        params (dict): {site_id: 网站id, access_token: token, ...}

    Returns:
        json: 百度统计返回的网页统计数据
    """
    url = 'https://openapi.baidu.com/rest/2.0/tongji/report/getData?'
    req = requests.post(url=url, data=params)
    data = req.json()

    return data