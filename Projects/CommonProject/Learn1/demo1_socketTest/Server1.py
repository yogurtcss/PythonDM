import socket

""" socket 编程思路：
服务端： (TCP 编程)
1.创建套接字，绑定套接字到本地 IP 与端口：
    socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind ()
2.开始监听连接：s.listen()
3.进入循环，不断接受客户端的连接请求：s.accept()
4.接收传来的数据，或者发送数据给对方：s.recv() , s.sendall()
5.传输完毕后，关闭套接字：s.close()
"""


""" 2020-02-03 12:03:24
win10 使用cmd输入命令，查看端口情况
1.命令netstat -ano：列出所有端口的使用情况
2.命令netstat  -ano | findstr "8080"：查看被占用端口8080对应的 PID;

此处的9999端口未被占用嗷
"""

""" 注意：
1.Python3 以后，socket 传递的都是 bytes 类型的数据，
若接收到字符串，需要先转换一下，string.encode() 即可；
另一端接收到的 bytes 数据想转换成字符串，只要 bytes.decode() 一下就可以。

2.在正常通信时，accept()和recv() 方法都是阻塞的。
所谓的阻塞，指的是程序会暂停在那，一直等到有数据过来。

"""

ip_port = ('127.0.0.1', 9999)  # 主机地址127.0.0.1、端口号9999

sk = socket.socket()  # 创建套接字
sk.bind(ip_port)  # 绑定服务地址
sk.listen(5)  # 监听连接请求
""" 服务器socket对象.listen(...某个数...) 方法：
开始监听连接；backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量。
该值至少为 1，大部分应用程序设为 5 就可以了。
"""

print("启动socket服务，等待客户端连接...")
(conn, address) = sk.accept()  # 等待连接，此处自动阻塞
""" 服务器socket对象.accept(...空参...) 方法：
被动接受客户端连接，(阻塞式)等待连接的到来，并返回（conn,address）二元元组，
其中 conn 是一个通信对象(实际上也是socket对象)，可以用来接收和发送数据；
address 是连接客户端的地址。

//每个socket对象就是一个抽象的 “通信对象”
"""
while True:
    """ 2020-02-03 12:46:09
    Python3 以后，socket 传递的都是 bytes类型的数据，
    若接收到字符串，则需要先转换一下，string.encode() 即可；
    另一端接收到的 bytes 数据想转换成字符串，只要 bytes.decode() 一下就可以。
    """
    client_data = conn.recv(1024).decode()  # 接收信息
    """ (socket对象或)连接对象conn.recv(...某个数字bufsize...) 方法：
    接收数据，数据以 bytes 类型返回，bufsize 指定要接收的最大数据量
    """

    if client_data == "exit":  # 判断是否退出连接
        exit("通信结束")
        break

    print("来自%s的客户端向你发来消息：%s" % (address, client_data))
    """ %s是啥？
    Python使用一个字符串作为模板。
    模板中有格式符(或 占位符)，这些格式符(或 占位符)为真实值预留位置，
    //类似 Java中 SQL语句的 ?,? 占位符
    
    字符串中使用 "%s , %s" 占位符，后面紧跟着 %( 变量1, 变量2, ...,  )
    按先后顺序替换原本的占位符嗷！
    """

    conn.sendall("服务器已经接收到你的消息".encode())   # 回馈信息给客户端
    """ (socket对象或)通信对象conn.sendall()方法
    完整发送数据。将数据发送到连接的套接字，
    但在返回之前会尝试发送所有数据。
    成功返回 None，失败则抛出异常。
    """

conn.close()   # 关闭连接
