import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(f"Disk free: {free:.2f}%")   # <-- added
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(3)
    print(f"CPU usage: {usage:.2f}%")  # <-- added
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("CPU USAGE TOO HIGH")
else:
    print("Everything is OK!")
