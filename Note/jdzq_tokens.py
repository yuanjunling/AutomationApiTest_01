# -*- coding: utf-8 -*-
# @Time : 2023/2/17 0017 13:18
# @Author : yuanjl
# @File : jdzq_tokens.py
# @Software: PyCharm
# @Title：生成token


import requests
from Driver.handle_excle import HandExcel

def get_handle(urls,headers):
    handle=HandExcel('E:\yswy_zy_member2.xlsx')
    value=handle.get_columns_value()

    for cell in value:
        res = requests.get(urls.format(cell), headers=headers)
        json_res = res.text
        print(json_res)
        with open('E:/tokens2.txt', 'a') as f:
            f.write(json_res+ '\n')


if __name__ == '__main__':

    headers = {
        "Content-Type": "application/json",
        "yswy-zy-app-token": "b3065e92-86db-4e1a-892c-530c03b75e96"
    }

    urls = "https://app-yswy.yjdfytmall.com/yswy-zy-activity-app/pointExchange/token?id={}"

    Get_handle=get_handle(urls, headers)
    Get_handle


