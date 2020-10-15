import requests


def generateBiliCookie(dic):
    cookiejar = requests.cookies.RequestsCookieJar()
    for k in dic:
        cookiejar.set(k, dic[k], domain='.bilibili.com', path='/')
    return cookiejar
    pass
