# coding=utf-8
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
import unittest,random,hashlib,time,json
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Case.Automation_Ui_Case.Login import Login_H5
from Data.Body.Json_Ui_Data import account_Order
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Driver.Public_function_Ui import is_element_exist, webdriverwait_xpath_click, webdriverwait_xpath_send_keys, \
    is_element, Unblock
from selenium.webdriver.support.ui import Select

class Automation_Registered_h5(unittest.TestCase):
    def setUp(self):
        mobileEmulation = {'deviceName': 'iPhone 6/7/8 Plus'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.order_url = 'http://app-uat.yjdfmall.com/Wap/#/login?redirect=%2Fhome'
        self.verificationErrors = []
        self.accept_next_alet = True
    @classmethod
    def setUpClass(cls):
        globals()["url"]=None
        globals()["username"]=None

    def tearDown(self):
        self.driver.quit()
    # @unittest.skip('test_01_Invite_agent_to_register暂时不执行')
    def test_01_Invite_agent_to_register(self):
        '''二级代理邀请代理'''
        driver = self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver, account_Order['username'], account_Order['pwd'])  # 调用公共登录
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()
        sleep(2)
        if is_element_exist(driver, '//*[@id="app"]/div/div[1]/div/div[4]/div[1]') == True:
            # 判断有无充值公告有就点击没有就下一步
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[2]/div/div[4]/div/div')
        else:
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[2]/div/div[4]/div/div')
        sleep(2)
        webdriverwait_xpath_click(driver,'//div/div/span[text()="省代"]')
        # webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div/div[3]/div/i/div')
        sleep(2)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[4]/div/div/div/div')
        sleep(2)
        globals()["url"]=driver.find_element_by_class_name('van-grid-item').get_attribute('data-clipboard-text')
        print('省代邀请码: {}'.format(globals()["url"]))


    # @unittest.skip('暂时不执行')
    def test_02_Province(self):
        '''邀请省级代理'''
        driver=self.driver
        driver.get(globals()["url"])
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div/input',account_Order['phone'])
        globals()["username"]=account_Order['phone']
        print('省级代理人账号：{}'.format(account_Order['phone']))
        # f = open('E://AutomationApiTest//Data//test','a')
        # f.write('省级代理人账号：{}'.format(account_Order['phone']))
        # f.write("\n")
        # f.close()

        with open('E://AutomationApiTest_01//Data//test','a') as f:
            f.write('省级代理人账号：{}{}'.format(account_Order['phone'],'\n'))


        sleep(2)
        Unblock(driver,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/button')
        sleep(1)
        self.assertEqual(driver.find_element_by_xpath('/html/body/div[2]/div').text,'短信发送成功')
        sleep(1)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/input',account_Order['Verification_Code'])
        sleep(2)
        Unblock(driver,'//*[@id="app"]/div/div[2]/div[2]/div[3]/button/span')
        sleep(2)
        # self.assertEqual(driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]').text,'邀请人授权码：XX154422 邀请人：快乐的胖子')
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[1]/div/div/input','a111111')
        sleep(2)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div[4]/div/div/i')
        sleep(2)
        Unblock(driver,'//*[@id="app"]/div/div[2]/div[3]/button/span')
        sleep(2)
        Unblock(driver,'//*[@id="app"]/div/div[4]/div[2]/button[2]/span')
        sleep(2)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[1]/div[2]/div/input',account_Order['name'])
        sleep(2)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[3]/div[2]/div/input',account_Order['Number'])
        sleep(2)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[2]/div[5]/div[2]/div/input',account_Order['IdNumber'])
        sleep(2)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div[2]/div/input')
        sleep(2)
        #选择省市区
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[5]/div/ul[2]/li[3]')
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[5]/div/ul[2]/li[3]')
        sleep(1)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/div[5]/div/ul[2]/li[3]')
        sleep(2)
        webdriverwait_xpath_send_keys(driver,'//*[@id="app"]/div/div[2]/div[3]/div[2]/div[2]/div/textarea',account_Order['Address'])
        sleep(2)
        Unblock(driver,'//*[@id="app"]/div/div[3]/button[2]/span')
        sleep(5)
    # @unittest.skip('暂时不执行')
    def test_03_Superior_approval(self):
        '''上级升级审批'''
        driver = self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver, account_Order['username'], account_Order['pwd'])
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()
        sleep(2)
        if is_element_exist(driver, '//*[@id="app"]/div/div[1]/div/div[4]/div[1]') == True:
            # 判断有无充值公告有就点击没有就下一步
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[2]/div/div[6]/div/div')
        else:
            webdriverwait_xpath_click(driver, '//*[@id="app"]/div/div[1]/div/div[2]/div/div[6]/div/div')
        sleep(2)
        webdriverwait_xpath_click(driver,'//*[@id="app"]/div/ul/li[1]/div[2]')
        sleep(2)
        # result=driver.find_elements_by_xpath('//button/span[text()="同意"]')
        for i in range(result:=len(driver.find_elements_by_xpath('//button/span[text()="同意"]'))):
           sleep(2)
           Unblock(driver,'//*[@id="app"]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/button[2]/span')
        sleep(2)

    # @unittest.skip('04暂时不执行')
    def test_04_Recharge(self):
        '''代理升级充值'''
        driver = self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver, globals()["username"], account_Order['pwd'])
        sleep(2)
        if is_element_exist(driver,'//*[@id="app"]/div/div[2]/div/div[4]') == True:
            Unblock(driver,'//*[@id="app"]/div/div[2]/div/div[4]')
        else:
            Unblock(driver,'//*[@id="app"]/div/div[2]/div/div[3]')
        sleep(2)
        global exist
        if (exist:=is_element(driver,'//div/button/span[text()="升级中"]'))==True:
            sleep(1)
            Unblock(driver,'//div/button/span[text()="升级中"]')
            sleep(2)
            Unblock(driver,'//button[2]/span[text()="去充值"]')
            sleep(2)
            driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
            sleep(2)
            Unblock(driver,'//*[@id="app"]/div/div[3]/button/span')
            sleep(2)
        else:
            print(driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/span').text)
    # @unittest.skip('暂时不执行')
    def test_05_Recharge_approved_by_superior(self):
        driver = self.driver
        driver.get(self.order_url)
        Login_H5.lonin_h5(driver, account_Order['username'], account_Order['pwd'])  # 调用公共登录
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]').click()
        sleep(2)
        if is_element_exist(driver, '//*[@id="app"]/div/div[1]/div/div[4]/div[1]') == True:
            # 判断有无充值公告有就点击没有就下一步
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[3]/button').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/i').click()
            webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
        else:
            webdriverwait_xpath_click(driver, '//div/span[text()="我的审批"]')
        sleep(2)
        webdriverwait_xpath_click(driver,'//span[text()="充值审批"]')
        sleep(2)
        for i in range(result:=len(driver.find_elements_by_xpath('//span[text()="加入平台充值"]'))):
            if result == 0:
                print('审批订单数{}'.format(result))
            else:
               sleep(2)
               Unblock(driver,'//*[@id="app"]/div/div[3]/div/div[1]/div[1]/div[2]/button[2]/span')
               sleep(1)
               Unblock(driver,'//span[text()="确定加入"]')
        sleep(2)
        Unblock(driver,'//span[text()="发起平台充值"]')
        sleep(2)
        driver.find_element_by_class_name('van-uploader__input').send_keys(account_Order['img'])
        sleep(2)
        Unblock(driver,'//span[text()="提交"]')
        sleep(10)

    @unittest.skip('暂时不执行')
    def test_06_Background_approval(self):
        '''后台暂时不执行'''
        self.driver = webdriver.ChromeOptions()
        driver = self.driver
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap['phantomjs.page.settings.Accept-Language']='zh-CN'
        dcap['phantomjs.page.settings.token'] = 'licjf40q4scstcidlu07lmset6'
        dcap['phantomjs.page.settings.version'] = '1.0'
        dcap['phantomjs.page.settings.clientType'] = '2'
        driver = webdriver.Chrome(chrome_options=dcap)
        driver.maximize_window()
        driver.get('http://app-uat.yjdfmall.com/Web/#/memberManage/exitAgent')
        driver.get('http://app-uat.yjdfmall.com/Web/#/memberManage/exitAgent')
        driver.get('http://app-uat.yjdfmall.com/Web/#/memberManage/exitAgent')
        sleep(5)
if __name__ == '__main__':
    unittest.main()