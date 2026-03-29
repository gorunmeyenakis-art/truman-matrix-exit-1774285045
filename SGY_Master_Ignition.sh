#!/data/data/com.termux/files/usr/bin/bash

# Renkler (Işık Hızı Teması)
WHITE='\033[1;37m'
GOLD='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[0;36m'
NC='\033[0m'

clear
echo -e "${WHITE}🕊️  İYİ CİN KANATLANDI, IŞIK HIZIYLA GELDİ...${NC}"
echo -e "${GOLD}--------------------------------------------------${NC}"
echo -e "${GOLD}     SGY-UNIVERSAL & RZN-CORE: MELEK KORUMASI      ${NC}"
echo -e "${GOLD}--------------------------------------------------${NC}"

# Hız Optimizasyonu (Arka planda gereksiz yükleri temizle)
echo -e "${BLUE}[*] Işık Hızı Modülü Aktif: Bellek Temizleniyor...${NC}"
sync 2>/dev/null || true

# SGY ve RZN Çekirdeklerini Ateşle
if [ -f ~/SGY_MASTER/SGY-CORE/main.py ]; then
    python ~/SGY_MASTER/SGY-CORE/main.py
fi

if [ -f ~/SGY_MASTER/RZN-CORE/rzn_engine.py ]; then
    python ~/SGY_MASTER/RZN-CORE/rzn_engine.py
fi

echo -e "${CYAN}[!] Sistem Işık Hızında Stabil. Dileğin Emrimdir Babaoğlu.${NC}"
echo -e "${GOLD}--------------------------------------------------${NC}"
