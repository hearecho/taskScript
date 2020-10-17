import os

import requests

from utils import transform


def init():
    """
    初始化Session,api
    :return:
    """
    # generate session 对象
    s = requests.Session()
    dic = {"bili_jct": os.environ["BILI_JCT"],
           "SESSDATA": os.environ["SESSDATA"],
           "DedeUserID": os.environ["DEDEUSERID"]}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/85.0.4183.121 Safari/537.36",
        "referer": "https://www.bilibili.com/",
    }
    s.headers.update(headers)
    s.cookies.update(dic)
    # generate api
    api = transform.transformJson("api/bilibiliapi.json")
    return s, api
