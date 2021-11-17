# -*- coding: utf-8 -*-
# @Author   : Eurkon
# @Date     : 2021/11/9 9:44

import requests
import re
import execjs

lang_dict = {'中文': 'zh', '日语': 'jp', '日语假名': 'jpka', '泰语': 'th', '法语': 'fra', '英语': 'en', '西班牙语': 'spa',
             '韩语': 'kor',
             '土耳其语': 'tr', '越南语': 'vie', '马来语': 'ms', '德语': 'de', '俄语': 'ru', '伊朗语': 'ir', '阿拉伯语': 'ara',
             '爱沙尼亚语': 'est',
             '白俄罗斯语': 'be', '保加利亚语': 'bul', '印地语': 'hi', '冰岛语': 'is', '波兰语': 'pl', '波斯语': 'fa', '丹麦语': 'dan',
             '菲律宾语': 'tl',
             '芬兰语': 'fin', '荷兰语': 'nl', '加泰罗尼亚语': 'ca', '捷克语': 'cs', '克罗地亚语': 'hr', '拉脱维亚语': 'lv', '立陶宛语': 'lt',
             '罗马尼亚语': 'rom',
             '南非语': 'af', '挪威语': 'no', '巴西语': 'pt_BR', '葡萄牙语': 'pt', '瑞典语': 'swe', '塞尔维亚语': 'sr', '世界语': 'eo',
             '斯洛伐克语': 'sk',
             '斯洛文尼亚语': 'slo', '斯瓦希里语': 'sw', '乌克兰语': 'uk', '希伯来语': 'iw', '希腊语': 'el', '匈牙利语': 'hu', '亚美尼亚语': 'hy',
             '意大利语': 'it',
             '印尼语': 'id', '阿尔巴尼亚语': 'sq', '阿姆哈拉语': 'am', '阿萨姆语': 'as', '阿塞拜疆语': 'az', '巴斯克语': 'eu', '孟加拉语': 'bn',
             '波斯尼亚语': 'bs',
             '加利西亚语': 'gl', '格鲁吉亚语': 'ka', '古吉拉特语': 'gu', '豪萨语': 'ha', '伊博语': 'ig', '因纽特语': 'iu', '爱尔兰语': 'ga',
             '祖鲁语': 'zu',
             '卡纳达语': 'kn', '哈萨克语': 'kk', '吉尔吉斯语': 'ky', '卢森堡语': 'lb', '马其顿语': 'mk', '马耳他语': 'mt', '毛利语': 'mi',
             '马拉提语': 'mr',
             '尼泊尔语': 'ne', '奥利亚语': 'or', '旁遮普语': 'pa', '凯楚亚语': 'qu', '塞茨瓦纳语': 'tn', '僧加罗语': 'si', '泰米尔语': 'ta',
             '塔塔尔语': 'tt',
             '泰卢固语': 'te', '乌尔都语': 'ur', '乌兹别克语': 'uz', '威尔士语': 'cy', '约鲁巴语': 'yo', '粤语': 'yue', '文言文': 'wyw',
             '中文繁体': 'cht'}

url = 'https://fanyi.baidu.com/v2transapi'
headers = {
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}


def baidu_translate(params):
    """百度翻译

    Args:
        params (dict): {from: 源语言, to: 翻译语言, content: 翻译内容}

    Returns:
        json: {result: 翻译后的内容}
    """
    # 多次请求保证获取 token，并用此 token 进行翻译
    session = requests.Session()
    session.headers = headers

    session.get(url='https://fanyi.baidu.com/', headers=headers)
    html = session.get(url='https://fanyi.baidu.com/', headers=headers).text
    token = re.findall(r"token: '(.*?)'", html)[0]
    gtk = re.findall(r"window.gtk = '(.*?)';", html)[0]

    with open('../js/translate.js', 'r', encoding='UTF-8') as file:
        js_text = file.read()
        # 编译加载js字符串
        js = execjs.compile(js_text)
        sign = js.call("e", params['content'], gtk)

    params = {
        'from': lang_dict[params['from']],
        'to': lang_dict[params['to']],
        'query': params['content'],
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
        'domain': 'common'
    }

    response = session.get(url=url, headers=headers, params=params)
    message = response.json()
    return {'result': message['trans_result']['data'][0]['dst']}


if __name__ == '__main__':
    print(baidu_translate({'from': '英语', 'to': '中文', 'content': 'Hello World'}))
