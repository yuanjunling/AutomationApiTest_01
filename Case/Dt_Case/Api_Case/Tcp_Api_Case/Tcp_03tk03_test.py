# coding=utf-8
import unittest
import socket, os, sys
current_dir = os.getcwd()
sys.path.append(current_dir)
from Driver.is_json import assert_field_value
from Driver.Third_party_decorator import *
from Data.Body.boby_dt import *
from Driver.handle_init import handle_ini
from Driver.loggings import logger


class TestClientSocket(unittest.TestCase):
    def setUp(self):
        logger.info("-------------------------测试开始---------------------")
        tcp_ip = handle_ini.get_value("Tcp_03tk03_IP")
        tk03_port = handle_ini.get_value("Tcp_03tk03_Port")
        self.code = handle_ini.get_value("code")
        self.recv = int(handle_ini.get_value("recv"))
        self.server_address = (tcp_ip, int(tk03_port))  # 服务器的地址和端口号
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)  # 连接服务器
        self.client_socket.settimeout(5)  # 设置超时为5秒

    def tearDown(self):
        logger.info("-------------------------测试结束---------------------")
        # 在每个测试方法运行后，都会创建这个tearDown方法
        self.client_socket.close()  # 关闭客户端的socket连接

    @time_execution
    def test_01_get_ant_state_info(self):
        """获取天线状态信息"""
        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_ant_state_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确
            self.assertIn('$GCCMD,ANT DIR', data, msg="响应数据错误")
            # 断言字段值效验
            assert_field_value(data, 2, '3', "FIELD1值错误", self.assertEqual)
            logger.info(f"Tcp获取天线状态信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取天线状态信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取天线状态信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取天线状态信息试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @time_execution
    def test_02_get_ins_info(self):
        """获取惯导信息"""

        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_ins_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确
            self.assertIn('$GCCMD,INS DATA', data, msg="响应数据错误")
            logger.info(f"Tcp获取惯导信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取惯导信息测试用例不通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取惯导信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取惯导信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                # client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @time_execution
    def test_03_get_modem_info(self):
        """获取MODEM信息"""

        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_modem_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确
            self.assertIn('$GCCMD,MODEM INFO', data, msg="响应数据错误")
            logger.info(f"Tcp获取MODEM信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取MODEM信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取MODEM信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取MODEM信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @time_execution
    def test_04_get_aim_sat_info(self):
        """获取目标卫星信息"""

        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_aim_sat_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确
            self.assertIn('$GCCMD,SAT DATA', data, msg="响应数据错误")
            logger.info(f"Tcp获取目标卫星信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取目标卫星信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取目标卫星信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取目标卫星信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @time_execution
    # @unittest.skip("暂时不需要执行")
    def test_05_get_ant_device_info(self):
        """获取天线系统信息"""

        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_ant_device_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确

            self.assertIn('$GCCMD,SYS INFO', data, msg="响应数据错误")
            logger.info(f"Tcp获取天线系统信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取天线系统信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取天线系统信息试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取天线系统信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @time_execution
    def test_06_get_sub_info(self):
        """获取副面跟踪信息"""

        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_sub_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确

            self.assertIn('$GCCMD,SUB DATA', data, msg="响应数据错误")
            logger.info(f"Tcp获取副面跟踪信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取副面跟踪信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取副面跟踪信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取副面跟踪信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @time_execution
    def test_07_get_warn_info(self):
        """获取天线告警信息"""
        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_warn_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确

            self.assertIn('$GCCMD,ANT ALM', data, msg="响应数据错误")
            logger.info(f"Tcp获取天线告警信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取天线告警信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取天线告警信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取天线告警信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @unittest.skip("暂时不需要执行")
    @time_execution
    def test_08_get_test_info(self):
        """获取天线测试信息"""
        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_test_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确

            self.assertIn('$GCCMD,TEST DATA', data, msg="响应数据错误")
            logger.info(f"Tcp获取天线测试信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取天线测试信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取天线测试信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取天线测试信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @unittest.skip("暂时不需要执行")
    @time_execution
    def test_09_get_test_step(self):
        """获取测试步骤信息"""
        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_test_step_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确

            self.assertIn('$GCCMD,TEST STEP', data, msg="响应数据错误")
            logger.info(f"Tcp获取测试步骤信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取测试步骤信息测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取测试步骤信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取测试步骤信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @unittest.skip("暂时不需要执行")
    @time_execution
    def test_10_get_all_info(self):
        """获取所有数据"""
        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(get_all_info_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确

            self.assertIn('$GCCMD,TEST STEP', data, msg="响应数据错误")
            logger.info(f"Tcp获取所有数据测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取所有数据测试用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取所有数据信息测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取所有数据信息测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)

    @unittest.skip("暂时不需要执行")
    @time_execution
    def test_11_set_power_save(self):
        """天线节电设置"""
        client_socket = self.client_socket
        # 这是一个测试方法，用于测试发送和接收数据
        try:
            client_socket.send(set_power_save_message.encode(self.code))  # 发送数据到服务器
            data = client_socket.recv(self.recv).decode(self.code)  # 验证服务器返回的数据是否正确
            # 分割响应数据，提取特定字段
            response_fields = data.split(',')
            # 验证特定字段的值
            field1_value = response_fields[2]
            field2_value = response_fields[3]
            # 进行断言验证
            self.assertEqual(field1_value, 'expected_value_1', msg="FIELD1值错误")
            self.assertEqual(field2_value, 'expected_value_2', msg="FIELD2值错误")
            self.assertIn('$GCCMD,COMMAND', data, msg="响应数据错误")
            logger.info(f"Tcp获取天线节电设置信息测试用例通过: {data}")
        except AssertionError as e:
            logger.error(f"Tcp获取天线节电设置信息用例通过: {e}", exc_info=True)
            raise e from None
        except socket.timeout:
            logger.error("Tcp获取天线节电设置测试用例中，接收数据超时")
        except Exception as e:
            logger.exception(f"Tcp获取天线节电设置测试用例中出现异常: {e}", exc_info=True)
        finally:
            try:
                client_socket.close()
                logger.info("Tcp客户端连接已关闭")
            except Exception as e:
                logger.error(f"关闭Tcp客户端连接时出错: {e}", exc_info=True)


if __name__ == '__main__':
    unittest.main()
