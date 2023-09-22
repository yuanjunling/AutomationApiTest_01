def xor_checksum(data):
    checksum = 0
    for b in data.encode("utf-8"):
        checksum ^= b  # 进行异或运算
    return checksum


data = "GCCMD,GET ANT DIR"

checksum = xor_checksum(data)
print("Data:", data)

# 将校验值转化为 16 进制
hex_checksum = hex(checksum)[2:].zfill(2)
print(f"${data}*{hex_checksum}<CR><LF>")

# 校验数据
if xor_checksum(data) == int(hex_checksum, 16):
    print("Data is valid")
else:
    print("Data is invalid")
