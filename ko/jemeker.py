#/bin/usr/python
#name:zyt
#-*-coding:utf-8-*-
import json, urllib
from urllib import urlencode


# ----------------------------------
# 影讯API合集调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/42
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "*********************"

    # 1.按关键字检索影片信息
    request1(appkey, "GET")

    # 2.检索周边影院
    request2(appkey, "GET")

    # 3.关键字影院检索
    request3(appkey, "GET")

    # 4.影院上映影片信息
    request4(appkey, "GET")

    # 5.今日放映影片
    request5(appkey, "GET")

    # 6.支持城市列表
    request6(appkey, "GET")

    # 7.影片上映影院查询
    request7(appkey, "GET")

    # 8.按影片ID检索影片信息
    request8(appkey, "GET")


# 按关键字检索影片信息
def request1(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/index"
    params = {
        "title": "",  # 需要检索的影片标题,utf8编码的urlencode
        "smode": "",  # &lt;font color=red&gt;是否精确查找，精确:1 模糊:0  默认1&lt;/font&gt;
        "pagesize": "",  # &lt;font color=red&gt;每次返回条数，默认20,最大50&lt;/font&gt;
        "offset": "",  # &lt;font color=red&gt;偏移量，默认0,最大760&lt;/font&gt;
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 检索周边影院
def request2(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/cinemas.local"
    params = {
        "lat": "",  # 纬度，百度地图坐标系
        "lon": "",  # 经度，百度地图坐标系
        "radius": "",  # 检索半径(米)，最大3000
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 关键字影院检索
def request3(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/cinemas.search"
    params = {
        "cityid": "",  # 城市ID
        "keyword": "",  # 关键字，urlencode utf8
        "page": "",  # 页数，默认1
        "pagesize": "",  # 每页返回条数，默认20
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 影院上映影片信息
def request4(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/cinemas.movies"
    params = {
        "cinemaid": "",  # 影院ID
        "movieid": "",  # 指定电影ID，默认全部电影
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 今日放映影片
def request5(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/movies.today"
    params = {
        "cityid": "",  # 城市ID
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 支持城市列表
def request6(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/citys"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 影片上映影院查询
def request7(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/movies.cinemas"
    params = {
        "cityid": "",  # 城市ID
        "movieid": "",  # 影片ID
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


# 按影片ID检索影片信息
def request8(appkey, m="GET"):
    url = "http://v.juhe.cn/movie/query"
    params = {
        "movieid": "",  # 需要检索的影片id
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml/json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print
            res["result"]
        else:
            print
            "%s:%s" % (res["error_code"], res["reason"])
    else:
        print
        "request api error"


if __name__ == '__main__':
    main()