import threading
import queue
import requests
import time
q = queue.Queue()
valid_proxies = []
proxynew = ""

with open("proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    global proxynew
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json",proxies={"http": proxy, "https": proxy})
        except:
            continue
    if res.status_code == 200:
        proxynew += proxy + "\n"
        print(proxy)



for _ in range(10):
    threading.Thread(target=check_proxies).start()

while q.empty() != False:
    print("Added All To Proxies")
    with open("proxy_list.txt", "w") as f:
        f.write(proxynew)
    time.sleep(10)