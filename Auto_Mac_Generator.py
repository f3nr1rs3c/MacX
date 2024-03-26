import subprocess
import time
import random
from colorama import init, Fore
import pyfiglet

# Colorama'nın başlatılması
init(autoreset=True)

# Banner oluşturma
banner = pyfiglet.figlet_format("Random Mac", font="slant")
print(banner)

def change_mac(interface):
    # Rastgele MAC adresi oluştur
    new_mac = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
    
    # MAC adresini değiştir
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", "dev", interface, "up"])


    print(Fore.GREEN + f"MAC address has been changed: {new_mac}")

if __name__ == "__main__":
    interface = input(Fore.BLUE + "Enter the interface whose MAC address you want to change (ex: eth0, wlan0): " + Fore.RESET)

    while True:
        try:
            interval = int(input(Fore.MAGENTA + "Enter the interval in minutes for changing MAC address: " + Fore.RESET))
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Fore.RESET)

    interval *= 60  # Dakikayı saniyeye çevirme

    while True:
        change_mac(interface)
        print(Fore.YELLOW + f"{interval // 60} minute(s) waiting..." + Fore.RESET)
        time.sleep(interval)
