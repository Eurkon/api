# -*- coding: utf-8 -*-
# @Author : Eurkon
# @Date : 2021/6/15 9:44

import io
import os
import qrcode
from MyQR import myqr


def qrcode(content: str = 'Hello World'):
    """生成二维码

    Args:
        content: 二维码内容

    Returns:
        bytes: 字节流
    """

    img = qrcode.make(content)
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    img.save(img_bytes, format="PNG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes


def qrcode_colorized(words: str = 'Hello World', picture: str = None, colorized: str = False):
    """生成二维码

    Args:
        words: 内容(不能是中文)
        picture: 背景
        colorized: 是否为彩色

    Returns:
        str: 图片地址
    """

    path = os.path.dirname(os.path.dirname(__file__)) + '/img/'
    name = 'qrcode.gif' if picture and picture[-4:] == '.gif' else 'qrcode.png'
    colorized = True if colorized and colorized.lower() == 'true' else False
    myqr.run(words=words, picture=picture, colorized=colorized, save_name=name, save_dir=path)

    return path + name


if __name__ == '__main__':
    # print(qrcode({'words': 'https://blog.eurkon.com/',
    # 'picture': '../img/background.gif',
    # 'colorized': True}))
    print(qrcode('https://blog.eurkon.com/'))
