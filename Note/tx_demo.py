import tkinter as tk


# 创建主窗口
window = tk.Tk()
window.title("XOR Checksum Demo")
window.geometry("500x200")


# XOR校验和算法
def xor_checksum(data):
    checksum = 0
    for b in data.encode("utf-8"):
        checksum ^= b
    return checksum


# 验证数据的函数
def validate_data():
    data = data_entry.get()  # 获取输入的数据
    checksum = xor_checksum(data)  # 计算校验和

    hex_checksum = hex(checksum)[2:].zfill(2)  # 转换为16进制格式
    result_text.set(hex_checksum)  # 显示数据和校验和

    # 比较计算出的校验和和转换后的校验和
    if xor_checksum(data) == int(hex_checksum, 16):
        valid_label.config(text="Data is valid")  # 数据有效
    else:
        valid_label.config(text="Data is invalid")  # 数据无效


# 创建输入框
data_entry = tk.Entry(window, width=60)
data_entry.pack()

# 创建验证按钮
validate_button = tk.Button(window, text="生成校验码", command=validate_data)
validate_button.pack()

# 显示数据和校验和
result_text = tk.StringVar()
result_label = tk.Entry(window, width=60, textvariable=result_text)
result_label.pack()

# 显示数据有效性
valid_label = tk.Label(window)
valid_label.pack()

window.mainloop()
