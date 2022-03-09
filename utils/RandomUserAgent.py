# -*- coding: utf-8 -*-
# @Author   : Eurkon
# @Date     : 2022/3/8 18:23


import os
import random
import settings


def process_request(request):
    UA = random.choice(settings["USER_AGENT_LIST"])
    if UA:
        request.headers.setdefault('User-Agent', UA)
    if settings.DEBUG and settings.HTTP_PROXY_URL != "":
        request.meta['proxy'] = settings.HTTP_PROXY_URL
    elif settings.HTTP_PROXY and os.environ.get("PROXY"):
        request.meta['proxy'] = os.environ["PROXY"]
    return request
