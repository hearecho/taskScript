"""
直播相关的api
"""
import os
import time

from utils import init


def getRoomInfo(s, room_id):
    """
    获取房间信息
    :param s: session
    :param room_id: 显示的房间ID
    :return: data字典
    """
    url = "https://api.live.bilibili.com/xlive/web-room" \
          "/v1/index/getRoomPlayInfo?room_id={}".format(room_id)
    r = s.get(url)
    return r.json()["data"]


def getDanMuCong(s, room_id):
    """
    获取弹幕服务器信息
    :param s: session
    :param room_id: 显示的房间ID
    :return: data字典
    """
    url = "https://api.live.bilibili.com/room/v1/Danmu/getConf?room_id={}".format(room_id)
    r = s.get(url).json()
    return r["data"]


def getBagList(s, room_id):
    r = s.get("https://api.live.bilibili.com/xlive/web-room/v1/gift/bag_list?room_id={}".format(room_id))
    return r.json()["data"]["list"]


def sendWillExpireGift(s, room_info, bage_info):
    # 将包裹中时间快到期的包裹送出
    count = 0
    t = int(time.time())
    daySecond = 24 * 60 * 60
    data = {"uid": os.environ["DEDEUSERID"],
            "gift_id": 1,
            "ruid": room_info["uid"],
            "gift_num": 1,
            "bag_id": 221873830,
            "biz_id": room_info["room_id"],
            "csrf_token": os.environ["BILI_JCT"]
            }
    # 判断过期
    for g in bage_info:
        if (g["expire_at"] - t) / daySecond < 1:
            # 送出礼物
            data["gift_id"] = g["gift_id"]
            data["gift_num"] = g["gift_num"]
            data["bag_id"] = g["bag_id"]
            r = s.post("https://api.live.bilibili.com/gift/v2/live/bag_send", data=data)
            count += 1
            print(r.json())
    print("送出将过期礼物{}".format(count))

def sign(s):
    """
    签到
    :param s:
    :return:
    """
    r = s.get("https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign")
    print(r.json())

if __name__ == '__main__':
    s, api = init.init()
    sign(s)
    room_info = getRoomInfo(s, 102)
    bag_info = getBagList(s, 102)
    sendWillExpireGift(s, room_info, bag_info)
