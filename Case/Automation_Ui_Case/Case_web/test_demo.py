# coding=utf-8

from selenium import webdriver
import unittest
from time import sleep
from Case.Automation_Ui_Case.Login import Login_H5
from Data.Body.Json_Ui_Data import account_Order
from Driver.Public_function_Ui import is_element_exist, webdriverwait_xpath_click, webdriverwait_xpath_send_keys, \
    is_element, Unblock


class Automation_Registered_web(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alet = True
    def test_accraditation_01_web(self):
        driver = self.driver
        driver.get('http://app-uat.yjdfmall.com/Web/#/walletManage/secondLeveWalletAudit')
        driver.execute_script('sessionStorage.setItem("token","afthcambtojogvi6gn80agbuk0")')
        driver.refresh()#刷新
        while is_element(driver,'//*[@id="app"]/section/section/main/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/button/span'):
            Unblock(driver,'//*[@id="app"]/section/section/main/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/button/span')
            Unblock(driver,'//span[text()="确认"]')
            if is_element_class(driver,'el-message--error')==True:
                driver.refresh()  # 刷新
            else:
                print('审批成功')

    def test_accraditation_02_two_web(self):
        pass


if __name__ == '__main__':
    unittest.main()