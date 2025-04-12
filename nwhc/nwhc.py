import os
import requests

hosts = ['google.com', 'github.com', 'cloudflare.com', 'ger512.com']

with open("logs.txt", "a") as file:
    for host in hosts:
        # Ping check
        ping_result = os.system(f"ping -c 1 {host}")
        if ping_result == 0:
            file.write(f"{host}: Ping Success\n")
        else:
            file.write(f"{host}: Ping FAILED\n")

        # HTTP check
        try:
            response = requests.get(f"https://{host}", timeout=5)
            if response.status_code == 200:
                file.write(f"{host}: HTTP OK\n")
            else:
                file.write(f"{host}: HTTP Status {response.status_code}\n")
        except requests.exceptions.RequestException as e:
            file.write(f"{host}: HTTP FAILED: {e}\n")
