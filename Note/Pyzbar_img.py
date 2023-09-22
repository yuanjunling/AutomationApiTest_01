# -*- coding: utf-8 -*-
# @Time : 2023/3/30 0030 19:18
# @Author : yuanjl
# @File : Pyzbar_img.py
# @Software: PyCharm
# @Title：标题

from PIL import Image
import pyzbar.pyzbar as pyzbar

def pyzbar_img(filename):
    img = Image.open(filename)
    barcodes = pyzbar.decode(img)
    # print(barcodes)
    print(pyzbar.decode(img)[0].data.decode('utf-8'))

if __name__ == '__main__':
    filename='E://Work_Project//yjl//AutomationApiTest_01//Data//Img//2.png'
    pyzbar_imgs=pyzbar_img(filename)
    pyzbar_imgs
