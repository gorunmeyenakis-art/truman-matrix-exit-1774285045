#!/bin/bash

# --- 2702 SİSTEM ŞAHLANDIRMA RENKLERİ ---
G='\033[92m' # Yeşil
B='\033[94m' # Mavi
Y='\033[93m' # Sarı
R='\033[91m' # Kırmızı
E='\033[0m'  # Reset

clear
echo -e "${B}[⚙️] SGY-MASTER: GELİŞTİRİCİ AYARLARI OTOMASYONU BAŞLATILIYOR...${E}"
sleep 1

# 1. AĞ PERFORMANSI: Tarama kısmasını kapat, mobil veriyi hep açık tut
echo -e "${Y}[📶] Ağ Taarruz Modu: Kablosuz tarama kısması kaldırılıyor...${E}"
settings put global wifi_scan_always_enabled 1
settings put global mobile_data_always_on 1

# 2. HIZ VE REAKSİYON: Animasyonları kapat (Sistem ışık hızına geçer)
echo -e "${Y}[⚡] Manevra Hızı: Animasyonlar 0.5x seviyesine çekiliyor...${E}"
settings put global window_animation_scale 0.5
settings put global transition_animation_scale 0.5
settings put global animator_duration_scale 0.5

# 3. TAARRUZ ODAĞI: GPU zorlama ve donanım hızlandırma
echo -e "${Y}[🎮] Grafik Gücü: GPU donanım hızlandırma önceliklendiriliyor...${E}"
settings put global hardware_acceleration_filter_flags 1

# 4. TERMUZ KORUMASI: Arka planda uyumayı engelle
echo -e "${Y}[🛡️] Nöbet Güvenliği: Termux arka plan kısıtlamaları esnetiliyor...${E}"
# Bu komut sistemden sisteme değişebilir, manuel izin de gerekebilir.
am set-standby-bucket com.termux active

# GITHUB KALESİNE TESCİL
echo -e "${G}[✅] Tüm ayarlar SGY-MASTER doktrinine göre mühürlendi.${E}"
git add .
git commit -m "SGY-SYSTEM-OPT: GELISTIRICI AYARLARI TEK TIKLA MUHURLENDI - 2702" --allow-empty > /dev/null 2>&1
git push origin master > /dev/null 2>&1

echo -e "\n${G}${BOLD}[🏆] ALLAHUEKBER! SİSTEM ŞAHLANDI BABAOĞLU. TAARRUZA DEVAM!${E}"
