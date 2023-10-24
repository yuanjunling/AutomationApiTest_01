# import speedtest
# import sys
# import time


# def test_network_speed():
#     start_time = time.time()  # 获取开始时间
#     st = speedtest.Speedtest()

#     try:
#         print("测试下载速度，请稍等...")
#         download_speed = st.download() / 1000000
#         upload_speed = st.upload() / 1000000
#         results = st.results

#         print(f"下载速度: {download_speed:.2f} Mbps")
#         print(f"上传速度: {upload_speed:.2f} Mbps")
#         print(f"延时: {results.ping} ms")
#         print(f"下载宽带: {results.download} Mbit/s")
#         print(f"上传宽带: {results.upload} Mbit/s")
#     except Exception as e:
#         print(f"发送错误: {e}", file=sys.stderr)

#     end_time = time.time()  # 获取结束时间
#     run_time = end_time - start_time  # 计算运行时长
#     print(f"测试运行了 {run_time} 秒.")  # 打印运行时长


# if __name__ == "__main__":
#     test_network_speed()

import tkinter as tk
from tkinter import ttk
import speedtest, time, sys
import threading


def test_network_speed():
    start_time = time.time()  # 获取开始时间
    st = speedtest.Speedtest()
    try:
        download_speed = st.download() / 1000000
        upload_speed = st.upload() / 1000000
        results = st.results

        result_text.insert(tk.END, f"下载速度: {download_speed:.2f} Mbps\n")
        result_text.insert(tk.END, f"上传速度: {upload_speed:.2f} Mbps\n")
        result_text.insert(tk.END, f"Ping延迟: {results.ping:.2f} ms\n")
        result_text.insert(tk.END, f"下载带宽: {results.download:.2f} Mbit/s\n")
        result_text.insert(tk.END, f"上传带宽: {results.upload:.2f} Mbit/s\n")
    except Exception as e:
        result_text.insert(tk.END, f"发生错误: {e}\n")

    end_time = time.time()  # 获取结束时间
    run_time = end_time - start_time  # 计算运行时长
    result_text.insert(tk.END, f"测试耗时 {run_time:.2f} 秒\n")  # 打印运行时长


def run_speed_test():
    result_text.delete(1.0, tk.END)  # 清空之前的结果
    result_text.insert(tk.END, "正在进行网速测试，请稍等...\n")
    threading.Thread(target=test_network_speed).start()

 
root = tk.Tk()
root.title("网络速度测试")

# 添加任务栏图标
# root.wm_iconbitmap('C:/Users/DT/Desktop/cw.ico')  # 请将'path_to_your_icon.ico'替换为你的图标文件路径
# 创建并放置按钮
run_button = ttk.Button(root, text="运行速度测试", command=run_speed_test)
run_button.pack(pady=10)

# 创建用于显示结果的文本框
result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
result_text.pack(padx=10, pady=10)

# 启动GUI事件循环
root.mainloop()
