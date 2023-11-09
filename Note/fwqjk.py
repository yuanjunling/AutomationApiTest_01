"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/11/3 11:19
@File : fwqjk.py
@Software: PyCharm
"""
import psutil
import time

while True:
    # 获取CPU利用率
    cpu_percent = psutil.cpu_percent()
    # 获取内存利用率
    memory_percent = psutil.virtual_memory().percent
    # 获取磁盘利用率
    disk_percent = psutil.disk_usage('/').percent
    # 获取网络流量
    net_io = psutil.net_io_counters()
    # 打印服务器状态信息
    print("CPU利用率：%.2f%%" % cpu_percent)
    print("内存利用率：%.2f%%" % memory_percent)
    print("磁盘利用率：%.2f%%" % disk_percent)
    print("网络流量：%.2f MBps" % (float(net_io.bytes_sent + net_io.bytes_recv) / 1024 / 1024))
    time.sleep(1)  # 暂停1秒钟后再次获取服务器状态信息