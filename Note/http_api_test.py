"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2024/2/20 14:03
@File : http_api_test.py
@Software: PyCharm
"""
import json

import requests

url = "http://192.168.100.1:16001/api/userinfo"

data = {
    "username": "13486665165"
}

response = requests.post(url=url,data=data)
res=response.json()
print(res['data'])
