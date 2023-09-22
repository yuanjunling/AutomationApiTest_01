# -*- coding: utf-8 -*-
# @Time : 2023/1/4 0004 16:07
# @Author : yuanjl
# @File : test_for_sum.py
# @Software: PyCharm
# @Title：标题
import json

import requests

url = "http://192.168.0.2:8000/cgi-bin/luci/?status=1&_=0.4786848212604997"

payload = {}
headers = {
  'Cookie': 'sysauth=c590426064f25f732b63da8766417411'
}

response = requests.request("GET", url, headers=headers, data=payload)

test=response.text
print(f"测试: {json.dumps(test, indent=2, ensure_ascii=False)}")