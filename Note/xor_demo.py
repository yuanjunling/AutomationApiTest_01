from typing import Any
from rich import print
def xor_checksum(data:Any):
    checksum = 0
    for b in data.encode("utf-8"):
        checksum ^= b  # 进行异或运算
    return checksum

#设置天线
# data = "GCCMD,AUTO SEARCH SET,125.00,1344.7,3,104500,100,1,0,1,0,0,3,18050,33"
data="GCCMD,AUTO SEARCH SET,105.50,1936.250,0,50000,0,0,0,1,0,0,3,10600,33"

# 计算校验值
checksum = xor_checksum(data)
print("[bold red]Data:", data)

# 将校验值转化为 16 进制
hex_checksum = hex(checksum)[2:].zfill(2)
print(f"[bold red]${data}*{hex_checksum}\\r\\n")

# 校验数据
if xor_checksum(data) == int(hex_checksum, 16):
    print("[bold red]Data is valid")
else:
    print("[bold red]Data is invalid")