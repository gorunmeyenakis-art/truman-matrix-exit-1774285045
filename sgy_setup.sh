#!/data/data/com.termux/files/usr/bin/bash

echo "--- SGY-Tavizsiz Protokol Başlatılıyor ---"

# 1. Depoları Güncelle ve Temel Araçları Kur
pkg update -y && pkg upgrade -y
pkg install clang python python-pip fftw make ninja libandroid-execve -y

# 2. Termux-User-Repository (TUR) Etkinleştir (Numpy/Scipy için kritik)
pkg install tur-repo -y

# 3. Pip Hatalarını Aşmak İçin Önceden Derlenmiş Paketleri Kur
echo "Numpy ve Scipy optimize ediliyor..."
pkg install python-numpy python-scipy -y

# 4. Gereksinim Listesini Temiz Kur
if [ -f "requirements.txt" ]; then
    echo "Gereksinimler yükleniyor..."
    # Numpy ve Scipy zaten pkg ile kurulduğundan onları listeden geçici olarak çıkaralım ki hata vermesin
    grep -vE 'numpy|scipy' requirements.txt > temp_req.txt
    pip install --no-cache-dir -r temp_req.txt
    rm temp_req.txt
fi

echo "--- Entegrasyon Tamamlandı. Sistem Hazır! ---"
