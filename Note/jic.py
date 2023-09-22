# -*- coding: utf-8 -*-
# @Time : 2023/3/20 0020 10:55
# @Author : yuanjl
# @File : jic.py
# @Software: PyCharm
# @Title：标题

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
