"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/11/15 16:22
@File : message.py
@Software: PyCharm
"""
# 错误消息字典
def get_error_message(error_code:int,error_messages:dict)-> str:
    # 如果错误码在字典中，则返回对应的错误提示
    # if error_code in error_messages:
    #     return error_messages[error_code]

        # 如果错误码不在字典中，返回默认的错误提示
    # else:
    #     return "未知错误。"
    try:
        return error_messages.get(error_code, "未知错误。")
    except KeyError:
        return "错误码不存在于错误消息字典中。"
    except Exception as e:
        # 这里可以打印错误信息到日志，方便排查问题
        print(f"Unexpected error occurred: {e}")
