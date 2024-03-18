"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/10/31 13:27
@File : fakerdemo.py
@Software: PyCharm
"""




from faker import Faker
import time,threading

from faker import Faker
import time, threading

from faker import Faker
import time
import threading
from concurrent.futures import ThreadPoolExecutor


def demo_txt(faker):
    start_time = time.perf_counter()

    print(faker.name())
    print(faker.ssn())
    print(faker.address())
    print(faker.phone_number())
    print(faker.email())
    print(faker.company())
    print(faker.job())

    end_time = time.perf_counter()
    run_time = end_time - start_time

    print('\n运行时长：', run_time)


if __name__ == '__main__':
    faker = Faker(locale="zh_CN")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(100):
            executor.submit(demo_txt, faker)