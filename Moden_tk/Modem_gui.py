"""
-*- coding: utf-8 -*-
@Author : yuanjl
@Time : 2024/1/31 14:08
@File : Moden_gui.py
@Software: PyCharm
"""

import platform
import requests
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinter import scrolledtext
import threading
import queue
import time
from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pydantic import BaseModel
from enum import Enum
import subprocess
from XTestRunner import HTMLTestRunner
from matplotlib import rcParams

# 设置全局字体为“Microsoft YaHei”（需要确保该字体已安装在系统上）
rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# 解决保存图像是负号'-'显示为方块的问题
rcParams["axes.unicode_minus"] = False

# 全局列表来存储sqf值
sqf_list = []
target_host = "192.168.222.1"
# target_host = "172.19.200.1"
community_string = "public"


class Color(Enum):
    modem_xiusi = "休斯"
    modem_UHP = "UHP"
    modem_503 = "503"


class UHP_OID(BaseModel):
    ETH: str = ".1.3.6.1.2.1.2.2.1.8.1"
    RX: str = ".1.3.6.1.2.1.2.2.1.8.1.3"
    TX: str = ".1.3.6.1.2.1.2.2.1.8.1.4"
    NET: str = ".1.3.6.1.2.1.2.2.1.8.1.5"
    TX_LEVEL: str = ".1.3.6.1.4.1.8000.22.4.6.1"
    SR: str = ".1.3.6.1.4.1.8000.22.9.4.0"
    SN: str = ".1.3.6.1.4.1.8000.22.9.2.0"
    FAULTS: str = ".1.3.6.1.4.1.8000.22.5.4.17.0"


class HoverLineChartApp:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.popup_window = None
        # Button to open the line chart in a popup window
        open_button = tk.Button(master, text="打开折线图", command=self.show_line_chart)
        open_button.grid(row=12, column=5)

    def show_line_chart(self):
        # Create a new toplevel window
        self.popup_window = tk.Toplevel(self.master)
        self.popup_window.title("Hover over a point to see details")

        # Create a matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)

        # Embed the matplotlib figure into the Toplevel window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.popup_window)
        self.widget = self.canvas.get_tk_widget()
        self.widget.pack(fill=tk.BOTH, expand=True)

        # Data for the line chart
        self.x_data = range(len(self.data))
        self.y_data = self.data

        # Plot the line chart
        (self.line,) = self.ax.plot(self.x_data, self.y_data, marker="o", pickradius=5)
        self.ax.set_title("将鼠标悬停在点上以查看详细信息")
        self.ax.set_xlabel("number")
        self.ax.set_ylabel("SQF")

        # Annotation for hover details
        self.annot = self.ax.annotate(
            "",
            xy=(0, 0),
            xytext=(20, 20),
            textcoords="offset points",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->"),
        )
        self.annot.set_visible(False)

        # Connect the event handler for motion events
        self.canvas.mpl_connect("motion_notify_event", self.hover)

        # Refresh the canvas
        self.canvas.draw()
        # self.canvas = FigureCanvasTkAgg(self.fig, master=self.popup_window)
        # self.widget = self.canvas.get_tk_widget()
        # # 创建工具栏并添加到窗口中
        toolbar = NavigationToolbar2Tk(self.canvas, self.popup_window)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.widget.pack(fill=tk.BOTH, expand=True)

    def hover(self, event):
        if event.inaxes == self.ax:
            cont, ind = self.line.contains(event)
            if cont:
                try:
                    x = self.x_data[ind["ind"][0]]
                    y = self.y_data[ind["ind"][0]]
                except IndexError:
                    # Handle the case where the indices are out of range
                    return
                    # Update the annotation position and text
                self.annot.xy = (x, y)
                text = f"X: {x}, Y: {y}"
                self.annot.set_text(text)

                # Make the annotation visible and position it
                self.annot.set_visible(True)
                self.fig.canvas.draw_idle()
            else:
                # Hide the annotation if the mouse is not over a data point
                if self.annot.get_visible():
                    self.annot.set_visible(False)
                    self.fig.canvas.draw_idle()


