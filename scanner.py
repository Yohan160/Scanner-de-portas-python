import socket

def scan_ports(ip):
    open_ports = []

    print(f"ESCANEANDO: {ip}")

    for port in range(1, 100):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)

        result = sock.connect_ex((ip, port))

        print(f"Testando porta {port} -> {result}")  

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports