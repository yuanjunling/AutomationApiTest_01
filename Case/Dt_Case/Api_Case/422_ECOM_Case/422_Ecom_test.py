"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/12/13 14:45
@File : 422_Ecom_test.py
@Software: PyCharm
"""
import unittest
import socket, os, sys

current_dir = os.getcwd()
sys.path.append(current_dir)
from Driver.is_json import assert_field_value

from Driver.Third_party_decorator import *
from Data.Body.boby_dt import *
from Driver.handle_init import handle_ini
from Driver.loggings import logger
import serial
import serial.tools.list_ports

class Ecom_test(unittest.TestCase):
    """
    测试用例
    """

    def setUp(self):
        """
        初始化
        :return:
        """
        logger.info("-------------------------测试开始---------------------")
        port = handle_ini.get_value("port")
        self.ser = serial.Serial(
            port=port,  # 串口设备路径，根据实际情况修改
            baudrate=115200,  # 波特率
            bytesize=serial.EIGHTBITS,  # 数据位
            parity=serial.PARITY_NONE,  # 校验位
            stopbits=serial.STOPBITS_ONE,  # 停止位
            timeout=1  # 超时时间，单位为秒
        )

    def tearDown(self):
        logger.info("-------------------------测试结束---------------------")
        # 在每个测试方法运行后，都会创建这个tearDown方法
        # self.client_socket.close()  # 关闭客户端的socket连接
        self.ser.close()

    @time_execution
    def test_01_get_ant_state_info(self):
        """获取天线状态信息"""
        ser = self.ser
        # 这是一个测试方法，用于测试发送和接收数据
        try:

            ser.write(get_ant_state_info_message.encode())  # 将字符串编码为字节流后发送

            # 接收设备发送的数据
            response = ser.readline().decode().strip()  # 读取一行数据并解码为字符串，去掉结尾的换行符
            # 断言字段值效验
            assert_field_value(response, 1, 'ANT DIR', "FIELD1值错误", self.assertEqual)
            logger.info(f"422获取天线状态信息测试用例通过: {response}")
        except AssertionError as e:
            logger.error(f"422获取天线状态信息测试用例不通过: {e}", exc_info=True)
            raise e from None
        except Exception as e:
            logger.exception(f"422获取天线状态信息试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                ser.close()
                logger.info("422客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭422客户端连接时出错: {e}", exc_info=True)


if __name__ == '__main__':
    unittest.main()