def run_Button():
    try:
        OutPut_entry.delete(1.0, tk.END)
        run_time_entry.delete(0, tk.END)
        run_times = f"{int(contents[3])+int(contents[5])}秒"
        run_time_entry.insert(0, run_times)
        time_out()
        update_out(int(contents[3]))
        OutPut_entry.insert(tk.END, "静态测试中，请稍等......\n")
        start_progress(int(contents[3]) + int(contents[5]))  # 假进度条
    except Exception as e:
        OutPut_entry.insert(tk.END, f"请查看配置文件或连接方式是否正确{e}\n")


def Reliabilitys_button():
    # 稳定性测试按钮
    try:
        OutPut_entry.insert(tk.END, "开始稳定性测试......\n")
        run_time_entry.delete(0, tk.END)
        run_times = f"{int(contents[10])}秒"
        run_time_entry.insert(0, run_times)
        time_out()
        Reliability_test(int(contents[10]), contents[9], contents[12])
        start_progress(int(contents[10]))  # 假进度条
    except Exception as e:
        OutPut_entry.delete(1.0, tk.END)
        OutPut_entry.insert(tk.END, f"请查看配置文件或连接方式是否正确{e}\n")


def clear_Button():
    standard_cn_entry.delete(0, tk.END)
    run_time_entry.delete(0, tk.END)
    modem_type_entry.delete(0, tk.END)
    modem_sn_entry.delete(0, tk.END)
    long_entry.delete(0, tk.END)
    Downlink_entry.delete(0, tk.END)
    Symbol_entry.delete(0, tk.END)
    cn_max_entry.delete(0, tk.END)
    cn_min_entry.delete(0, tk.END)
    cn_entry.delete(0, tk.END)
    entry_filename.delete(0, tk.END)
    jttest_entry.delete(0, tk.END)
    xntest_entry.delete(0, tk.END)
    kekaotest_entry.delete(0, tk.END)
    kekaotestyq_entry.delete(0, tk.END)
    xntestyq_entry.delete(0, tk.END)
    sqf_list.clear()


#
def start_progress(run_times):
    # 创建一个新线程来运行进度条
    progress_thread = threading.Thread(target=run_progress, args=(run_times,))
    progress_thread.start()


def run_progress(run_time):
    start_time = time.time()  # 记录开始时间
    end_time = start_time + run_time  # 计算结束时间
    progress["value"] = 0
    print("运行时间", run_time, "秒")

    # 循环直到当前时间超过或接近结束时间
    while time.time() < end_time:
        time.sleep(0.1)  # 模拟长时间运行的任务
        elapsed_time = time.time() - start_time  # 计算已经过去的时间
        progress_value = int((elapsed_time / run_time) * 100)  # 计算进度百分比
        progress["value"] = progress_value
        root.update_idletasks()  # 更新GUI但不处理事件


def time_out():
    # 时间设置
    jttest_entry.insert(0, f"{contents[3]}秒")
    xntest_entry.insert(0, f"{contents[5]}秒")
    kekaotest_entry.insert(0, f"{contents[10]}秒")
    models_sn()
    print_files = print_file()
    print(print_files)
    modem_type_entry.delete(0, tk.END)
    modem_type_entry.insert(0, contents[1])
    xntestyq_entry.insert(0, f"{contents[8]}")
    kekaotestyq_entry.insert(0, f"{contents[13]}")


def models_sn():
    api_value = api_modem_type()
    modem_sn_entry.delete(0, tk.END)  #
    modem_sn_entry.insert(0, api_value["esn"])
    long_entry.delete(0, tk.END)  # 插入经度
    long_entry.insert(0, api_value["satLong"])
    Downlink_entry.delete(0, tk.END)  # 插入下行频率
    Downlink_entry.insert(0, api_value["outroute_freq"])
    Symbol_entry.delete(0, tk.END)  # 插入符码率
    Symbol_entry.insert(0, api_value["symbol_rate"])
    cn_entry.delete(0, tk.END)


