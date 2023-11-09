import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("192.168.0.2", 15102))
    while True:
        re_data = "$GCCMD,GET SYS SINFO*30\r\n"
        try:
            client.send(re_data.encode("utf-8"))
        except Exception as e:
            print(e)
        data = client.recv(1024)
        print(data.decode("utf8"))


