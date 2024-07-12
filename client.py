import socket

# 创建一个TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
# 127.0.0.1 虚拟网络？ 本地网络
# 像stable diffusion那样 本地网络服务器 或者说终端

# 10.28.2.245 笔记本IPv4地址

client_socket.connect(('127.0.0.1', 12345))

# 发送数据
data_to_send = "Hello, server!"
client_socket.send(data_to_send.encode('utf-8'))

# 接收响应
response = client_socket.recv(1024)
print(f"Received response: {response.decode('utf-8')}")

# 关闭连接
client_socket.close()