def update_out(seconds_remaining: int):
    # 将数据输出到控制
    api_value = api_modem_type()
    cn_entry.delete(0, tk.END)
    sqf = f"{float(api_value['sqf']) * 0.1:.2f}"
    cn_entry.insert(0, sqf)  # 插入实时信噪比
    sqf_list.append(float(sqf))
    cn_max_entry.delete(0, tk.END)
    cn_max_entry.insert(0, max(sqf_list))
    cn_min_entry.delete(0, tk.END)
    cn_min_entry.insert(0, min(sqf_list))
    print(sqf_list)
    # 减少剩余秒数
    seconds_remaining -= 1
    if seconds_remaining > 0:
        root.after(1000, lambda: update_out(seconds_remaining))
    else:
        if not static_test(contents[14]):
            raise ValueError("静态测试未通过")
        performance_preparation_test(contents[4], contents[7])


# class PingsButtons:
#     def __init__(self, master):
#         self.master = master
#         self.popup_window = None
#         self.result_queue = queue.Queue()

#         # Button to open the ping tool in a popup window
#         open_button = tk.Button(master, text="ping包", command=self.show_ping_tool)
#         open_button.grid(row=14, column=1)

#         # Check the platform and set the ping command accordingly
#         self.ping_command = "ping" if platform.system().lower() == "windows" else "ping -c"

#     def show_ping_tool(self):
#         self.popup_window = tk.Toplevel(self.master)
#         self.popup_window.title("Ping Tool")

#         tk.Label(self.popup_window, text="输入IP地址").grid(row=0, column=0)
#         self.target_host_entry = tk.Entry(self.popup_window)
#         self.target_host_entry.grid(row=0, column=1)

#         tk.Label(self.popup_window, text="循环次数").grid(row=1, column=0)
#         self.ping_count_entry = tk.Entry(self.popup_window, width=10)
#         self.ping_count_entry.grid(row=1, column=1)
#         self.ping_count_entry.insert(0, "1")

#         ping_button = tk.Button(self.popup_window, text="Ping", command=self.on_ping_button_click)
#         ping_button.grid(row=2, column=0, columnspan=2)

#         self.result_text = scrolledtext.ScrolledText(self.popup_window, wrap=tk.WORD, width=60, height=15)
#         self.result_text.grid(row=3, column=0, columnspan=2)

#         # Check the result queue periodically and update the result text if there's any new message
#         self.check_result_queue()

#     def on_ping_button_click(self):
#         target_host = self.target_host_entry.get()
#         try:
#             ping_count = int(self.ping_count_entry.get())
#             if ping_count < 1 or ping_count > 500:
#                 raise ValueError("Ping count must be between 1 and 500.")
#         except ValueError as e:
#             self.add_result(f"Warning: {e}")
#             return

#         if target_host:
#             self.result_text.delete('1.0', tk.END)
#             self.result_text.insert(tk.END, "ping包开始请稍等。。。。。。\n")
#             ping_thread = threading.Thread(target=self.ping_target, args=(target_host, ping_count))
#             ping_thread.start()
#         else:
#             self.add_result("Warning: Please enter a valid host address")

#     def ping_target(self, target_host, ping_count):
#         try:
#             if platform.system().lower() == "windows":
#                 completed_process = subprocess.run([self.ping_command, target_host, '-n', str(ping_count)],
#                                                    capture_output=True, text=True)
#             else:
#                 completed_process = subprocess.run([self.ping_command, str(ping_count), target_host],
#                                                    capture_output=True, text=True)

#             output = completed_process.stdout
#             if completed_process.returncode != 0:
#                 output += "\n" + completed_process.stderr
#             self.add_result(output)
#         except Exception as e:
#             self.add_result(f"Error: {e}")

