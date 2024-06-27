import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def userinfo_test(username, password):
    # 禁用SSL证书验证的警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    login_url = "http://192.168.100.1:16001/api/login"
    login_data = {"username": username, "password": password}
    log_response = requests.post(url=login_url, data=login_data)
    logres = log_response.json()
    print(f"login{logres}")
    time.sleep(1)
    while True:
        userinfo_url = "https://192.168.100.1:16004/api/userinfo"
        hea = {"Content-Type": "application/json"}
        userinfo_data = {"username": username}
        userinfo_response = requests.post(
            url=userinfo_url, json=userinfo_data, headers=hea, verify=False
        )

        # 检查响应状态码，确保请求成功
        if userinfo_response.status_code == 200:
            userinfos = userinfo_response.json()
            print(userinfos)
        else:
            print(f"Error: {userinfo_response.status_code}")


if __name__ == "__main__":
    run_test = userinfo_test(17888888866, 123456)
    run_test
