# local socket

"""客户端 """
import socket

# 创建一个TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect(('127.0.0.1', 12345))

# 发送数据
data_to_send = "Hello, server!"
client_socket.send(data_to_send.encode('utf-8'))

# 接收响应
response = client_socket.recv(1024)
print(f"Received response: {response.decode('utf-8')}")

# 关闭连接
client_socket.close()
"""服务端"""
# 创建一个TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定主机和端口
server_socket.bind(('127.0.0.1', 12345))

# 监听连接
server_socket.listen()

print("Server is listening for incoming connections...")

# 接受客户端连接
client_socket, client_address = server_socket.accept()

print(f"Connection established with {client_address}")

# 接收数据
data = client_socket.recv(1024)
print(f"Received data: {data.decode('utf-8')}")

# 发送响应
response = "Hello, client!"
client_socket.send(response.encode('utf-8'))

# 关闭连接
client_socket.close()
server_socket.close()