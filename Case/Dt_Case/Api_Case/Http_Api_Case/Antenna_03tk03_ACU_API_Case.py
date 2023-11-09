# coding=utf-8
import json
import string
import unittest
import sys, os
current_dir = os.getcwd()
sys.path.append(current_dir)
from Driver.is_json import is_jsons
from Driver.base_request import request
from Driver.handle_init import handle_ini
from Data.Headers.headers_Dt_data import *
from Data.Body.boby_dt import *
from Driver.loggings import logger
import time


class Antenna_03_Case(unittest.TestCase):
    def setUp(self):
        logger.info("测试开始")
        rootpath = handle_ini.get_value("antenna_tk03_url")
        tk03_Ip = handle_ini.get_value("antenna_tk03_Ip")
        self.get_ant_state_info = f"{rootpath}:{tk03_Ip}/get_ant_state_info"
        self.get_ins_info = f"{rootpath}:{tk03_Ip}/get_ins_info"
        self.get_modem_info = f"{rootpath}:{tk03_Ip}/get_modem_info"
        self.get_aim_sat_info = f"{rootpath}:{tk03_Ip}/get_aim_sat_info"
        self.get_ant_device_info = f"{rootpath}:{tk03_Ip}/get_ant_device_info"
        self.get_sub_info = f"{rootpath}:{tk03_Ip}/get_sub_info"
        self.get_out_ins_data = f"{rootpath}:{tk03_Ip}/get_out_ins_data"
        self.get_warn_info = f"{rootpath}:{tk03_Ip}/get_warn_info"
        self.get_test_info = f"{rootpath}:{tk03_Ip}/get_test_info"
        self.set_aim_sat = f"{rootpath}:{tk03_Ip}/set_aim_sat"
        self.get_test_step = f"{rootpath}:{tk03_Ip}/get_test_step"
        self.set_power_save = f"{rootpath}:{tk03_Ip}/set_power_save"
        self.set_ant_reset = f"{rootpath}:{tk03_Ip}/set_ant_reset"
        self.set_ant_manual_mode = f"{rootpath}:{tk03_Ip}/set_ant_manual_mode"
        self.set_ant_test_mode = f"{rootpath}:{tk03_Ip}/set_ant_test_mode"
        self.set_ant_test_cmd = f"{rootpath}:{tk03_Ip}/set_ant_test_cmd"
        self.set_sub = f"{rootpath}:{tk03_Ip}/set_sub"
        self.set_manual_cmd = f"{rootpath}:{tk03_Ip}/set_manual_cmd"
        self.set_ant_cal = f"{rootpath}:{tk03_Ip}/set_ant_cal"
        self.get_all_info = f"{rootpath}:{tk03_Ip}/get_all_info"
        self.set_acu_upload = f"{rootpath}:{tk03_Ip}/set_acu_upload"
        self.set_mcu_upload = f"{rootpath}:{tk03_Ip}/set_mcu_upload"
        self.get_file_to_ant_step = f"{rootpath}:{tk03_Ip}/get_file_to_ant_step"
        self.get_modem_upload_step = f"{rootpath}:{tk03_Ip}/get_modem_upload_step"
        self.getgisconfig = f"{rootpath}:{tk03_Ip}/getgisconfig"
        self.setgisconfig = f"{rootpath}:{tk03_Ip}/setgisconfig"
        self.getacuconfig = f"{rootpath}:{tk03_Ip}/getacuconfig"
        self.setacuconfig = f"{rootpath}:{tk03_Ip}/setacuconfig"
        self.get_adapter_data = f"{rootpath}:{tk03_Ip}/get_adapter_data"
        self.set_modem_upload = f"{rootpath}:{tk03_Ip}/set_modem_upload"

    def tearDown(self):
        logger.info("-------------------------测试结束---------------------")

    def test_01_get_ant_state_info(self):
        """获取天线状态信息"""
        get_ant_state_info = self.get_ant_state_info
        res = request.run_main(
            "post",
            url=get_ant_state_info,
            headers=headers_json,
            json=get_ant_state_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_ant_state_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取天线状态信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取天线状态信息测试用例不通过%s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_02_get_ins_info(self):
        """获取惯导信息"""
        get_ins_info = self.get_ins_info
        res = request.run_main(
            "post",
            url=get_ins_info,
            headers=headers_json,
            json=get_ins_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_ins_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取惯导信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取惯导信息测试用例不通过%s" % e)
            raise e

    def test_03_get_modem_info(self):
        """获取MODEM信息"""
        get_modem_info = self.get_modem_info
        res = request.run_main(
            "post",
            url=get_modem_info,
            headers=headers_json,
            json=get_modem_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_modem_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取MODEM信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取MODEM信息测试用例不通过%s" % e)
            raise e

    def test_04_get_aim_sat_info(self):
        """获取目标卫星信息"""
        get_aim_sat_info = self.get_aim_sat_info
        res = request.run_main(
            "post",
            url=get_aim_sat_info,
            headers=headers_json,
            json=get_aim_sat_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_aim_sat_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取目标卫星信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取目标卫星信息测试用例不通过%s" % e)
            raise e

    def test_05_get_ant_device_info(self):
        """获取天线系统信息"""
        get_ant_device_info = self.get_ant_device_info
        res = request.run_main(
            "post",
            url=get_ant_device_info,
            headers=headers_json,
            json=get_ant_device_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_ant_device_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取天线系统信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取天线系统信息测试用例不通过%s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_06_get_sub_info(self):
        """获取副面跟踪信息"""
        get_sub_info = self.get_sub_info
        res = request.run_main(
            "post",
            url=get_sub_info,
            headers=headers_json,
            json=get_sub_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_sub_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取副面跟踪信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取副面跟踪信息测试用例不通过: %s" % e)
            raise e

    # @unittest.skip("test_07_get_out_ins_data暂时不需要执行")
    def test_07_get_out_ins_data(self):
        """获取外部惯导数据"""
        get_out_ins_data = self.get_out_ins_data
        res = request.run_main(
            "post",
            url=get_out_ins_data,
            headers=headers_json
            # json=get_sub_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_out_ins_data", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取外部惯导数据测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取外部惯导数据测试用例不通过%s" % e)
            raise e

    def test_08_get_warn_info(self):
        """获取天线告警信息"""
        get_warn_info = self.get_warn_info
        res = request.run_main(
            "post",
            url=get_warn_info,
            headers=headers_json,
            json=get_warn_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_warn_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取天线告警信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取天线告警信息测试用例不通过: %s" % e)
            raise e

    def test_09_get_test_info(self):
        """获取天线测试信息"""
        get_test_info = self.get_test_info
        res = request.run_main(
            "post",
            url=get_test_info,
            headers=headers_json,
            json=get_test_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_test_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取天线测试信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取天线测试信息测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_10_set_aim_sat(self):
        """切换卫星测试"""
        set_aim_sat = self.set_aim_sat
        res = request.run_main(
            "post",
            url=set_aim_sat,
            headers=headers_json,
            json=set_aim_sat_json_01,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(json_ress["theme"], "set_aim_sat", "Incorrect instruction")
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台切换卫星信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台切换卫星信息测试用例不通过: %s" % e)
            raise e

    def test_11_get_test_step(self):
        """获取测试步骤"""
        get_test_step = self.get_test_step
        res = request.run_main(
            "post",
            url=get_test_step,
            headers=headers_json,
            json=get_test_step_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_test_step", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取测试步骤测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取测试步骤测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_12_set_power_save(self):
        """天线节电设置"""
        set_power_save = self.set_power_save
        res = request.run_main(
            "post",
            url=set_power_save,
            headers=headers_json,
            json=set_power_save_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_power_save", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台天线节电设置测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台天线节电设置测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_13_set_ant_reset(self):
        """天线复位设置"""
        set_ant_reset = self.set_ant_reset
        res = request.run_main(
            "post",
            url=set_ant_reset,
            headers=headers_json,
            json=set_ant_reset_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_ant_reset", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台天线复位设置测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台天线复位设置测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_14_set_ant_manual_mode(self):
        """设置手动模式"""
        set_ant_manual_mode = self.set_ant_manual_mode
        res = request.run_main(
            "post",
            url=set_ant_manual_mode,
            headers=headers_json,
            json=set_ant_manual_mode_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_ant_manual_mode", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台设置手动模式测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台设置手动模式测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_15_set_ant_test_mode(self):
        """设置测试模式"""
        set_ant_test_mode = self.set_ant_test_mode
        res = request.run_main(
            "post",
            url=set_ant_test_mode,
            headers=headers_json,
            json=set_ant_test_mode_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_ant_test_mode", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台设置测试模式测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台设置测试模式测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_16_set_ant_test_cmd(self):
        """测试模式测试命令"""
        set_ant_test_cmd = self.set_ant_test_cmd
        res = request.run_main(
            "post",
            url=set_ant_test_cmd,
            headers=headers_json,
            json=set_ant_test_cmd_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_ant_test_cmd", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台测试模式测试命令测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台测试模式测试命令测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_17_set_sub(self):
        """设置副面跟踪信息"""
        set_sub = self.set_sub
        res = request.run_main(
            "post",
            url=set_sub,
            headers=headers_json,
            json=set_sub_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(json_ress["theme"], "set_sub", "Incorrect instruction")
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台设置副面跟踪信息测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台设置副面跟踪信息测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_18_set_manual_cmd(self):
        """手动模式下控制电机"""
        set_manual_cmd = self.set_manual_cmd
        res = request.run_main(
            "post",
            url=set_manual_cmd,
            headers=headers_json,
            json=set_manual_cmd_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_manual_cmd", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台手动模式下控制电机测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台手动模式下控制电机测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_19_set_ant_cal(self):
        """天线零位标定"""
        set_ant_cal = self.set_ant_cal
        res = request.run_main(
            "post",
            url=set_ant_cal,
            headers=headers_json,
            json=set_ant_cal_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(json_ress["theme"], "set_ant_cal", "Incorrect instruction")
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台天线零位标定测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台天线零位标定测试用例不通过: %s" % e)
            raise e

    def test_20_get_all_info(self):
        """获取所有数据"""
        get_all_info = self.get_all_info
        res = request.run_main(
            "post",
            url=get_all_info,
            headers=headers_json,
            json=get_all_info_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_all_info", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取所有数据测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取所有数据测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_21_set_acu_upload(self):
        """升级acu软件包"""
        set_acu_upload = self.set_acu_upload
        res = request.run_main(
            "post",
            url=set_acu_upload,
            headers=headers_json,
            json=set_acu_upload_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_acu_upload", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台升级acu软件包测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台升级acu软件包测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_22_set_mcu_upload(self):
        """发送天线升级文件"""
        set_mcu_upload = self.set_mcu_upload
        res = request.run_main(
            "post",
            url=set_mcu_upload,
            headers=headers_json,
            json=set_mcu_upload_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_mcu_upload", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台发送天线升级文件测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台发送天线升级文件测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_23_get_file_to_ant_step(self):
        """获取升级文件传输进度"""
        get_file_to_ant_step = self.get_file_to_ant_step
        res = request.run_main(
            "post",
            url=get_file_to_ant_step,
            headers=headers_json,
            json=get_file_to_ant_step_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_file_to_ant_step", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取升级文件传输进度测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取升级文件传输进度测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_24_get_modem_upload_step(self):
        """获取升级modem进度"""
        get_modem_upload_step = self.get_modem_upload_step
        res = request.run_main(
            "post",
            url=get_modem_upload_step,
            headers=headers_json,
            json=get_modem_upload_step_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_modem_upload_step", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取升级modem进度测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取升级modem进度测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_25_set_modem_upload(self):
        """发送modem升级文件"""
        set_modem_upload = self.set_modem_upload
        res = request.run_main(
            "post",
            url=set_modem_upload,
            headers=headers_json,
            json=set_modem_upload_json,
        )

        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "set_modem_upload", "Incorrect instruction"
            )
            # self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            # self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台发送modem升级文件测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台发送modem升级文件测试用例不通过: %s" % e)
            raise e

    def test_26_getgisconfig(self):
        """获取GIS配置参数"""
        getgisconfig = self.getgisconfig
        res = request.run_main(
            "post",
            url=getgisconfig,
            headers=headers_json,
            # json=getgisconfig_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "getgisconfig", "Incorrect instruction"
            )
            self.assertEqual(json_ress["en"], 0, "Setting failed")
            # self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取GIS配置参数测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取GIS配置参数测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_27_setgisconfig(self):
        """设置GIS配置参数"""
        setgisconfig = self.setgisconfig
        res = request.run_main(
            "post",
            url=setgisconfig,
            headers=headers_json,
            json=setgisconfig_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "setgisconfig", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台设置GIS配置参数测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台设置GIS配置参数测试用例不通过: %s" % e)
            raise e

    def test_28_getacuconfig(self):
        """获取ACU配置参数"""
        getacuconfig = self.getacuconfig
        res = request.run_main(
            "post",
            url=getacuconfig,
            headers=headers_json,
            # json=getacuconfig_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "getacuconfig", "Incorrect instruction"
            )
            self.assertEqual(json_ress["verbose_en"], 1, "Setting failed")
            # self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取ACU配置参数测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取ACU配置参数测试用例不通过: %s" % e)
            raise e

    @unittest.skip("暂时不需要执行")
    def test_29_setacuconfig(self):
        """设置ACU配置参数"""
        setacuconfig = self.setacuconfig
        res = request.run_main(
            "post",
            url=setacuconfig,
            headers=headers_json,
            json=setacuconfig_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "setacuconfig", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台设置ACU配置参数测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台设置ACU配置参数测试用例不通过: %s" % e)
            raise e

    @unittest.skip("获取外部适配器数据暂时不需要执行")
    def test_30_get_adapter_data(self):
        """获取外部适配器数据"""
        get_adapter_data = self.get_adapter_data
        res = request.run_main(
            "post",
            url=get_adapter_data,
            headers=headers_json,
            # json=getgisconfig_json,
        )
        json_res = is_jsons(res)  # 判断返回报文是json还是data
        json_ress = json.loads(json_res)

        try:
            self.assertTrue(json_ress, "Empty JSON response")
            self.assertEqual(
                json_ress["theme"], "get_adapter_data", "Incorrect instruction"
            )
            self.assertEqual(json_ress["back_state"], 0, "Setting failed")
            self.assertEqual(json_ress["code_msg"], "ok", "Response not OK")
            logger.info("后台获取外部适配器数据测试用例通过: %s" % json_res)
        except AssertionError as e:
            logger.error("后台获取外部适配器数据测试用例不通过: %s" % e)
            raise e


if __name__ == "__main__":
    unittest.main()
