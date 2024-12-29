import platform
import os
import psutil
import time
from colorama import Fore, Style, init

init()

def get_os_info():
    """Get operating system information."""
    return f"{platform.system()} {platform.release()} ({platform.version()})"

def get_kernel_info():
    """Get kernel information."""
    return platform.release()

def get_uptime():
    """Get system uptime."""
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = int(current_time - boot_time)
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m"

def get_cpu_info():
    """Get CPU information."""
    cpu = platform.processor()
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    return f"{cpu} ({cores} cores, {threads} threads)"

def get_memory_info():
    """Get memory usage information."""
    mem = psutil.virtual_memory()
    total = mem.total // (1024 ** 2)
    used = mem.used // (1024 ** 2)
    return f"{used} MiB / {total} MiB"

def get_disk_info():
    """Get disk usage information."""
    disk = psutil.disk_usage('/')
    total = disk.total // (1024 ** 3)
    used = disk.used // (1024 ** 3)
    return f"{used} GiB / {total} GiB"

def get_user_info():
    """Get current user and hostname."""
    user = os.getlogin()
    hostname = platform.node()
    return f"{user}@{hostname}"

def display_neofetch():
    """Display system information in a styled format."""
    print(f"{Fore.CYAN}{get_user_info()}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}OS:{Style.RESET_ALL} {get_os_info()}")
    print(f"{Fore.GREEN}Kernel:{Style.RESET_ALL} {get_kernel_info()}")
    print(f"{Fore.GREEN}Uptime:{Style.RESET_ALL} {get_uptime()}")
    print(f"{Fore.GREEN}CPU:{Style.RESET_ALL} {get_cpu_info()}")
    print(f"{Fore.GREEN}Memory:{Style.RESET_ALL} {get_memory_info()}")
    print(f"{Fore.GREEN}Disk:{Style.RESET_ALL} {get_disk_info()}")

if __name__ == "__main__":
    display_neofetch()
