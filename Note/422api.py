"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/12/6 11:02
@File : 422api.py
@Software: PyCharm
"""
import serial
import time

ser = serial.Serial(
    port='COM10',  # 串口设备路径，根据实际情况修改
    baudrate=115200,  # 波特率
    bytesize=serial.EIGHTBITS,  # 数据位
    parity=serial.PARITY_NONE,  # 校验位
    stopbits=serial.STOPBITS_ONE,  # 停止位
    timeout=1  # 超时时间，单位为秒
)

# 向设备发送数据
message = "$GCCMD,GET ANT DIR*\r\n"
ser.write(message.encode())  # 将字符串编码为字节流后发送
print("Sent:", message)

# 接收设备发送的数据
response = ser.readline().decode().strip()  # 读取一行数据并解码为字符串，去掉结尾的换行符
print("Received:", response)

# 关闭串口连接
ser.close()