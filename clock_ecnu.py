import time
import requests
import json
import datetime
import os

if __name__ == '__main__':
    host = "https://anti-epidemic.ecnu.edu.cn/"
    str_ids = os.environ["ECNUID"]
    ids = str_ids.split(",")
    for id in ids:
        s = requests.Session()
        r = s.get(host + "/clock/user/v2/{}".format(id))
        print(r.json())
        data = {
            "number": id,
            "location": "在学校",
            "health": "健康，未超过37.3",
            "recordTime": int(time.time() * 1000),
            "token": "c40a1c26761cf1aa147006efdbced498"
        }
        headers = {'Content-Type': 'application/json'}
        r = s.put(host + "/clock/record", json.dumps(data), headers=headers)
        print(r.json())
        now = datetime.date.today()
        r = s.get(host + "/clock/record/{}?date={}%2F{}%2F{}".format(id,now.year, now.month, now.day))
        print(r.json())