#     def add_result(self, text):
#         self.result_queue.put(text)

#     def check_result_queue(self):
#         try:
#             while True:
#                 result = self.result_queue.get_nowait()
#                 self.result_text.insert(tk.END, result + "\n")
#                 self.result_text.see(tk.END)
#         except queue.Empty:
#             self.popup_window.after(100, self.check_result_queue)


def static_test(Performance_testing_drop_range):
    # 静态测试
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    ave = f"{sum(sqf_list)/len(sqf_list):.1f}"
    print("平均值：", ave)
    value = standard_cn_entry.get()  # 获取手动输入的信噪比
    ave = float(ave)
    if value:
        value = float(value)
    else:
        messagebox.showerror("错误", "请手动输入信噪比")
    if (
        ave - 0.5 <= value <= ave + 0.5
    ):  # 这个条件首先检查 value 是否在 ave 的0.5范围内（包括边界）。
        value1 = max(sqf_list) - min(sqf_list)
        values = round(value1, 2)
        if values > float(Performance_testing_drop_range):
            OutPut_entry.insert(
                tk.END, f"静态测试跌落范围超常 静态测试跌落范围值{values:.2f}\n"
            )
            max_value = max(sqf_list)
            result = [round(max_value, 2) - round(x, 2) for x in sqf_list]
            rounded_result = [round(num, 2) for num in result]
            print("静态result:", rounded_result)
            print("静态范围值：", Performance_testing_drop_range)
            results = [
                x
                for x in rounded_result
                if float(Performance_testing_drop_range) < float(x)
            ]
            print("results:", rounded_result)
            OutPut_entry.insert(tk.END, f"超出范围值个数{len(results)}\n")
            print(f"超出范围值个数{len(results)}\n")
            if sqf_list:
                proportion = (len(results) / len(sqf_list)) * 100
                OutPut_entry.insert(tk.END, f"超出的比例为：{proportion:.2f}%\n")
                print(f"超出的比例为：{proportion:.2f}%\n")
                messagebox.showerror("错误", "静态测试跌落范围超常")
                return False
        # HoverLineChartApp(root,sqf_list)
        print_time = f"当前时间：{current_time} "
        OutPut_entry.delete(1.0, tk.END)
        OutPut_entry.insert(
            tk.END, f"{print_time}:静态信噪比测试通过 当前平均值{ave}\n"
        )
        return True
    else:
        OutPut_entry.delete(1.0, tk.END)
        print_time = f"当前时间：{current_time} "
        OutPut_entry.insert(
            tk.END, f"{print_time}:静态信噪比测试未通过 当前平均值{ave}"
        )
        messagebox.showerror("错误", "静态测试跌落范围超常")
        return False


def performance_preparation_test(
    Performance_testing_drop_range, Exceeding_Extreme_Values
):
    # 性能测试准备工作
    value = max(sqf_list) - min(sqf_list)
    values = round(value, 2)
    print(Performance_testing_drop_range)
    if values > float(Performance_testing_drop_range):
        OutPut_entry.insert(
            tk.END, f"性能测试跌落范围超常 性能测试跌落范围值{value:.2f}\n"
        )
        if values > float(Exceeding_Extreme_Values):
            messagebox.showerror("错误", f"性能测试跌落超出极值 跌落值{value:.2f}")
            raise ValueError("性能测试跌落超出极值")
        else:
            max_value = max(sqf_list)
            result = [round(max_value, 2) - round(x, 2) for x in sqf_list]
            rounded_result = [round(num, 2) for num in result]
            print("result:", rounded_result)
            print("范围值：", Performance_testing_drop_range)
            results = [
                x
                for x in rounded_result
                if float(Performance_testing_drop_range) < float(x)
            ]
            print("results:", rounded_result)
            OutPut_entry.insert(tk.END, f"超出范围值个数{len(results)}\n")
            print(f"超出范围值个数{len(results)}\n")
            if sqf_list:
                proportion = (len(results) / len(sqf_list)) * 100
                OutPut_entry.insert(tk.END, f"超出的比例为：{proportion:.2f}%\n")
                print(f"超出的比例为：{proportion:.2f}%\n")

            else:
                OutPut_entry.insert(tk.END, "列表为空，无法计算比例。\n")
    else:
        OutPut_entry.insert(
            tk.END,
            f"静态测试跌落范围正常 跌落范围值{value:.2f}\n开始进行性能测试......\n",
        )
        sqf_list.clear()
        performance_test(int(contents[5]), contents[4], contents[7])


