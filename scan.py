import socket

host = input("Enter host: ")

start_port = int(input("enter start port: "))
end_port = int(input("enter end port: "))

for port in range(start_port, end_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0)
    result = sock.connect_ex((host, port))
    if result == 0:
        print("port {}: Open".format(port))
    sock.close()
