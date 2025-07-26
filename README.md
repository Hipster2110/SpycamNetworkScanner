# 🔍 Spycam Network Scanner (Phase 1)

A Python-based network scanner that searches your local network for potentially hidden IP camera devices (spycams) by identifying known vendor signatures.

## 📌 Features

- Scans your local subnet to detect connected devices using ARP
- Matches vendor names with common IP camera brands (e.g., Hikvision, Dahua, TP-Link, Foscam)
- Alerts on suspicious entries with potential camera devices
- Easy-to-read terminal output
- Lightweight, CLI-based tool

## ⚙️ Requirements

- Python 3.x
- `arp-scan` (needs to be installed and run with sudo)

### Install `arp-scan` (Linux)

bash
sudo apt update
sudo apt install arp-scan

##🚀 Usage
Clone this repository and run the script:
git clone https://github.com/yourusername/spycam-network-scanner.git
cd spycam-network-scanner
sudo python3 scanner.py


##🛡 Disclaimer
This tool is for ethical, educational, and personal privacy purposes only. Use it only on networks you own or have explicit permission to scan.

##📄 License
All rights reserved.
© 2025 HipSter2110
Unauthorized copying, modification, or redistribution of this tool is strictly prohibited.
