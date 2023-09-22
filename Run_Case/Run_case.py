# coding=utf-8

import unittest
from XTestRunner import HTMLTestRunner
import time, os, sys

current_dir = os.getcwd()
sys.path.append(current_dir)
# from Case.Test_Demo import ZNcase_01
from Driver.handle_init import handle_ini
from Driver.runtest_email import send_mail, latest_report
import threading

# from Case.Jcx_Case.Sunscreen_Case import Sunscreen_Api
# from Case.Automation_Ui_Case.Case_H5.Automation_Registered import Automation_Registered_h5 as h5
from Case.Dt_Case.Api_Case.Http_Api_Case.Antenna_Api_Case import Antenna_Case
from Case.Dt_Case.Api_Case.Http_Api_Case.Antenna_03tk03_ACU_API_Case import (
    Antenna_03_Case,
)


suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Sunscreen_Api.Sunscreen))
suite.addTest(unittest.makeSuite(Antenna_03_Case))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
rootpath = handle_ini.get_value("rootpath")
file_path = f"{rootpath}/Report/"

wwwa = f"{file_path}{now}_Dt.html"
with open(wwwa, "wb") as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title="迪泰-天线api",
        description="天线03接口自动化输出报告",
        language="zh-CN",
        tester="执行人：袁军令",
    )
    runner.run(suite)


# if __name__ == "__main__":
#     lock = threading.Lock()
#     for i in range(2):
#         t1 = threading.Thread(target=run_case)
#         t1.start()
#         t1.join()


# h获取最新测试报告
# latest_report = latest_report(file_path)
# 发送邮件报告
# send_mail(latest_report)
