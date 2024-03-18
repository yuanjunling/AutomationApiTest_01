"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/10/30 17:17
@File : classtest.py
@Software: PyCharm
"""


def get_error_message(error_code):
    error_messages = {
        0: "设置成功",
        1: "设置超时",
        2: "设置失败",
        3: "与设备断开",
        4: "其它错误",
        # 其他错误码和对应的错误提示...
    }

    # 如果错误码在字典中，则返回对应的错误提示
    if error_code in error_messages:
        return error_messages[error_code]

        # 如果错误码不在字典中，返回默认的错误提示
    else:
        return "未知错误。"

message=get_error_message
a=1
print(message(a))