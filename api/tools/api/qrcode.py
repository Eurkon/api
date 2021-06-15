# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/15 9:44


from MyQR import myqr
import os


def tool_qrcode(params):
    # 普通二维码
    name = 'qrcode.png'
    path = os.path.dirname(os.path.dirname(__file__)) + '/img/'
    myqr.run(
        words=params['words'],
        save_name=name,
        save_dir=path
    )
    return '/tools/img/' + name


if __name__ == '__main__':
    tool_qrcode({'words': 'https://blog.eurkon.com'})