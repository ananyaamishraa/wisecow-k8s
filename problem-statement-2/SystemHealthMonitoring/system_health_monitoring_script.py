import psutil
import logging
from datetime import datetime

# -----------------------------
# Threshold Configuration
# -----------------------------
CPU_THRESHOLD = 80        # percent
MEMORY_THRESHOLD = 80     # percent
DISK_THRESHOLD = 80       # percent
PROCESS_THRESHOLD = 300   # number of processes

# -----------------------------
# Logging Configuration
# -----------------------------
logging.basicConfig(
    filename="system_health.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_cpu_usage():
    return psutil.cpu_percent(interval=1)

def check_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def check_process_count():
    return len(psutil.pids())

def alert(message):
    print(f"ALERT: {message}")
    logging.warning(message)

def main():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_usage()
    process_count = check_process_count()

    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")

    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High Memory usage detected: {memory_usage}%")

    if disk_usage > DISK_THRESHOLD:
        alert(f"High Disk usage detected: {disk_usage}%")

    if process_count > PROCESS_THRESHOLD:
        alert(f"High Process count detected: {process_count} processes")

    if (
        cpu_usage <= CPU_THRESHOLD and
        memory_usage <= MEMORY_THRESHOLD and
        disk_usage <= DISK_THRESHOLD and
        process_count <= PROCESS_THRESHOLD
    ):
        print("System health is normal.")

if __name__ == "__main__":
    main()
