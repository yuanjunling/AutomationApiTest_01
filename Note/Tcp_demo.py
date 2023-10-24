import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.1", 15103))
while True:
    re_data = "$GCCMD,GET ANT DIR*30<CR><LF>"
    client.send(re_data.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode("utf8"))
