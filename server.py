import socket
"""服务端"""
# 创建一个TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定主机和端口
server_socket.bind(('127.0.0.1', 12345))
# 10.28.2.245 笔记本IPv4地址

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