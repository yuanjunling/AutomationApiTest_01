import tkinter as tk
import serial
import time
from tkinter import messagebox

# 串口通信配置
SERIAL_PORT = 'COM11'
BAUD_RATE = 115200
TIMEOUT = 1

# 创建串口对象
ser = serial.Serial(
    port=SERIAL_PORT,
    baudrate=BAUD_RATE,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=TIMEOUT
)


# GUI窗口类
class SerialGUI:
    def __init__(self, master):
        self.master = master
        master.title("Serial Communication")
        master.geometry("300x200")

        # 添加输入框用于输入指令
        self.input_var = tk.StringVar()  # 创建StringVar对象用于存储输入框的值
        self.input_entry = tk.Entry(master, textvariable=self.input_var)  # 创建输入框组件，并与StringVar对象关联
        self.input_entry.pack()
        self.input_entry.bind('<Return>', self.send_data)  # 绑定回车键事件到发送数据函数

        # 添加“发送”按钮
        self.send_button = tk.Button(master, text="发送数据", command=self.send_data)
        self.send_button.pack()

        # 添加“关闭”按钮
        self.close_button = tk.Button(master, text="关闭串口", command=self.close_serial)
        self.close_button.pack()

        # 添加输出框用于显示接收到的数据
        self.output_var = tk.StringVar()  # 创建新的StringVar对象用于存储接收数据的输入框的值
        self.output_entry = tk.Entry(master, textvariable=self.output_var, state='readonly')  # 创建只读输入框组件，用于显示接收到的数据
        self.output_entry.pack()

        # 启动定时器，定时检查串口接收数据
        self.receive_data_timer = self.master.after(100, self.check_receive_data)  # 每100毫秒检查一次接收数据

    def send_data(self, event=None):  # 添加event参数以便绑定回车键事件时使用
        command = self.input_var.get()  # 获取输入框中的指令
        if command:  # 判断指令是否为空
            message = f"{command}\r\n"  # 添加换行符
            ser.write(message.encode())  # 将指令编码为字节流后发送
            print("Sent:", message)
            self.input_var.set("")  # 清空输入框，等待接收新数据
        else:
            messagebox.showwarning("警告", "指令不能为空")  # 如果指令为空，弹出警告对话框

    def check_receive_data(self):
        response = ser.readline().decode().strip()  # 读取一行数据并解码为字符串，去掉结尾的换行符
        if response:  # 判断是否接收到新数据
            print("Received:", response)
            self.output_var.set(
                response)  # 在输出框中显示接收到的数据，而不是输入框中显示接收到的数据，实现发送数据和返回数据显示在不同的输入框中。如果你仍然想在输入框中显示接收到的数据，你可以将这行代码更改为 self.input_var.set(response) 。但是，请注意，这将会覆盖你发送的指令。所以建议你使用一个新的输入框来显示接收到的数据。希望这能帮到你！            self.receive_data_timer = self.master.after(100, self.check_receive_data)  # 重新启动定时器，继续检查接收数据

    def close_serial(self):
        ser.close()
        messagebox.showinfo("提示", "串口已关闭")
        self.master.destroy()  # 关闭窗口
        self.master.after_cancel(self.receive_data_timer)  # 取消定时器，停止检查接收数据

# 主程序入口点
if __name__ == "__main__":
    root = tk.Tk()  # 创建主窗口对象
    app = SerialGUI(root)  # 创建GUI窗口对象并运行主循环
    root.mainloop()  # 运行主循环，等待用户操作