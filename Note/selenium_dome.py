"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/11/10 9:51
@File : selenium_dome.py
@Software: PyCharm
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
verificationErrors = []
accept_next_alet = True
driver.get('https://www.baidu.com/')
element = driver.find_element(By.ID,"kw")  # 通过ID查找元素
  # 通过类名查找多个元素
element.send_keys('selenium')
time.sleep(5)