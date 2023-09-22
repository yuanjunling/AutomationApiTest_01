# coding=utf-8
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
import unittest,random,hashlib,time,json
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Case.Automation_Ui_Case.Login import Login_H5
from Data.Body.Json_Ui_Data import account_Order
from Driver.Public_function_Ui import is_element_exist, webdriverwait_xpath_click, webdriverwait_xpath_send_keys,is_element
from selenium.webdriver.support.ui import Select

class Purchase_order(unittest.TestCase):

    def setUp(self):
        mobileEmulation = {'deviceName': 'iPhone 6/7/8 Plus'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.order_url='http://app-uat.yjdfmall.com/Wap/#/login'
        self.verificationErrors=[]
        self.accept_next_alet=True
    # @unittest.skip('采购订单，暂时不执行')
    def test_01_order(self):
        '''二级发起采购订单'''
        driver=self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver,account_Order['username'],account_Order['pwd'])#调用公共登录
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()
        sleep(2)
        if  is_element_exist(driver,'//*[@id="app"]/div/div[1]/div/div[4]/div[1]')==True:
            #判断有无充值公告有就点击没有就下一步
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div/div')
        else:
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[2]/div/div')
        #搜索
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[3]/div/i')
        sleep(1)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[1]/div/div[2]/form/div/div/div/div[2]/div/input',account_Order['produce'])
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[1]/div/div[3]/span')
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div/div[2]/button')
        sleep(1)
        webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[1]/i')
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/button')#普通进货单
        sleep(1)
        element = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/button')
        driver.execute_script("arguments[0].click();", element)# 提交
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div')
        sleep(2)

        print(is_element(driver,'//*[@id="app"]/div/ul/li[1]/div/div/div[1]'))

        if is_element(driver,'//*[@id="app"]/div/ul/li[1]/div/div/div[1]')==True:
            sleep(1)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/ul/li[1]/div/div/div[1]')
            sleep(2)
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[4]/button')  # 提交订单
        else:
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div/button')
            webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/input',account_Order['name'])
            webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/input', account_Order['phone'])
            status = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[2]/div/input')
            status.click()
            sleep(1)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[6]/div/ul[2]/li[11]')
            sleep(1)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[6]/div/ul[2]/li[2]')
            sleep(1)
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[6]/div/ul[2]/li[2]')
            sleep(1)
            data = ''.join(random.sample(string.ascii_letters + string.digits, 50))
            webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[4]/div[2]/div/textarea',data)
            sleep(1)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/div/button')
            sleep(1)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/ul/li/div/div/div[1]')
            sleep(10)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/button')#提交订单
            sleep(2)
            # element = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div[2]/div[3]/button/span')
            # driver.execute_script("arguments[0].click();", element)  # 提交

        sleep(1)
        if is_element(driver,'//*[@id="app"]/div/div[4]/div[3]/div[2]/div[2]/div[2]/ul/li[1]')==True:
            for i in range(6):
                webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/div[3]/div[2]/div[2]/div[2]/ul/li[1]')
            sleep(2)
            #截取当前窗口，并指定截图图片的保存位置
            try:
                self.assertEqual(driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/div[1]').text,'提交成功')
            except:
                now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time())) #生成时间
                file_path = 'E://AutomationApiTest//Report//Img//'
                wwwa=file_path+now+'selenium_img.png'
                driver.get_screenshot_as_file(wwwa)#自动错误截图
        else:
            sleep(1)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/div[2]/div[2]/div[3]/button')#立即支付
            sleep(2)
            driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
            sleep(2)
            webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[3]/button')
            sleep(1)
            status=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div[1]').text
            Purchaser=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]').text
            #效验订单状态
            self.assertEquals(status,'已确认')
        sleep(5)


        driver.quit()
if __name__ == '__main__':
    unittest.main()





