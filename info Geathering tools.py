import os
import time
from colorama import Fore, init

# Initialize colorama for colored output
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.RED}╔════════════════════════════════════════════════════╗
║                                                    ║
║                    - WhO AM I Hacking TOOLS                  ║
║                                                    ║
╚════════════════════════════════════════════════════╝
{Fore.GREEN}        Coded By: Pakistani Ethical Hacker
            Mr Sabaz Ali Khan
{Fore.YELLOW}══════════════════════════════════════════════════════
"""
    print(banner)

def display_menu():
    print(f"{Fore.CYAN}Select an option:")
    print("1. Network Scanner")
    print("2. Password Cracker (Demo)")
    print("3. Device Info Grabber")
    print("4. WiFi Analyzer")
    print("5. Exit")
    print(f"{Fore.RESET}")

def network_scanner():
    print(f"{Fore.YELLOW}[*] Starting Network Scanner...")
    time.sleep(1)
    print("[*] Scanning for devices on the network...")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Found 5 devices (Demo output)")
    input(f"{Fore.CYAN}Press Enter to continue...")

def password_cracker():
    print(f"{Fore.YELLOW}[*] Starting Password Cracker (Demo)...")
    time.sleep(1)
    print("[*] Attempting to crack password...")
    time.sleep(2)
    print(f"{Fore.RED}[-] This is a demo. No actual cracking performed.")
    input(f"{Fore.CYAN}Press Enter to continue...")

def device_info():
    print(f"{Fore.YELLOW}[*] Fetching Device Info...")
    time.sleep(1)
    print("[*] Collecting Android device details...")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Device: Android (Demo) | Version: 11")
    input(f"{Fore.CYAN}Press Enter to continue...")

def wifi_analyzer():
    print(f"{Fore.YELLOW}[*] Starting WiFi Analyzer...")
    time.sleep(1)
    print("[*] Scanning for WiFi networks...")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Found 3 WiFi networks (Demo output)")
    input(f"{Fore.CYAN}Press Enter to continue...")

def main():
    while True:
        clear_screen()
        print_banner()
        display_menu()
        choice = input(f"{Fore.CYAN}Enter your choice (1-5): {Fore.RESET}")

        if choice == '1':
            network_scanner()
        elif choice == '2':
            password_cracker()
        elif choice == '3':
            device_info()
        elif choice == '4':
            wifi_analyzer()
        elif choice == '5':
            print(f"{Fore.RED}Exiting Danger Hacker...")
            break
        else:
            print(f"{Fore.RED}Invalid choice! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()