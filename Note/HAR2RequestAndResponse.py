# coding=utf-8
import json
from haralyzer import HarParser

# 打开 HAR 文件并指定正确的编码方式


def HarParser_run(address):
    with open(address, "r", encoding="utf-8") as file:
        # 使用 ISO-8859-1 编码方式读取文件内容
        har_content = file.read()

        # 将文件内容加载为 JSON 对象
        har_data = json.loads(har_content)

    # 实例化 HarParser 类
    har_parser = HarParser(har_data)

    # 获取所有请求条目
    entries = har_parser.har_data["entries"]

    # 检查HAR文件结构
    if "log" in har_data and "entries" in har_data["log"]:
        entries = har_data["log"]["entries"]

        # 遍历每个请求项
        for entry in entries:
            initiator = entry["_initiator"]

            # 判断initiator类型为script的请求
            if initiator["type"] == "script":
                # 提取请求URL
                url = entry["request"]["url"]
                # 提取请求方法

                # 过滤掉路径中包含"SVG"和"PNG"的请求
                if (
                    "svg" not in url
                    and "png" not in url
                    and "js" not in url
                    and "css" not in url
                ):
                    method = entry["request"]["method"]
                    # print('请求方法:', method)

                    if method.upper() == "POST":
                        # 提取请求URL
                        url = entry["request"]["url"]
                        print("请求URL:", url)

                        # 提取请求方法
                        method = entry["request"]["method"]
                        print("请求方法:", method)

                        # 请求内容
                        request = entry["request"]["postData"]["text"]
                        print("请求内容:", request)

                        # 提取响应体内容
                        content = entry["response"]["content"]["text"]
                        print("响应体内容:", content)
                        print(
                            "--------------------------------------------------------"
                        )

                    if method.upper() == "GET":
                        # 提取请求URL
                        url = entry["request"]["url"]
                        print("请求URL:", url)

                        # 提取请求方法
                        method = entry["request"]["method"]
                        print("请求方法:", method)

                        request = entry["request"]["queryString"]
                        print("请求内容:", request)

                        # 提取响应体内容
                        content = entry["response"]["content"]["text"]
                        print("响应体内容:", content)
                        print(
                            "--------------------------------------------------------"
                        )

                # 提取特定字段的值
                # 例如，提取响应体中的某个字段值
                # 注意：字段名称可能因实际情况而不同，需要根据HAR文件的结构调整
                # specific_field = content.get('userName', None)
                # if specific_field:
                #     print('特定字段值:', specific_field)
    else:
        print("HAR文件的结构不符合预期")



if __name__ == "__main__":
    har = HarParser_run
    har("E:/AutomationApiTest_01/Data/192.168.0.2.har")
