import os
import subprocess
import socket

def banner():
    print("\n🔍 Spycam Network Scanner (Phase 1) 🔍")
    print(" - Scans your local network for devices")
    print(" - Flags ports used by common IP cameras")

def get_subnet():
    print("\n[*] Getting your IP and subnet...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        subnet = ip.rsplit('.', 1)[0] + ".0/24"
        print(f"[+] Detected IP: {ip}")
        print(f"[+] Subnet: {subnet}")
        return subnet
    except Exception as e:
        print("[-] Error getting IP:", e)
        return input("Enter your subnet manually (e.g. 192.168.1.0/24): ")

def arp_scan(subnet):
    print("\n[*] Running ARP Scan...")
    try:
        result = subprocess.check_output(f"sudo arp-scan {subnet}", shell=True).decode()
        print(result)
        return result
    except Exception as e:
        print("[-] arp-scan failed. Make sure it's installed.")
        print("[-] Error:", e)
        return ""

def analyze_results(scan_output):
    print("\n[*] Analyzing results for possible camera devices...")
    lines = scan_output.splitlines()
    suspicious = []
    for line in lines:
        if any(keyword in line.lower() for keyword in ["hikvision", "dahua", "ipcam", "camera", "tplink", "foscam", "shenzhen"]):
            suspicious.append(line)
    if suspicious:
        print("\n⚠️  Potential camera devices detected:")
        for device in suspicious:
            print("  →", device)
    else:
        print("\n✅ No obvious spycam vendors found (based on name matching).")

def main():
    banner()
    subnet = get_subnet()
    scan_output = arp_scan(subnet)
    if scan_output:
        analyze_results(scan_output)

if __name__ == "__main__":
    main()