def performance_test(
    Performance_test_swing_duration,
    Performance_testing_drop_range,
    Exceeding_Extreme_Values,
):
    # 性能测试
    api_value = api_modem_type()
    cn_entry.delete(0, tk.END)
    sqf = f"{float(api_value['sqf']) * 0.1:.2f}"
    cn_entry.insert(0, sqf)  # 插入实时信噪比
    sqf_list.append(float(sqf))
    cn_max_entry.delete(0, tk.END)
    cn_max_entry.insert(0, max(sqf_list))
    cn_min_entry.delete(0, tk.END)
    cn_min_entry.insert(0, min(sqf_list))
    print(sqf_list)
    # 减少剩余秒数
    Performance_test_swing_duration -= 1
    if Performance_test_swing_duration > 0:
        root.after(
            1000,
            lambda: performance_test(
                Performance_test_swing_duration,
                Performance_testing_drop_range,
                Exceeding_Extreme_Values,
            ),
        )
    else:
        value = max(sqf_list) - min(sqf_list)
        values = round(value, 2)
        OutPut_entry.insert(tk.END, f"性能测试完成\n性能跌落范围值{values}\n")
        if values > float(Exceeding_Extreme_Values):
            messagebox.showerror("错误", f"性能测试跌落超出极值 跌落值{value:.2f}")
            raise ValueError("性能测试跌落超出极值")
        else:
            max_value = max(sqf_list)
            result = [round(max_value, 2) - round(x, 2) for x in sqf_list]
            rounded_result = [round(num, 2) for num in result]
            print("result:", rounded_result)
            print("范围值：", Performance_testing_drop_range)
            results = [
                x
                for x in rounded_result
                if float(Performance_testing_drop_range) < float(x)
            ]
            print("results:", rounded_result)
            OutPut_entry.insert(tk.END, f"性能超出范围值个数{len(results)}\n")
            print(f"性能超出范围值个数{len(results)}\n")
            if sqf_list:
                proportion = (len(results) / len(sqf_list)) * 100
                OutPut_entry.insert(tk.END, f"性能超出的比例为：{proportion:.2f}%\n")
                if round(proportion, 2) < int(contents[6]):
                    OutPut_entry.insert(
                        tk.END, f"性能超出的比例小于设定值{contents[6]}%,性能测试通过\n"
                    )
                else:
                    messagebox.showerror(
                        "错误", f"性能超出的比例大于设定值{contents[6]}%,性能测试失败"
                    )
                    OutPut_entry.insert(
                        tk.END, f"性能超出的比例大于设定值{contents[6]}%,性能测试失败\n"
                    )
                print(f"性能超出的比例为：{proportion:.2f}%\n")
                HoverLineChartApp(root, sqf_list)
            else:
                OutPut_entry.insert(tk.END, "列表为空，无法计算比例。\n")


