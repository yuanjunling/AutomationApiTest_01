import socket


class UDPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        self.socket.sendto(data.encode(), (self.host, self.port))

    def receive(self, bufsize=1024):
        return self.socket.recvfrom(bufsize)

    def close(self):
        self.socket.close()


# Usage:
if __name__ == "__main__":
    client = UDPClient("127.0.0.1", 5000)
    client.send("Hello Server")
    response, address = client.receive()
    print(response)
    client.close()
