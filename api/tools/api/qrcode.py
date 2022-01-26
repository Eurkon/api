# -*- coding: utf-8 -*- 
# @Author : Eurkon
# @Date : 2021/6/15 9:44

import io
import os


def tools_qrcode(params):
    """生成二维码

    Args:
        params (dict): {content: 内容}

    Returns:
        bytes: 字节流
    """
    import qrcode

    img = qrcode.make(str(params['content']))
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    img.save(img_bytes, format="PNG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes


def tools_qrcode_color(params):
    """生成二维码

    Args:
        params (dict): {words: 内容(不能是中文), picture: 背景, colorized: 是否为彩色}

    Returns:
        str: 图片地址
    """
    from MyQR import myqr

    words = params['words']
    name = 'qrcode.png'
    path = os.path.dirname(os.path.dirname(__file__)) + '/img/'
    picture = None
    colorized = False

    if 'picture' in params:
        picture = str(params['picture'])
        if picture[-4:] == '.gif':
            name = 'qrcode.gif'

    if 'colorized' in params and str(params['colorized']).lower() == 'true':
        colorized = True

    myqr.run(
        words=words,
        picture=picture,
        colorized=colorized,
        save_name=name,
        save_dir=path
    )

    return path + name


if __name__ == '__main__':
    # print(qrcode({'words': 'https://blog.eurkon.com/',
    # 'picture': '../img/background.gif',
    # 'colorized': True}))
    print(tools_qrcode({'content': 'https://blog.eurkon.com/'}))
