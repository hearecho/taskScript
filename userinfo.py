import time

from utils import init

if __name__ == '__main__':
    s, api = init.init()
    with open("userinfo.csv", "a+") as f:
        for i in range(1, 1000000):
            print("crawelsing url: https://api.biliob.com/author?page={}&text=&sort=0".format(i))
            try:
                r = s.get("https://api.biliob.com/author?page={}&text=&sort=0".format(i))
                data = r.json()["content"]
                for user in data:
                    f.write("{},{},{}\n".format(user["name"], user["cFans"], user["channels"]))
                f.flush()
            except Exception as e:
                print(e)
                pass
            time.sleep(0.5)
