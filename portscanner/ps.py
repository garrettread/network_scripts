import socket
import time
import os



host = "google.com"
ports = [22, 80, 443, 8080]

with open("port_scan_log.txt", "a") as file:
    file.write(f'---------------{host}---------------\n')
    for port in ports:
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                file.write(f"Port {port}: OPEN\n")
            else:
                file.write(f"Port {port}: CLOSED\n")
            s.close()
        except Exception as e:
            file.write(f"Error checking port {port}: {e}\n")
