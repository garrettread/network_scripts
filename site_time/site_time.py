import requests
import time

urls = ["https://ger512.com", "https://google.com", "https://github.com", "https://cloudflare.com"]

with open("response_times.txt", "w") as file:
    for url in urls:
        try:
            start = time.time()
            requests.get(url)
            end = time.time()

            elapsed = (end - start) * 1000  # convert to milliseconds

            if elapsed > 500:
                file.write(f"{url} took {elapsed:.2f} ms - WARNING: Slow response!\n")
            else:
                file.write(f"{url} took {elapsed:.2f} ms - OK\n")

        except Exception as e:
            file.write(f"{url} could not be reached. Error: {e}\n")
