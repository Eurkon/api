# -*- coding: utf-8 -*-
# @Author   : Eurkon
# @Date     : 2021/11/10 16:32

import requests
from hashlib import md5
import time
import random


def translate(content: str = 'Hello World'):
    """有道翻译

    Args:
        content: 翻译内容

    Returns:
        dict: {result: 翻译后的内容}
    """
    # 请求地址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    appVersion = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '244',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1506602845@10.169.0.82; JSESSIONID=aaaUggpd8kfhja1AIJYpx; OUTFOX_SEARCH_USER_ID_NCOO=108436537.92676207; ___rl__test__cookies=1597502296408',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'user-agent': appVersion,
        'X-Requested-With': 'XMLHttpRequest',
    }

    word = content
    bv = md5(appVersion.encode()).hexdigest()
    lts = str(int(time.time() * 1000))
    salt = lts + str(random.randint(0, 9))
    sign = md5(('fanyideskweb' + word + salt + ']BjuETDhU)zqSxf-=B#7m').encode()).hexdigest()
    params = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    response = requests.post(url=url, headers=headers, data=params)
    result = response.json()
    return {'result': result['translateResult'][0][0]['tgt']}


if __name__ == '__main__':
    print(translate('Hello World'))
