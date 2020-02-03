import socket
import sys

from demo2_withJava.classes1.Thread1 import ServerThreading

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()  # 创建套接字
sk.bind(ip_port)  # 绑定服务地址
sk.listen(5)  # 监听连接请求
print("启动socket服务，等待客户端连接...")

while True:
    # 要把这句话放进 永真循环 中
    (conn, address) = sk.accept()  # 等待连接，此处自动阻塞

    try:
        clientData = conn.recv(1024).decode()

        if clientData == "start":
            t = ServerThreading(conn)
            t.start()

    except Exception as e:
        print(e)