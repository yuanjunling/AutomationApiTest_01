# coding=utf-8
import time
import os
from rich import print
pathname = ""


def creatfilesize(n, pathname):
    local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    global file_name
    file_name = pathname + str(local_time) + ".test"
    print("[bold red]写入文件路径:" + file_name)
    action = input("确认继续?（y/n)")

    if action == "y":
        try:
            print("[bold red]正在写入，请稍等..")
            t = time.time()
            testFile = open(file_name, "w")
            i = 1
            per = 100 / n  # 百分比计算
            while i < (n + 1):
                testFile.seek(1024 * 1024 * 1024 * i)
                testFile.write("1")
                print(f"{per*i:.2f}%")
                i += 1
            testFile.close()
            print("[bold red]\r\n写入已经完成")
            # print("写入文件大小:"+n+"GB")
            dectime = time.time() - t
            print(f"[bold red]写入用时为:{dectime:.2f}s")
            print(f"[bold red]平均速度为:{1024*n/dectime:.2f}MB/s")
            time.sleep(5)
        except IOError:
            print("[bold red]写入失败，检查路径和文件名称")
    else:
        print("[bold red]退出写入")


def main():
    n = 1  # 生成1G大小的文件
    pathname = input("输入目标位置,(例如D:\\)")
    n = input("输入要生成的文件大小(单位GB) :")
    gb = int(n)
    creatfilesize(gb, pathname)


def delete_file(file_name):
    path = file_name
    if os.path.isfile(path):
        os.remove(path)
    else:
        print("[bold red]Error: %s file not exist" % path)


number = 1
while number <= 2:
    main()
    # delete_file(file_name)
    number = number + 1
print("[bold red]硬盘测试完成")
