import subprocess
import datetime


def ssh_file_exists(local_file_path:str,remote_host:str,remote_user:str,remote_file_path                                                                                                                                                                                                                                      :str):

    while True:
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            # 在新文件名中添加时间戳
            new_remote_file_name = f"new_file_name_{timestamp}.test"  # 新文件名

            # 构建SCP命令
            command = [
                "scp",
                "-r",
                "-o", "StrictHostKeyChecking=no",  # 跳过主机密钥检查
                f"{local_file_path}",  # 本地文件路径
                f"{remote_user}@{remote_host}:{remote_file_path}{new_remote_file_name}"  # 远程服务器信息和新的文件名
            ]

            # 执行SCP命令
            print('文件上传中...')
            with subprocess.run(command, check=True, capture_output=True, text=True, timeout=3600) as process:
                # 检查命令执行结果
                if process.returncode == 0:
                    print("文件上传成功！")
                else:
                    print("文件上传失败！")
                    print("错误信息：", process.stderr)
        except subprocess.TimeoutExpired:
            print("文件上传超时，重新尝试上传...")
        except Exception as e:
            print("文件上传出现异常！")
            print("异常信息：", str(e))
            break  # 遇到不可恢复的错误时退出循环

if __name__ == '__main__':
    local_file_path = r"E:\AutomationApiTest_01\e20231120164137.test"
    remote_host = "192.168.1.1"
    remote_user = "root"
    remote_file_path = "/mnt/sda1/hdd/04/"
    ssh_file_exists(local_file_path,remote_host,remote_user,remote_file_path)