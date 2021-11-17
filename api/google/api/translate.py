# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/10 9:56

import execjs
import requests

lang_dict = {'中文': 'zh-CN', '阿尔巴尼亚语': 'sq', '阿拉伯语': 'ar',
             '阿姆哈拉语': 'am', '阿塞拜疆语': 'az', '爱尔兰语': 'ga',
             '爱沙尼亚语': 'et', '巴斯克语': 'eu', '白俄罗斯语': 'be',
             '保加利亚语': 'bg', '冰岛语': 'is', '波兰语': 'pl', '波斯尼亚语': 'bs',
             '波斯语': 'fa', '布尔语': 'af', '丹麦语': 'da', '德语': 'de', '俄语': 'ru', '法语': 'fr',
             '菲律宾语': 'tl', '芬兰语': 'fi', '弗里西语': 'fy', '高棉语': 'km', '格鲁吉亚语': 'ka',
             '古吉拉特语': 'gu', '哈萨克语': 'kk', '海地克里奥尔语': 'ht', '韩语': 'ko',
             '豪萨语': 'ha', '荷兰语': 'nl', '吉尔吉斯语': 'ky', '加利西亚语': 'gl', '加泰罗尼亚语': 'ca',
             '捷克语': 'cs', '卡纳达语': 'kn', '科西嘉语': 'co', '克罗地亚语': 'hr',
             '库尔德语': 'ku', '拉丁语': 'la', '拉脱维亚语': 'lv', '老挝语': 'lo', '立陶宛语': 'lt',
             '卢森堡语': 'lb', '罗马尼亚语': 'ro', '马尔加什语': 'mg', '马耳他语': 'mt',
             '马拉地语': 'mr', '马拉雅拉姆语': 'mf', '马来语': 'ms', '马其顿语': 'mk',
             '毛利语': 'mi', '蒙古语': 'mn', '孟加拉语': 'bn', '缅甸语': 'my', '苗语': 'hmn', '南非克萨语': 'xh', '南非祖鲁语': 'zu',
             '尼泊尔语': 'ne', '挪威语': 'no', '旁遮普语': 'pa', '葡萄牙语': 'pt', '普什图语': 'ps',
             '齐切瓦语': 'ny', '日语': 'ja', '瑞典语': 'sv', '萨摩亚语': 'sm', '塞尔维亚语': 'sr',
             '赛所托语': 'st', '僧伽罗语': 'si', '世界语': 'eo', '斯洛伐克语': 'sk', '斯洛文尼亚语': 'sl',
             '斯瓦希里语': 'sw', '苏格兰盖尔语': 'gd', '宿务语': 'ceb', '索马里语': 'so', '塔吉克语': 'tg', '泰卢固语': 'te',
             '泰米尔语': 'ta', '泰语': 'th', '土耳其语': 'tr', '威尔士语': 'cy', '乌尔都语': 'ur',
             '乌克兰语': 'uk', '乌兹别克语': 'uz', '西班牙语': 'es', '希伯来语': 'rw', '希腊语': 'el',
             '夏威夷语': 'haw', '信德语': 'sd', '匈牙利语': 'hu', '修纳语': 'sn',
             '亚美尼亚语': 'hy', '伊博语': 'ig', '意大利语': 'it', '意第绪语': 'yi', '印地语': 'hi',
             '印尼巽他': 'su', '印尼语': 'id', '印尼爪哇语': 'jw', '英语': 'en', '约鲁巴语': 'yo', '越南语': 'vi', '中文繁体': 'zh-TW'}


def google_translate(params):
    """谷歌翻译

    Args:
        params (dict): {from: 源语言, to: 翻译语言, content: 翻译内容}

    Returns:
        json: {result: 翻译后的内容}
    """

    with open('../js/translate.js', 'r', encoding='UTF-8') as file:
        js_text = file.read()
        # 编译加载js字符串
        js = execjs.compile(js_text)
        tk = js.call("TL", str(params['content']))

    if len(params['content']) > 4891:
        return {'error': '内容过长'}
    else:
        url = "http://translate.google.cn/translate_a/single?client=t" \
              "&sl={}&tl={}&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
              "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
              "&srcrom=0&ssel=0&tsel=0&kc=2&tk={}&q={}".format(lang_dict[params['from']], lang_dict[params['to']], tk,
                                                               params['content'])
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'referer': 'https://translate.google.cn/',
            'authority': 'translate.google.cn'
        }
        response = requests.get(url=url, headers=headers)

        end = response.text.find("\",")
        if end > 4:
            message = response.text[4:end]
        else:
            return {'error': '翻译失败'}
        return {'result': message}


if __name__ == '__main__':
    print(google_translate({'from': '英语', 'to': '中文', 'content': 'Hello World'}))