def Reliability_test(
    seconds_remaining, Performance_testing_drop_range, Exceeding_Extreme_Values
):
    # 可靠性的测试
    api_value = api_modem_type()
    cn_entry.delete(0, tk.END)
    sqf = f"{float(api_value['sqf']) * 0.1:.2f}"
    cn_entry.insert(0, sqf)  # 插入实时信噪比
    sqf_list.append(float(sqf))
    cn_max_entry.delete(0, tk.END)
    cn_max_entry.insert(0, max(sqf_list))
    cn_min_entry.delete(0, tk.END)
    cn_min_entry.insert(0, min(sqf_list))
    print(sqf_list)
    # 减少剩余秒数
    seconds_remaining -= 1
    if seconds_remaining > 0:
        root.after(
            1000,
            lambda: Reliability_test(
                seconds_remaining,
                Performance_testing_drop_range,
                Exceeding_Extreme_Values,
            ),
        )
    else:
        value = max(sqf_list) - min(sqf_list)
        values = round(value, 2)
        OutPut_entry.insert(tk.END, f"稳定性测试完成......稳定性跌落范围值{values}\n")
        max_value = max(sqf_list)
        if values > float(Exceeding_Extreme_Values):
            messagebox.showerror("错误", f"稳定性测试跌落超出极值 跌落值{value:.2f}")
            raise ValueError("稳定性测试跌落超出极值")
        else:
            result = [round(max_value, 2) - round(x, 2) for x in sqf_list]
            rounded_result = [round(num, 2) for num in result]
            print("result:", rounded_result)
            print("范围值：", Performance_testing_drop_range)
            results = [
                x
                for x in rounded_result
                if float(Performance_testing_drop_range) < float(x)
            ]
            print("results:", rounded_result)
            OutPut_entry.insert(tk.END, f"稳定性超出范围值个数{len(results)}\n")
            print(f"稳定性超出范围值个数{len(results)}\n")
            if sqf_list:
                proportion = (len(results) / len(sqf_list)) * 100
                OutPut_entry.insert(tk.END, f"稳定性超出的比例为：{proportion:.2f}%\n")
                if round(proportion, 2) < int(contents[6]):
                    OutPut_entry.insert(
                        tk.END,
                        f"稳定性超出的比例小于设定值{contents[11]}%,稳定性测试通过\n",
                    )
                else:
                    messagebox.showerror(
                        "错误",
                        f"稳定性超出的比例大于设定值{contents[11]}%,稳定性测试失败",
                    )
                    OutPut_entry.insert(
                        tk.END,
                        f"稳定性超出的比例大于设定值{contents[11]}%,稳定性测试失败\n",
                    )
                print(f"稳定性超出的比例为：{proportion:.2f}%\n")
                HoverLineChartApp(root, sqf_list)
            else:
                OutPut_entry.insert(tk.END, "列表为空，无法计算比例。\n")


def open_file():
    # 打开文件
    filename = filedialog.askopenfilename(
        title="打开txt文件", filetypes=[("txt files", "*.txt")]
    )
    global contents
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()  # 读取所有行
            if len(lines) > 1:  # 确保有两行数据
                # 跳过第一行
                content = ",".join(lines[1:])  # 将从第二行开始的所有行合并为一个字符串
                contents = content.split(",")
            else:
                messagebox.showerror("错误", "配置文件内容错误！")
                return  # 提前返回，不更新Entry控件
        entry_filename.delete(0, tk.END)  # 清空Entry控件
        entry_filename.insert(0, filename)  # 插入文件名
        # 读取文件内容


def print_file():
    # 打印文件数据
    a = entry_filename.get()  # 用get提取entry中的内容
    return a


