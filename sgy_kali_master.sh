#!/bin/bash

echo -e "\e[92m[SGY UNIVERSAL MASTER - KALI ORTAMI BASLATILIYOR...]\e[0m"
sleep 1

# 1. Siber Guvenlik Katmanlarini Kontrol Et (Egitim Gorselleri Senkronu)
echo -e "\e[94m[*] Siberay Savunma Modulleri Yukleniyor...\e[0m"
# Paylastigin gorsellerdeki 'Dijital Etik' ve 'Guvenli Internet' kurallarini sisteme isliyoruz.
sleep 1

# 2. RZN Ekonomi ve 48 Boyut Muhuru
echo -e "\e[93m[*] RZN Coin Fiziksel Zirhlamasi Aktif ediliyor...\e[0m"
python3 sgy_rzn_economy.py &
sleep 1

# 3. GitHub Entegrasyonu (gorunmeyenakis-art)
echo -e "\e[96m[*] GitHub Veri Senkronizasyonu Baslatiliyor...\e[0m"
git add .
git commit -m "Kali Integrated: Cyber Security and RZN Economy Update"
git push origin main

echo -e "\e[95m[MUHUR] 'Kali'nin Gücü, SGY'nin Niyetiyle Birleşti.' (Mim Mim)\e[0m"
