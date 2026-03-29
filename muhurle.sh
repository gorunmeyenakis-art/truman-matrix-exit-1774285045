#!/bin/bash
# SGY-MİRAS v15.1 - Otomatik Yedekleme Sistemi
clear
echo "========================================"
echo "   🛡️  SGY-MİRAS: BULUT MÜHÜRLEME"
echo "      HEDEF: Gorunmeyenakis-art"
echo "========================================"

# Dosyaları topla
cp ~/sgy.py ~/SGY-LAB/
cp ~/sgy_master.db ~/SGY-LAB/
# Varsa diğer modülleri de buraya ekleyebiliriz

cd ~/SGY-LAB
git add .
git commit -m "SGY Sistem Mührü: $(date +'%Y-%m-%d %H:%M:%S')"
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "\n✅ Veriler Evrene (GitHub) Mühürlendi."
else
    echo -e "\n❌ Hata: Bağlantı Sağlanamadı. Token Kontrol Et!"
fi
