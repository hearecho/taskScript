import json
import time
from random import choice
import os
import logging

from utils.init import init


def getVideoList(s):
    """
    返回更新列表
    :return:
    """
    videolist = []
    r = s.get(
        "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid={}&type_list=8,512,4097,4098,"
        "4099,4100,4101".format(os.environ["DEDEUSERID"])).json()
    for dyn in r["data"]["cards"]:
        card = json.loads(dyn["card"])
        videolist.append(card["aid"])
    return videolist


def getDeldCoins(s, aid):
    """
    获取该视频已经投的硬币
    :param s:Session
    :param aid: av号
    :return: 返回已投硬币个数
    """
    r = s.get("https://api.bilibili.com/x/web-interface/archive/coins?aid={}".format(aid)).json()
    return r["data"]["multiply"]
    pass


def deliveryCoin(s, aid, coins):
    """
    :param s: session
    :param aid: av号
    :param coins: 可投硬币数
    :return:
    """
    data = {"aid": aid, "multiply": coins, "select_like": "1", "cross_domain": "true",
            "csrf": "97f897c8b4e300f2e8c8473fa6659a17"}
    r = s.post("https://api.bilibili.com/x/web-interface/coin/add", data=data).json()
    return r["data"]["like"]
    pass


if __name__ == '__main__':
    s, api = init()
    coins = 5
    videolist = getVideoList(s)
    logging.info("获取到videolist{}".format(videolist))
    while coins > 0:
        time.sleep(0.5)
        aid = choice(videolist)
        deliveiedCoin = getDeldCoins(s, aid)
        if deliveiedCoin < 2:
            # 投币
            if deliveiedCoin == 1 or coins == 1:
                deliveryCoin(s, aid, 1)
                logging.info("投币视频aid{}".format(aid))
                coins = coins - 1
            elif coins >= 2:
                deliveryCoin(s, aid, 2)
                logging.info("投币视频aid{}".format(aid))
                coins = coins - 2
