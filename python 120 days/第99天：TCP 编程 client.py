# 导入socket库
import socket

import socket
import time

# 创建 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(("127.0.0.1", 6000))

# 接收服务器消息
print(s.recv(1024).decode())

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.send(data)
    time.sleep(2)
    # 打印接收到的数据
    print(s.recv(1024).decode('utf-8'))
    time.sleep(1)

time.sleep(3)
# 请求退出
s.send(b'exit')
time.sleep(2)
print(s.recv(1024).decode('utf-8'))

# 关闭连接
s.close()

# # 创建一个socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接
# s.connect(("127.0.0.1", 6000))
# # 创建socket时，第一个参数socketAF_INET表示指定使用IPv4协议，如果要使用IPv6协议，
# # 就指定为socket.AF_INET6。SOCK_STREAM指定使用面向流的TCP协议。然后调用connect()方法，
# # 传入IP地址（或者域名），指定端口号就可以建立连接了。
# # 向服务器发送数据：
# s.send(b'Hello Mr Right!')
# # 接收数据时，调用recv(1024)方法，一次最多接收指定的字节数。
# # 在一个while循环种反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
# # 接收数据
# buffer = []
# while True:
#     # 每次最多接收1k字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 关闭连接
# s.close()