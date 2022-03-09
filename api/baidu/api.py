# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/9 17:13

import requests
import re
import execjs


def tongji(params):
    """重定向请求百度统计，解决跨域问题

    Args:
        params: {site_id: 网站id, access_token: token, ...}

    Returns:
        dict: 百度统计返回的网页统计数据
    """
    url = 'https://openapi.baidu.com/rest/2.0/tongji/report/getData?'
    req = requests.post(url=url, data=params)
    data = req.json()

    return data


def translate(fr: str = '英语', to: str = '中文', content: str = 'Hello World'):
    """百度翻译

    Args:
        fr: 源语言
        to: 翻译语言
        content: 翻译内容

    Returns:
        dict: {result: 翻译后的内容}
    """
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

    # 多次请求保证获取 token，并用此 token 进行翻译
    session = requests.Session()
    session.headers = headers
    session.get(url='https://fanyi.baidu.com/')
    html = session.get(url='https://fanyi.baidu.com/').text
    token = re.findall(r"token: '(.*?)'", html)[0]
    gtk = re.findall(r"window.gtk = '(.*?)';", html)[0]

    js_text = """
    function a (r) {
      if (Array.isArray(r)) {
        for (var o = 0,
          t = Array(r.length); o < r.length; o++) t[o] = r[o];
        return t
      }
      return Array.from(r)
    }

    function n (r, o) {
      for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
          a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
          r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
      }
      return r
    }

    function e (r, u) {
      var o = r.match(/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/g);
      if (null === o) {
        var t = r.length;
        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(- 10, 10));
      } else {
        for (var e = r.split(/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)"" !== e[C] && f.push.apply(f, a(e[C].split(""))),
          C !== h - 1 && f.push(o[C]);
        var g = f.length;
        g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(- 10).join(""));
      }

      var l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
      for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
        var A = r.charCodeAt(v);
        128 > A ? (S[c++] = A) : (2048 > A ? (S[c++] = (A >> 6) | 192) : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? ((A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v))), (S[c++] = (A >> 18) | 240), (S[c++] = ((A >> 12) & 63) | 128)) : (S[c++] = (A >> 12) | 224), (S[c++] = ((A >> 6) & 63) | 128)), (S[c++] = (63 & A) | 128));
      }
      for (var p = m,
        F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)(p += S[b]),
          (p = n(p, F));
      return ((p = n(p, D)), (p ^= s), 0 > p && (p = (2147483647 & p) + 2147483648), (p %= 1e6), p.toString() + "." + (p ^ m));
    }
    """

    # with open('js/translate.js', 'r', encoding='UTF-8') as file:
    # js_text = file.read()
    # 编译加载js字符串
    js = execjs.compile(js_text)
    sign = js.call("e", str(content), gtk)

    params = {
        'from': lang_dict[fr],
        'to': lang_dict[to],
        'query': content,
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
        'domain': 'common'
    }

    response = session.get(url=url, params=params)
    message = response.json()
    return {'result': message['trans_result']['data'][0]['dst']}
