import os
import time
import psutil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def monitor_cli():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        disk_usage = psutil.disk_usage("/")
        disk_percent = disk_usage.percent

        print(f"CPU: {cpu_percent}%")
        print(f"Memory: {get_size(memory.used)} / {get_size(memory.total)} ({memory_percent}%)")
        print(f"Disk: {get_size(disk_usage.used)} / {get_size(disk_usage.total)} ({disk_percent}%)")

        time.sleep(1)
        os.system("clear")

if __name__ == "__main__":
    monitor_cli()