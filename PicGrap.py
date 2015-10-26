#!/usr/bin/env python
# coding:utf-8

import random
import os
import urllib2
import urllib
import sys
import thread
import time
import io
import requests
import json

path = os.path.abspath('/Library/Desktop pictures/')
sleeptime = 300


def register():
    url = "http://api.lovebizhi.com//macos_v4.php"
    options = "options=%7B%22loved%22%3A%7B%22open%22%3A%22false%22%7D%2C%22category%22%3A%7B%22open%22%3A%22true%22%2C%22data%22%3A%5B2%5D%7D%7D"

    querystring = {"a": "autoWallpaper", "spdy": "1", "device": "105", "uuid": "47d31fafd336c8e61adbafaf254d3e8b", "mode": "0", "retina": "1", "client_id": "1008", "device_id": "58039058", "model_id": "105",
                   "size_id": "0", "channel_id": "79981", "screen_width": "2560", "screen_height": "1600", "bizhi_width": "2560", "bizhi_height": "1600", "version_code": "26", "language": "zh-Hans", "jailbreak": "0", "mac": ""}
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'keep-alive': "No",
        'content-length': "118",
        'user-agent': "LoveWallpaperHD/1008/3.5.8/2560*1600",
        'host': "api.lovebizhi.com",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-cn",
        'cache-control': "no-cache",
    }
    response = requests.post(
        url, data=options, headers=headers, params=querystring)
    jsonstring = response.json()
    urlLists = []
    for x in jsonstring:
        if len(x['image']['original']) > 0:
            urlLists.append(str(x['image']['original']))
        pass
    return urlLists


def getImage():
    while(1):
        urllist = register()
        while len(urllist) > 0:
            try:
                print(urllist[len(urllist) - 1])
                response = requests.get(urllist[len(urllist) - 1])
                strs = urllist[len(urllist) - 1].split("/")
                fl = open(path + "/" + strs[len(strs) - 1], "w")
                fl.write(response.content)
                fl.close()
                print("save:" + strs[len(strs) - 1])
            except:
                print("503 error")
            del urllist[len(urllist) - 1]
            time.sleep(sleeptime)
        pass


def main():
   getImage()

if __name__ == '__main__':
    main()
