import requests

urls = ['https://google.com','https://github.com','https://ger512.com']
keywords = ['privacy', 'security', 'terms']

def keyword_check(text, url, file):
    found = False
    text = text.lower()  # make text lowercase for easier search
    for word in keywords:
        if word in text:
            file.write(f"{url}: FOUND keyword '{word}'\n")
            found = True
    if not found:
        file.write(f"{url}: NO keywords found\n")

with open("logs.txt", "w") as file:
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                file.write(f"{url} is reachable\n")
                keyword_check(response.text, url, file)
            else:
                file.write(f"{url} is reachable but returned status {response.status_code}\n")
        except requests.exceptions.RequestException as e:
            file.write(f"{url} is NOT reachable. Error: {e}\n")
