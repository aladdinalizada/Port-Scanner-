import socket


def get_ip():
    ip_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip_s.connect(("10.255.255.255", 1))
        new_ip = ip_s.getsockname()[0]
    except:
        new_ip = "127.0.0.1"
    finally:
        ip_s.close()


your_ip = get_ip()


for port in range(1, 65536):
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = soket.connect_ex((your_ip, port))
    if result == 0:
        print("Port {}: \t Open".format(port))
    soket.close()


# Path: portScanner.py
