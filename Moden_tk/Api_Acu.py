import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinter import scrolledtext
import threading
from pydantic import BaseModel
import requests
import json
import socket, time


# 创建主窗口UI
root = tk.Tk()
root.geometry("800x600")
root.title("ACU_API")


class DATAINFO(BaseModel):
    httpip: str = "192.168.100.1"
    prots: int = 15103


datainfo = DATAINFO()

options = ["天线1", "天线2"]

# =====================================================================================


def get_api_info(param):
    url = f"http://{datainfo.httpip}:{datainfo.prots}/{param}"
    value = 1 if dropdown.get() == "天线1" else 2
    jsons = {"ant_type": value}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, headers=headers, json=jsons)
    res = json.dumps(response.json(), indent=4)
    OutPut_entry.insert(tk.END, f"{res}\n")


def tcp_api_info(param):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("172.19.200.253", 15102))
        re_data = param
        client.send(re_data.encode("utf-8"))
        data = client.recv(1024)
        OutPut_entry.insert(tk.END, f"{data}\n")


def get_ant_state_info():
    get_api_info("get_ant_state_info")


def get_ins_info():
    get_api_info("get_ins_info")


dropdown = tk.StringVar(root)
dropdown.set(options[0])
dropdown_menu = tk.OptionMenu(root, dropdown, *options)  # 创建下拉框
dropdown_menu.grid(row=0, column=0)  # 将下拉框放置在窗口中

button_import = tk.Button(root, text="获取天线状态信息", command=get_ant_state_info)
button_import.grid(row=1, column=0)

button_imports = tk.Button(root, text="获取惯导信息", command=get_ins_info)
button_imports.grid(row=2, column=0)

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

if __name__ == "__main__":
    root.mainloop()
