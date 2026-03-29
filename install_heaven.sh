#!/data/data/com.termux/files/usr/bin/bash
echo "SGY-Cennet Kuruluyor..."
pkg update && pkg upgrade -y
pkg install python git termux-api -y
pip install numpy requests geopy rich gps3
echo "Sistem Hazır. 'python cennet.py' ile evreni başlat."
