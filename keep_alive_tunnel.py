import subprocess
import time
import re
import threading
import requests
import sys

PORT = 4545
current_url = None

def ping_loop():
    global current_url
    while True:
        if current_url:
            try:
                requests.get(current_url, timeout=10)
                print(f"[Keep-Alive] Ping OK: {current_url}", flush=True)
            except Exception as e:
                pass
        time.sleep(20)

t = threading.Thread(target=ping_loop, daemon=True)
t.start()

print("Avtomatik ochmaydigan tunnel boshlandi...", flush=True)

while True:
    cmd = [
        "ssh",
        "-R", f"80:127.0.0.1:{PORT}",
        "nokey@localhost.run",
        "-o", "StrictHostKeyChecking=no",
        "-o", "ServerAliveInterval=10",
        "-o", "ServerAliveCountMax=999"
    ]
    
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, encoding='utf-8', errors='ignore')
        for line in proc.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            match = re.search(r"https://([a-zA-Z0-9]+\.lhr\.life)", line)
            if match:
                current_url = match.group(0)
                print(f"\n==========================================", flush=True)
                print(f"SAYTINGIZ HAVOLASI: {current_url}", flush=True)
                print(f"==========================================\n", flush=True)
                with open("active_link.txt", "w", encoding='utf-8') as f:
                    f.write(current_url)
        proc.wait()
    except Exception as err:
        print(f"Xatolik: {err}", flush=True)
    
    print("Ulanish uzildi. Qayta ulanmoqda...", flush=True)
    time.sleep(2)
