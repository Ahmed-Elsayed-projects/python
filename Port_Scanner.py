import socket
from IPy import IP

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def scan(address, startport = 1, endport = 100):
    open_ports = []
    for port in range(startport, endport):
        try:
            sock = socket.socket()
            ipaddress = check_ip(address)
            sock.settimeout(0.5)
            sock.connect((ipaddress, port))
            try:
                banner = sock.recv(1024)
                open_ports.append([port, banner.decode()])
            except:
                open_ports.append([port])
        except:
            pass
    return open_ports

ports = scan('192.168.0.17', 120, 160)
print(ports)
import time
time.sleep(30)
