# coding=utf-8
import unittest
from ddt import ddt, data, unpack
import sys
import os

current_dir = os.getcwd()
sys.path.append(current_dir)
from Driver.handle_excle import HandExcel

handle = HandExcel("E:\AutomationApiTest_01\Data\case_01.xlsx")
test_data = []
value = handle.get_excel_data()
for i in value:
    test_data.append(i)


@ddt
class TestExample(unittest.TestCase):
    @data(*test_data)
    def test_case(self, data):
        param1, param2, expected = data