def api_modem_type():
    # 匹配猫型号
    try:
        if contents[1] == Color.modem_xiusi.value:
            res_sn = http_requests_sn_ht2500_api()
            res_modem = http_requests_modem_ht2500_api()
            esn = res_sn["esn"]  # sn号
            satLong = res_modem["beam_info"]["satLong"]  # 卫星经度
            outroute_freq = res_modem["downlink"]["outroute_freq"]  # 下行频率
            symbol_rate = res_modem["downlink"]["symbol_rate"]  # 符码率
            sqf = res_modem["downlink"]["sqf"]  # 信噪比
            return {
                "esn": esn,
                "satLong": satLong,
                "outroute_freq": outroute_freq,
                "symbol_rate": symbol_rate,
                "sqf": sqf,
            }
        elif contents[1] == Color.modem_503.value:
            res_modem = http_requests_modem_503_api()
            res_sn = http_requests_sn_503_api()
            esn = res_sn["rcstMac"]
            satLong = res_modem["satellite_name_now"]
            outroute_freq = res_modem["u32_current_freq"]
            symbol_rate = res_modem["u32_current_srate"]
            sqf = res_modem["s32_fwd_snr"]  # 信噪比
            return {
                "esn": esn,
                "satLong": satLong,
                "outroute_freq": outroute_freq,
                "symbol_rate": symbol_rate,
                "sqf": sqf,
            }
        elif contents[1] == Color.modem_UHP.value:
            uhp_oid = UHP_OID()
            snmp_sn = snmp_get(uhp_oid.SN)
            snmp_modem = snmp_get(uhp_oid.SR)
            hexadecimal_with_prefix = hex(int(snmp_sn))
            esn = hexadecimal_with_prefix[2:]
            sqf = snmp_modem
            return {
                "esn": esn,
                "satLong": "satLong",
                "outroute_freq": "outroute_freq",
                "symbol_rate": "symbol_rate",
                "sqf": sqf,
            }
        else:
            messagebox.showerror(
                "错误", "modem类型匹配失败，请确认当前modem类型是否填写正确"
            )
    except Exception as e:
        OutPut_entry.insert(tk.END, f"连接失败请检查连接配置或网络情况......{e}\n")


def http_requests_sn_ht2500_api():
    # 获取sn号
    url_sn = "http://192.168.0.1/api/system/terminal_info"
    response_sn = requests.get(url=url_sn)
    res_sn = response_sn.json()
    return res_sn


def http_requests_modem_ht2500_api():
    # 获取信噪比等信息
    url_modem = "http://192.168.0.1/api/home/aero/aero_stats"
    response_sn = requests.get(url=url_modem)
    res_modem = response_sn.json()
    return res_modem


def http_requests_modem_503_api():
    url_modem = "http://192.168.0.1/action/fwdStatusGet"
    response_modem = requests.get(url=url_modem)
    res_modem = response_modem.json()
    return res_modem


def http_requests_sn_503_api():
    url_sn = "http://192.168.0.1/action/managerNetworkGet"
    response_sn = requests.post(url=url_sn)
    res_sn = response_sn.json()
    return res_sn


def snmp_get(oid: str):
    cg = cmdgen.CommandGenerator()  ##获得CommandGenerator对象
    errorIndication, errorStatus, errorIndex, varBinds = cg.getCmd(
        # 0代表v1,1代表v2c
        cmdgen.CommunityData("myagent", community_string, 1),
        cmdgen.UdpTransportTarget((target_host, 161)),
        oid,
    )
    for name, val in varBinds:
        name: ObjectIdentity
        val: ObjectIdentity
        return val.prettyPrint()


# 创建主窗口UI
root = tk.Tk()
root.geometry("800x600")
root.title("V1.0.3 获取信噪比")
# 创建Label控件来显示时间前缀
standard_cn_label = tk.Label(root, text="标准天线信噪值:", width=15)
standard_cn_label.grid(row=0, column=0)
standard_cn_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
standard_cn_entry.grid(row=0, column=1)

cn_label = tk.Label(root, text="实时信噪比:", width=10)
cn_label.grid(row=1, column=0)
cn_entry = tk.Entry(root, font=("calibri", 10, "bold"), background="white", width=20)
cn_entry.grid(row=1, column=1)

cn_max_label = tk.Label(root, text="信噪最大值:", width=10)
cn_max_label.grid(row=3, column=0)
cn_max_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
cn_max_entry.grid(row=3, column=1)

cn_min_label = tk.Label(root, text="信噪最小值:", width=10)
cn_min_label.grid(row=4, column=0)
cn_min_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
cn_min_entry.grid(row=4, column=1)

