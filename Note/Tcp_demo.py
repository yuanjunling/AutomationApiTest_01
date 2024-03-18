# 导入socket模块
import socket
# 定义要发送的数据列表
data_list = ["$GCCMD,GET ANT DIR*30\r\n", '$GCCMD,GET INS DATA*70\r\n', "$GCCMD,GET SAT DATA*62\r\n",
             '$GCCMD,GET MODEM INFO*74\r\n', '$GCCMD,GET SYS INFO*63\r\n', '$GCCMD,GET ANT ALM*2f\r\n','$GCCMD,SYSTEM RESET,0*0e\r\n']

# 创建socket连接
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # 连接到指定主机和端口
    client.connect(("192.168.0.2", 15102))
    # 循环发送数据
    while True:
        # 遍历要发送的数据
        for re_data in data_list:
            # re_data = "$GCCMD,AUTO SEARCH SET,125.00,1344.7,3,104500,0,1,0,1,0,0,3,18050,33*32\r\n"
            try:
                # 将要发送的数据转换为utf-8编码
                client.send(re_data.encode("utf-8"))
            except Exception as e:
                raise e
                                                                                  # 接收数据
            data = client.recv(1024)
            # 将接收到的数据转换为utf8编码
            print(data.decode("utf8"))