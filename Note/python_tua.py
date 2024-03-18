"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/12/27 10:33
@File : python_tua.py
@Software: PyCharm
"""


# test_example.py

def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


