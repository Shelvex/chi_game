from socket import *
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 服务端的IP地址和使用的接口

""" 
10.28.2.245 笔记本IPv4地址
"""

"""
台式电脑 10.32.49.51
"""

# serve_ip = "192.168.1.3"
serve_ip = "10.28.2.245 "
serve_port = 8000

tcp_socket.connect((serve_ip, serve_port))
while(1):
    send_data=input("Please input:") # 输入想发给服务端的信息
    tcp_socket.send(send_data.encode("gbk"))
    if send_data == "exit": # 断开连接
        break
    from_server_msg=tcp_socket.recv(1024) # 接收服务端的答复
    print(from_server_msg.decode("gbk"))
tcp_socket.close()
