import os

from utils import init

if __name__ == '__main__':
    s, api = init.init()
    url = api["live"]["operate"]["Sliver2Coin"]["url"]
    body = {"csrf_token": os.environ["BILI_JCT"]}
    r = s.post(url, data=body)
    print(r.json())
    pass
