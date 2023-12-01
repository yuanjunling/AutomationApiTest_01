"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2023/11/7 17:08
@File : Third_party_decorator.py
@Software: PyCharm
"""
import time
from functools import wraps


def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"测试耗时 {run_time:.2f} 秒")
        return result
    return wrapper


def log_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("results.log", "a") as log_file:
            log_file.write(f"{func.__name__} - Result: {result}\n")
            return result

    return wrapper


def suppress_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
        return None

    return wrapper

#当函数遇到异常时，该装饰器会强制函数重试多次。它接受三个参数：重试次数、捕获的异常以及重试之间的间隔时间
def retry(num_retries, exception_to_check, sleep_time=0):
    """
    遇到异常尝试重新执行装饰器
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_retries+1):
                try:
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f"{func.__name__} raised {e.__class__.__name__}. Retrying...")
                    if i < num_retries:
                        time.sleep(sleep_time)
            # 尝试多次后仍不成功则抛出异常
            raise e
        return wrapper
    return decorate

#@retry(num_retries=3, exception_to_check=ValueError, sleep_time=1)


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Debugging {func.__name__} - args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper

#该装饰器的所用是多次调用被修饰函数。这对于调试、压力测试或自动化多个重复任务非常有用
def repeat(number_of_times):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(number_of_times):
                func(*args, **kwargs)

        return wrapper

    return decorate

#@countcall用于统计被修饰函数的调用次数。这里的调用次数会缓存在wraps的count属性中。
def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} has been called {wrapper.count} times')
        return result

    wrapper.count = 0
    return wrapper

#@rate_limited装饰器会在被修饰函数调用太频繁时，休眠一段时间，从而限制函数的调用速度。这在模拟、爬虫、接口调用防过载等场景下非常有用。
def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)
    def decorate(func):
        last_time_called = [0.0]
        @wraps(func)
        def rate_limited_function(*args, **kargs):
            elapsed = time.perf_counter() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kargs)
            last_time_called[0] = time.perf_counter()
            return ret
        return rate_limited_function
    return decorate