satellite_label = tk.Label(root, text="卫星信息:", width=10)
satellite_label.grid(row=5, column=0)

long_label = tk.Label(root, text="经度:", width=10)
long_label.grid(row=6, column=0)
long_entry = tk.Entry(root, font=("calibri", 10, "bold"), background="white", width=20)
long_entry.grid(row=6, column=1)

Downlink_label = tk.Label(root, text="下行频率:", width=10)
Downlink_label.grid(row=7, column=0)
Downlink_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
Downlink_entry.grid(row=7, column=1)

Symbol_label = tk.Label(root, text="符码率:", width=10)
Symbol_label.grid(row=8, column=0)
Symbol_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
Symbol_entry.grid(row=8, column=1)

run_time_label = tk.Label(root, text="预计测试时间:", width=10)
run_time_label.grid(row=0, column=3)
run_time_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
run_time_entry.grid(row=0, column=4)

modem_type_label = tk.Label(root, text="modem类型:", width=10)
modem_type_label.grid(row=1, column=3)
modem_type_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
modem_type_entry.grid(row=1, column=4)
# modem_type_comboxlist=ttk.Combobox(root,width=18)
# modem_type_comboxlist["values"]=("修斯","503","UHP")
# modem_type_comboxlist.current(0)
# modem_type_comboxlist.bind("<<comboboxselected>>",selectedlins)
# modem_type_comboxlist.grid(row=1, column=4)

modem_sn_label = tk.Label(root, text="modem S/N:", width=10)
modem_sn_label.grid(row=3, column=3)
modem_sn_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
modem_sn_entry.grid(row=3, column=4)

button_import = tk.Button(root, text="导入文件配置", command=open_file)
button_import.grid(row=4, column=3)

entry_filename = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
entry_filename.grid(row=4, column=4)

test_label = tk.Label(root, text="测试要求:", width=10)
test_label.grid(row=5, column=3)

jttest_label = tk.Label(root, text="静态测试，测试时长", width=20)
jttest_label.grid(row=6, column=3)
jttest_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
jttest_entry.grid(row=6, column=4)

xntest_label = tk.Label(root, text="性能测试，测试时长:", width=20)
xntest_label.grid(row=7, column=3)
xntest_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
xntest_entry.grid(row=7, column=4)

kekaotest_label = tk.Label(root, text="稳定性测试，测试时长:", width=20)
kekaotest_label.grid(row=8, column=3)
kekaotest_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
kekaotest_entry.grid(row=8, column=4)

xntestyq_label = tk.Label(root, text="性能摇摆台要求:", width=20)
xntestyq_label.grid(row=9, column=3)
xntestyq_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
xntestyq_entry.grid(row=9, column=4)

kekaotestyq_label = tk.Label(root, text="稳定性摇摆台要求:", width=20)
kekaotestyq_label.grid(row=10, column=3)
kekaotestyq_entry = tk.Entry(
    root, font=("calibri", 10, "bold"), background="white", width=20
)
kekaotestyq_entry.grid(row=10, column=4)

# #输出结果
OutPut_entry = scrolledtext.ScrolledText(
    root,
    width=80,
    height=15,
    font=("calibri", 10, "bold"),
    undo=True,
    autoseparators=False,
)
OutPut_entry.grid(row=12, columnspan=5)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.grid(row=13, columnspan=5)

# 创建按钮
run_button = tk.Button(root, text="运行", command=run_Button)
run_button.grid(row=13, column=5)

clear_button = tk.Button(root, text="清空", command=clear_Button)
clear_button.grid(row=13, column=6)

Reliability_button = tk.Button(root, text="稳定性运行", command=Reliabilitys_button)
Reliability_button.grid(row=13, column=7)


if __name__ == "__main__":
    # 运行主循环
    # 新增版本号
    app = HoverLineChartApp(root, sqf_list)
    # ping_buttons = PingsButtons(root)
    root.mainloop()
