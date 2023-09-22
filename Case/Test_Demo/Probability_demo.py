# -*- coding: utf-8 -*-
# @Time : 2023/6/9 0009 9:58
# @Author : yuanjl
# @File : Probability_demo.py
# @Software: PyCharm
# @Title：标题
import requests
import json

url = "https://api-qzy-uat.yjdfytmall.com/yswy-qingziyan-service/draw/startDraw"

headers = {
  'yswy-qingziyan-app-token': '6a2e52ad-716b-4615-a357-c6d1f4f8059a',
  'content-type': 'application/json'
}

for a in range(100):
    res=requests.post(url=url,headers=headers)
    print(res.json()['data'])
