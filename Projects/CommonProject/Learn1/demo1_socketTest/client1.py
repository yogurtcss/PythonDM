import socket

""" socket 编程思路：
客户端： (TCP 编程)
1.创建套接字，连接服务器地址：socket.socket(socket.AF_INET,socket.SOCK_STREAM),   s.connect()
2.连接后发送数据和接收数据：s.sendall(), s.recv()
3.传输完毕后，关闭套接字：s.close()
"""

ip_port = ('127.0.0.1', 9999)

s = socket.socket()
s.connect(ip_port)

while True:
    inp = input("请输入要发送的消息：").strip()
    if not inp:  # 防止输入空消息，而导致异常退出
        continue

    s.sendall(inp.encode())

    if inp == "exit":
        print("结束通信！")
        break

    server_reply = s.recv(1024).decode()
    print(server_reply)

s.close()
