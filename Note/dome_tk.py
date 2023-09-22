# -*- coding: utf-8 -*-
# @Time : 2023/4/13 0013 16:16
# @Author : yuanjl
# @File : dome_tk.py
# @Software: PyCharm
# @Title：标题

import tkinter as tk


def B1():
    s = e1.get()
    l1.configure(text=s)

root = tk.Tk()
root.title("test")
root.geometry("500x300+200+300")
e1 = tk.Entry(root)
e1.pack()
l1 = tk.Label(root,text="")
l1.pack()
b1 = tk.Button(root,text="获取文本框文字",command=B1)
b1.pack()

root.mainloop()