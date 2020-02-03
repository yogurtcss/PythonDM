import threading

import sys

""" 路径名必需用双_反斜杠\\
使用 sys.append( r'自定义的模块路径' )，将自定义模块所在路径添加到搜索路径
"""
sys.path.append(r"H:\\ProcExes\\PyFiles\\PythonDM\\Projects\\CommonProject\\Learn1\\demo2_withJava\\func")

import SqlFun1  # 虽然飘红，但还是能运行的！


class ServerThreading(threading.Thread):
    def __init__(self, clientSocket):
        super().__init__()
        self.clientSocket = clientSocket

    def run(self):

        try:
            SqlFun1.insert1()
            self.clientSocket.sendall("操作数据库成功！".encode("utf-8"))
        except Exception as e:
            print(e)
        finally:
            self.clientSocket.close()
        print("任务结束")