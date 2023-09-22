# coding=utf-8
import json
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
class Sunscreen(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        rootpath = handle_ini.get_value('uat')
        self.SaveUrl = rootpath + "/mgmt/activity/save"
        self.publish = rootpath + "/mgmt/activity/publish/{}"
        self.applyurl = rootpath + "/activity/apply"
        self.agree = rootpath + "/activity/apply/agree"
        self.reject = rootpath + "/activity/apply/reject"
        self.generate = rootpath + "/activity/order/generate"
        self.page =rootpath +"/activity/order/page"
        self.saveVoucher = rootpath + "/activity/order/saveVoucher"
        self.operate = rootpath + "/mgmt/order/operate"
        self.push = rootpath +"/mgmt/order/push/{}"
        self.report = rootpath +"/activity/apply/report/{}"
        self.activity_page = rootpath+"/activity/page"
        self.pageApprove=rootpath+ "/activity/apply/pageApprove"
        self.pageApproveItem = rootpath + "/activity/apply/pageApproveItem"
        self.User_info=rootpath+"/activity/apply/{}"
        self.pageApply=rootpath+"/mgmt/activity/pageApply"
        self.Slideshow = rootpath+"/activity/apply/preCheck/{}"
        self.mysql = DoMysql("yjdf_mall_orders")

    def tearDown(self):
        print('测试结束')
    # @unittest.skip("test_01_reject暂时不需要执行")
    def test_01_Save(self):
        '''后台添加活动'''
        global activityName
        # activityName = emoji.emojize('姬存希活动yuan{0} :thumbs_up:').format(random.randint(6, 999999))
        activityName="姬存希活动yuan{0}".format(random.randint(6,999999))
        print("活动名称："+activityName)
        json_Save['activityName']=activityName
        res = request.run_main('post',url=self.SaveUrl,headers=headers_Sunscreen_web_uat,json=json_Save)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('后台添加活动测试用例通过: %s'%json_res["success"])
        except Exception as e:
            print("后台添加活动测试用例不通过%s"%json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))
    # @unittest.skip("test_02_reject暂时不需要执行")
    def test_02_publish(self):
        '''活动上架'''
        Activityname=activityName
        sql = "SELECT id FROM t_activity_info WHERE activity_name = '{}'".format(Activityname)
        global result
        result = self.mysql.fetchAll(sql)
        publish=self.publish.format(result[0]['id'])
        res = request.run_main('get', url=publish, headers=headers_Sunscreen_web_uat)
        json_res=res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('活动上架测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("活动上架测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))

    # @unittest.skip("test_03_reject暂时不需要执行")
    def test_03_Slideshow(self):
        '''首页轮播进入活动校验'''
        Slideshow = self.Slideshow.format(result[0]['id'])
        res = request.run_main('post', url=Slideshow, headers=headers_Sunscreen_h5_City)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('首页轮播进入活动校验测试用例通过： %s' % json_res["success"])
        except Exception as e:
            print("首页轮播进入活动校验测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res, indent=2, ensure_ascii=False))
    # @unittest.skip("test_04_reject暂时不需要执行")
    def test_04_apply(self):
        '''市级代理活动报名'''
        json_apply['receiverName'] =GenPass()
        json_apply['activityId']=result[0]['id']
        json_apply['receiverPhone']=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        res = request.run_main('post', url=self.applyurl, headers=headers_Sunscreen_h5_City, json=json_apply)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('市级代理活动报名测试用例通过： %s' % json_res["success"])
        except Exception as e:
            print("市级代理活动报名测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))

    # @unittest.skip("test_05_reject暂时不需要执行")
    def test_05_pageApply(self):
        '''活动管理报名记录'''
        pageApply = self.pageApply
        # print(result[0]['id'])
        json_pageApply['activityId']=result[0]['id']
        res = request.run_main('post', url=pageApply, headers=headers_Sunscreen_web_uat, json=json_pageApply)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            self.assertEqual(json_res["data"]["list"][0]['applyStatusDesc'],'已报名')
            print('报名记录测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("报名记录测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res, indent=2, ensure_ascii=False))

    # @unittest.skip("test_06_reject暂时不需要执行")
    def test_06_User_info(self):
        '''获取用户报名信息'''
        User_info=self.User_info.format(result[0]['id'])
        res = request.run_main('post', url=User_info, headers=headers_Sunscreen_h5_City)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('获取用户报名信息测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("获取用户报名信息测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))
    # @unittest.skip("test_07_reject暂时不需要执行")
    def test_07_agree(self):
        '''省级审批通过'''
        sql = "SELECT id,user_id FROM t_activity_apply_info WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql)
        json_agree['activityId']=result[0]['id']
        # json_agree['applyId']=results[0]['id']
        json_agree['applyUserId'] =results[0]['user_id']
        res = request.run_main('post', url=self.agree, headers=headers_Sunscreen_h5_Province, json=json_agree)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('省级审批通过测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("省级审批通过测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))
    @unittest.skip("test_08_reject暂时不需要执行")
    def test_08_reject(self):
        '''省级审批拒绝'''
        sql = "SELECT id,user_id FROM t_activity_apply_info WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql)
        json_agree['activityId']=result[0]['id']
        # json_agree['applyId']=results[0]['id']
        json_agree['applyUserId'] =results[0]['user_id']
        res = request.run_main('post', url=self.reject, headers=headers_Sunscreen_h5_Province, json=json_agree)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('省级审批拒绝测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("省级审批拒绝测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))
    # @unittest.skip("test_09_reject暂时不需要执行")
    def test_09_agree_two(self):
        '''二级审批通过'''
        sql = "SELECT id,province_id FROM t_activity_apply_info WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql)
        json_Two['activityId'] = result[0]['id']
        # json_agree['applyId']=results[0]['id']
        json_Two['applyUserId'] = results[0]['province_id']
        res = request.run_main('post', url=self.agree, headers=headers_Sunscreen_h5_Two, json=json_Two)
        json_res = res
        try:
            self.assertEqual(json_res["success"], True)
            self.assertEqual(json_res['code'], '200')
            print('二级审批通过测试用例通过: %s' % json_res["success"])
        except Exception as e:
            print("二级审批通过测试用例不通过%s" % json.dumps(json_res, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r",json.dumps(json_res, indent=2, ensure_ascii=False))

    # @unittest.skip("test_10_reject暂时不需要执行")
    def test_10_generate_two(self):
        '''二级一键生成采购单'''
        generate = self.generate
        json_generate['activityId'] = result[0]['id']
        res_generate = request.run_main('post', url=generate, headers=headers_Sunscreen_h5_Two, json=json_generate)
        json_res_generate = res_generate
        try:
            self.assertEqual(json_res_generate["success"], True)
            self.assertEqual(json_res_generate['code'], '200')
            print('二级一键生成采购单测试用例通过: %s' % json_res_generate["success"])
        except Exception as e:
            print("二级一键生成采购单测试用例不通过%s" % json.dumps(json_res_generate, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res_generate, indent=2, ensure_ascii=False))
    # @unittest.skip("test_11_reject暂时不需要执行")
    def test_11_page(self):
        '''活动订单分页列表'''
        page=self.page
        res_page = request.run_main('post', url=page, headers=headers_Sunscreen_h5_Two, json=json_page)
        json_res_page = res_page
        try:
            self.assertEqual(json_res_page["success"], True)
            self.assertEqual(json_res_page['code'], '200')
            print('活动订单分页列表测试用例通过: %s' % json_res_page["success"])
        except Exception as e:
            print("活动订单分页列表测试用例不通过%s" % json.dumps(json_res_page, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res_page, indent=2, ensure_ascii=False))

    # @unittest.skip("test_12_reject暂时不需要执行")
    def test_12_saveVoucher(self):
        '''保存支付凭证'''
        saveVoucher = self.saveVoucher
        sql = "SELECT id FROM t_activity_order WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql)
        json_saveVoucher['id']=results[0]['id']
        saveVoucher_res = request.run_main('post', url=saveVoucher, headers=headers_Sunscreen_h5_Two, json=json_saveVoucher)
        json_res_saveVoucher = saveVoucher_res
        try:
            self.assertEqual(json_res_saveVoucher["success"], True)
            self.assertEqual(json_res_saveVoucher['code'], '200')
            print('保存支付凭证测试用例通过: %s' % json_res_saveVoucher["success"])
        except Exception as e:
            print("保存支付凭证测试用例不通过%s" % json.dumps(json_res_saveVoucher, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res_saveVoucher, indent=2, ensure_ascii=False))

    # @unittest.skip("test_13_reject暂时不需要执行")
    def test_13_operate(self):
        '''操作订单审批通过或不通过'''
        operate=self.operate
        sql = "SELECT id FROM t_activity_order WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql)
        json_operate['orderIdList'][0]=results[0]['id']
        operate_res = request.run_main('post', url=operate, headers=headers_Sunscreen_web_uat, json=json_operate)
        json_res_operate = operate_res
        try:
            self.assertEqual(json_res_operate["success"], True)
            self.assertEqual(json_res_operate['code'], '200')
            print('操作订单审批通过或不通过测试用例通过: %s' % json_res_operate["success"])
        except Exception as e:
            print("操作订单审批通过或不通过测试用例不通过%s" % json.dumps(json_res_operate, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res_operate, indent=2, ensure_ascii=False))
    # @unittest.skip("test_14_reject暂时不需要执行")
    def test_14_report(self):
        '''团队业绩-总业绩'''
        report=self.report.format(result[0]['id'])
        report_res = request.run_main('post',url=report,headers=headers_Sunscreen_h5_Two)
        json_report=report_res
        try:
            self.assertEqual(json_report["success"], True)
            self.assertEqual(json_report['code'], '200')
            print('团队业绩-总业绩测试用例通过: %s' % json_report["success"])
        except Exception as e:
            print("团队业绩-总业绩测试用例不通过%s" % json.dumps(json_report, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_report, indent=2, ensure_ascii=False))

    # @unittest.skip("test_15_reject暂时不需要执行")
    def test_15_pageApprove(self):
        '''团队业绩明细分页列表'''
        pageApprove=self.pageApprove
        json_pageApprove['activityId']=result[0]['id']
        pageApprove_res = request.run_main('post',url=pageApprove,headers=headers_Sunscreen_h5_Two,json=json_pageApprove)
        json_res_pageApprove = pageApprove_res
        try:
            self.assertEqual(json_res_pageApprove["success"], True)
            self.assertEqual(json_res_pageApprove['code'], '200')
            print('团队业绩明细分页列表测试用例通过: %s' % json_res_pageApprove["success"])
        except Exception as e:
            print("团队业绩明细分页列表测试用例不通过%s" % json.dumps(json_res_pageApprove, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res_pageApprove, indent=2, ensure_ascii=False))

    # @unittest.skip("test_16_reject暂时不需要执行")
    def test_16_pageApproveItem(self):
        '''团队业绩明细-审批明细'''
        sql_user_id = "SELECT user_id FROM t_activity_order WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql_user_id)
        pageApproveItem=self.pageApproveItem
        json_pageApproveItem['activityId']=result[0]['id']
        json_pageApproveItem['approveUserId'] = results[0]['user_id']
        pageApproveItem_res = request.run_main('post',url=pageApproveItem,headers=headers_Sunscreen_h5_Two,json=json_pageApproveItem)
        json_res_pageApproveItem = pageApproveItem_res
        try:
            self.assertEqual(json_res_pageApproveItem["success"], True)
            self.assertEqual(json_res_pageApproveItem['code'], '200')
            self.assertEqual(json_res_pageApproveItem["data"]["list"][0]['result'], '通过')
            print('团队业绩明细-审批明细测试用例通过: %s' % json_res_pageApproveItem["success"])
        except Exception as e:
            print("团队业绩明细-审批明细测试用例不通过%s" % json.dumps(json_res_pageApproveItem, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res_pageApproveItem, indent=2, ensure_ascii=False))
    # @unittest.skip("test_17_reject暂时不需要执行")
    def test_17_report(self):
        '''抢购活动列表'''
        activity_page=self.activity_page
        activity_page_res = request.run_main('post', url=activity_page, headers=headers_Sunscreen_h5_Two,json=json_activity_page)
        json_res_activity_page = activity_page_res
        try:
            self.assertEqual(json_res_activity_page["success"], True)
            self.assertEqual(json_res_activity_page['code'], '200')
            print('抢购活动列表测试用例通过: %s' % json_res_activity_page["success"])
        except Exception as e:
            print("抢购活动列表测试用例不通过%s" % json.dumps(json_res_activity_page, indent=2, ensure_ascii=False))
            raise e
        logger.debug("this= %r", json.dumps(json_res_activity_page, indent=2, ensure_ascii=False))
    # @unittest.skip("test_18_reject暂时不需要执行")
    def test_18_operate(self):
        '''推送ERP'''
        sql = "SELECT id FROM t_activity_order WHERE activity_id = '{}'".format(result[0]['id'])
        results = self.mysql.fetchAll(sql)
        push1=self.push.format(results[0]['id'])
        push_res = request.run_main('get', url=push1, headers=headers_Sunscreen_web_uat)
        json_res_push = push_res
        try:
            self.assertEqual(json_res_push["success"], True)
            self.assertEqual(json_res_push['code'], '200')
            print(f'推送ERP测试用例通过：{json_res_push["success"]}')
        except Exception as e:
            print(f"推送ERP测试用例不通过: {json.dumps(json_res_push, indent=2, ensure_ascii=False)}")
            raise e
        logger.debug("this= %r", json.dumps(json_res_push, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    unittest.main()