# coding=utf-8
import json
import string
import unittest
import sys

sys.path.append("e:/AutomationApiTest_01")
from Driver.is_json import is_jsons
from Driver.base_request import request
from Driver.handle_init import handle_ini
from Data.Headers.headers_Dt_data import *
from Data.Body.boby_dt import *
from Driver.loggings import logger


class Antenna_Case(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        rootpath_login = handle_ini.get_value("antenna_url_login")
        rootpath = handle_ini.get_value("antenna_url")
        self.login = rootpath_login
        self.getTemperature = f"{rootpath}/getTemperature"
        self.getAcuVersion = f"{rootpath}/getAcuVersion"
        self.getSysinfo = f"{rootpath}/getSysinfo"
        self.getAntennaStatus = f"{rootpath}/getAntennaStatus"
        self.setSatelliteList = f"{rootpath}/setSatelliteList"
        self.switchSatellite = f"{rootpath}/switchSatellite"
        self.asySatellite = f"{rootpath}/asySatellite"
        self.getIns = f"{rootpath}/getIns"
        self.getSub = f"{rootpath}/getSub"
        self.setSub = f"{rootpath}/setSub"
        self.getAntennaAlarm = f"{rootpath}/getAntennaAlarm"
        self.setAdjustSet = f"{rootpath}/setAdjustSet"
        self.getTestInfo = f"{rootpath}/getTestInfo"
        self.manualItems = f"{rootpath}/manualItems"
        self.restart = f"{rootpath}/restart"
        self.getLog = f"{rootpath}/getLog"

    def tearDown(self):
        print("测试结束")

    def test_01_Login(self):
        """登录"""
        login = self.login
        res = request.run_main(
            "post",
            url=login,
            headers=headers_data_login,
            data=login_payload,
            allow_redirects=False,
        )
        res.encoding = "utf-8"
        cookie = res.headers.get("Set-Cookie")
        str = ";"
        global cookies
        cookies = cookie[: cookie.index(str)]

        try:
            self.assertTrue(cookies)
            print("获取cookie用例成功: %s" % cookies)
        except Exception as e:
            print("获取cookie用例失败%s" % json.dumps(cookies, indent=2, ensure_ascii=False))
            raise e
        # logger.debug("this= %r", json.dumps(cookies, indent=2, ensure_ascii=False))

    def test_02_GetTemperaTure(self):
        """获取温度/湿度"""
        getTemperature = self.getTemperature
        headers_data["Cookie"] = cookies
        res = request.run_main("get", url=getTemperature, headers=headers_data)
        data_res = is_jsons(res)
        try:
            self.assertTrue(data_res)
            print("后台获取温度/湿度测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取温度/湿度测试用例不通过%s"
                % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e
        # logger.debug("this= %r", json.dumps(data_res, indent=2, ensure_ascii=False))

    def test_03_GetAcuVersion(self):
        """获取ACU程序版本"""
        getAcuVersion = self.getAcuVersion
        headers_data["Cookie"] = cookies
        res = request.run_main("get", url=getAcuVersion, headers=headers_data)
        data_res = is_jsons(res)
        try:
            self.assertTrue(data_res)
            print("后台获取ACU程序版本测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取ACU程序版本测试用例不通过%s"
                % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e
        # logger.debug("this= %r", json.dumps(data_res, indent=2, ensure_ascii=False))

    def test_04_GetSysinfo(self):
        """获取天线型号"""
        getSysinfo = self.getSysinfo
        headers_data["Cookie"] = cookies
        res = request.run_main("get", url=getSysinfo, headers=headers_data)
        data_res = is_jsons(res)
        try:
            self.assertTrue(data_res)
            print("后台获取天线型号测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取天线型号测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e
        # logger.debug("this= %r", json.dumps(data_res, indent=2, ensure_ascii=False))

    def test_05_GetAntennaStatus(self):
        """获取天线状态信息"""
        getAntennaStatus = self.getAntennaStatus
        headers_data["Cookie"] = cookies
        res = request.run_main("get", url=getAntennaStatus, headers=headers_data)
        data_res = is_jsons(res)
        try:
            self.assertTrue(data_res)
            print("后台获取天线状态信息测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取天线状态信息测试用例不通过%s"
                % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e
        # logger.debug("this= %r", json.dumps(data_res, indent=2, ensure_ascii=False))

    def test_06_SetSatelliteList(self):
        """保存卫星参数"""
        setSatelliteList = self.setSatelliteList
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post",
            url=setSatelliteList,
            headers=headers_data,
            data=setSatelliteList_payload,
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            self.assertTrue(data_res)
            print("后台保存卫星参数测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台保存卫星参数测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e
        # logger.debug("this= %r", json.dumps(data_res, indent=2, ensure_ascii=False))

    def test_07_SwitchSatellite(self):
        """切换卫星"""
        switchSatellite = self.switchSatellite
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post",
            url=switchSatellite,
            headers=headers_data,
            data=switchSatellite_payload,
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台切换卫星参数测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台切换卫星参数测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e
        # logger.debug("this= %r", json.dumps(data_res, indent=2, ensure_ascii=False))

    # @unittest.skip("暂时不执行")
    def test_08_AsySatellite(self):
        """下载卫星列表"""
        asySatellite = self.asySatellite
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=asySatellite, headers=headers_data, data=sasySatellite_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台下载卫星列表测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台下载卫星列表测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e
        # logger.debug("this= %r", json.dumps(data_res, indent=2, ensure_ascii=False))

    def test_09_AsySatellite_Upload(self):
        """上传卫星列表"""
        asySatellite = self.asySatellite
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=asySatellite, headers=headers_data, data=sasySatellite_payload2
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台上传卫星列表测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台上传卫星列表测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_10_GetIns(self):
        """获取天线惯导状态信息"""
        getIns = self.getIns
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=getIns, headers=headers_data, data=getIns_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台获取天线惯导状态信息测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取天线惯导状态信息测试用例不通过%s"
                % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_11_GetSub(self):
        """获取副面信息"""
        getSub = self.getSub
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=getSub, headers=headers_data, data=getIns_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台获取副面信息测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取副面信息测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_12_SetSub(self):
        """设置副面信息"""
        setSub = self.setSub
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=setSub, headers=headers_data, data=setSub_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台设置副面信息测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台设置副面信息测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_13_GetAntennaAlarm(self):
        """获取告警信息"""
        getAntennaAlarm = self.getAntennaAlarm
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=getAntennaAlarm, headers=headers_data, data=getIns_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台获取告警信息测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取告警信息测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_14_SetAdjustSet(self):
        """设置天线校准"""
        setAdjustSet = self.setAdjustSet
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=setAdjustSet, headers=headers_data, data=setAdjustSet_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台设置天线校准测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台设置天线校准测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_15_GetTestInfo(self):
        """获取天线测试信息"""
        getTestInfo = self.getTestInfo
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=getTestInfo, headers=headers_data, data=getIns_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台获取天线测试信息测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台获取天线测试信息测试用例不通过%s"
                % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_16_ManualItems(self):
        """手动执行操作"""
        manualItems = self.manualItems
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=manualItems, headers=headers_data, data=manualItems_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台手动执行操作测试测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台手动执行操作测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_17_Restart(self):
        """重启天线"""
        restart = self.restart
        headers_data["Cookie"] = cookies
        res = request.run_main("post", url=restart, headers=headers_data)
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台重启天线测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台重启天线测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e

    def test_18_GetLog(self):
        """获取天线日志"""
        getLog = self.getLog
        headers_data["Cookie"] = cookies
        res = request.run_main(
            "post", url=getLog, headers=headers_data, data=getLog_payload
        )
        data_res = is_jsons(res)
        self.assertTrue(data_res)
        try:
            print("后台重启天线测试用例通过: %s" % data_res)
        except Exception as e:
            print(
                "后台重启天线测试用例不通过%s" % json.dumps(data_res, indent=2, ensure_ascii=False)
            )
            raise e


if __name__ == "__main__":
    unittest.main()
    logger.debug("this= %r", json.dumps(unittest.main(), indent=2, ensure_ascii=False))
