# coding=utf-8
import json
import string
import unittest
from Data.Body.body_data import *
from Driver.DoMysql import DoMysql
from Driver.base_request import request
from Driver.GenPass import GenPass
from Driver.handle_init import handle_ini
from Data.Headers.headers_data import *
import logging
rootpath = handle_ini.get_value('rootpath')
file_path = rootpath + "/Log/"
logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                filename=file_path+'\logs.log',
                filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                # a是追加模式，默认如果不写的话，就是追加模式
                format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                # 日志格式
                )
logger = logging.getLogger()

class Activity_Reward(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('uat')
        self.AddReward = rootpath+"/mgmt/reward/save"
        self.openActivity = rootpath+"/mgmt/reward/enable/{}"
        self.enableAutoApprove = rootpath +"/mgmt/reward/enableAutoApprove/{}"
        self.mysql = DoMysql("elephant")
        self.headers_Sunscreen_web=headers_Sunscreen_web_uat
    def tearDown(self):
        print('测试结束')
    def test_01_AddReward(self):
        '''后台添加活动奖励'''
        global activityName
        activityName="姬存希活动奖励yuan{0}".format(random.randint(6,999999))
        print("活动名称："+activityName)
        AddReward = self.AddReward
        json_AddReward['name']=activityName
        json_AddReward['content']=''.join(random.sample(string.ascii_letters + string.digits, 50))
        json_AddReward['desc'] = ''.join(random.sample(string.ascii_letters + string.digits, 50))

        res = request.run_main('post',url=AddReward,headers=self.headers_Sunscreen_web,json=json_AddReward)
        json_AddReward_res = res
        try:
            self.assertEqual(json_AddReward_res["success"], True)
            self.assertEqual(json_AddReward_res['code'], '200')
            print('后台添加活动奖励测试用例通过: %s'%json_AddReward_res["success"])
        except Exception as e:
            print("后台添加活动奖励测试用例不通过%s"%json.dumps(json_AddReward_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_AddReward_res, indent=2, ensure_ascii=False))

    def test_02_OpenActivity(self):
        '''活动上架'''
        Activityname=activityName
        sql = "SELECT id FROM reward_info WHERE reward_name = '{}'".format(Activityname)
        global result
        result = self.mysql.fetchAll(sql)
        openActivity=self.openActivity.format(result[0]['id'])
        self.mysql.close()
        res = request.run_main('get', url=openActivity, headers=self.headers_Sunscreen_web)
        json_res=res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('奖励活动开启测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("奖励活动开启测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))

    def test_03_enableAutoApprove(self):
        '''开启自动审批'''
        enableAutoApprove = self.enableAutoApprove.format(result[0]['id'])
        res = request.run_main('get', url=enableAutoApprove, headers=self.headers_Sunscreen_web)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('奖励活动开启自动审批测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("奖励活动开启自动审批测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    unittest.main()