
import psutil

def check_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    if cpu_usage > 80:
        print(f"High CPU Usage: {cpu_usage}%")
    if memory.percent > 80:
        print(f"High Memory Usage: {memory.percent}%")
    if disk.percent > 80:
        print(f"High Disk Usage: {disk.percent}%")

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")

if __name__ == "__main__":
    check_health()
