# -*- coding: utf-8 -*-
# @Author   : Eurkon
# @Date     : 2022/3/8 14:17

import settings
from scrapy.utils.project import get_project_settings
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from api.baidu.api import api as baidu
from api.google.api import api as google
from api.tools.api import api as tools
from api.weibo.api import api as weibo
from api.youdao.api import api as youdao

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])
settings = get_project_settings()


@app.get("/baidu/translate", tags=["API"], summary="百度翻译")
def baidu_translate(fr: str = '英语', to: str = '中文', content: str = 'Hello World'):
    """百度翻译

    Args:
        fr: 源语言
        to: 翻译语言
        content: 翻译内容

    Returns:
        dict: {result: 翻译后的内容}
    """
    return baidu.baidu_translate(fr, to, content)


@app.get("/baidu/tongji", tags=["API"], summary="百度统计")
def baidu_tongji(request: Request):
    """重定向请求百度统计，解决跨域问题

    Args:
        request: {site_id: 网站id, access_token: token, ...}

    Returns:
        json: 百度统计返回的网页统计数据
    """
    return baidu.baidu_tongji(request.query_params)


@app.get("/google/translate", tags=["API"], summary="谷歌翻译")
def google_translate(fr: str = '英语', to: str = '中文', content: str = 'Hello World'):
    """谷歌翻译

    Args:
        fr: 源语言
        to: 翻译语言
        content: 翻译内容

    Returns:
        dict: {result: 翻译后的内容}
    """
    return google.google_translate(fr, to, content)


@app.get("/weibo/top", tags=["API"], summary="微博热搜")
def weibo_top():
    """微博热搜

    Args:

    Returns:
        list: [{title: 标题, url: 地址, num: 热度数值, hot: 热搜等级}, ...]
    """
    return weibo.weibo_top()


@app.get("/youdao/translate", tags=["API"], summary="有道翻译")
def youdao_translate(content: str = 'Hello World'):
    """有道翻译

    Args:
        content: 翻译内容

    Returns:
        dict: {result: 翻译后的内容}
    """
    return youdao.youdao_translate(content)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1")
