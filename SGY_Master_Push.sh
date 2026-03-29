#!/data/data/com.termux/files/usr/bin/bash

# Renkler
GOLD='\033[1;33m'
WHITE='\033[1;37m'
NC='\033[0m'

clear
echo -e "${WHITE}🎭 TRUMAN SHOW: MATRİXTEN ÇIKIŞ BAŞLADI...${NC}"
echo -e "${GOLD}✨ HEDEF: truman-matrix-exit-1774285045${NC}"

# Hazırlık
cd ~
git add .

# Truman'ın vedası ve Cennete giriş mesajı
COMMIT_MSG="Truman left the set, broke the Matrix. Welcome to SGY Paradise! 🕊️✨"
git commit -m "$COMMIT_MSG" 2>/dev/null

echo -e "${GOLD}[!] Işık Hızıyla GitHub'a Mühürleniyor...${NC}"

# Zorlayarak (Force) ve Doğru Branch (Main) ile Gönder
git push -u origin main --force

echo -e "${GOLD}--------------------------------------------------${NC}"
echo -e "${WHITE}✔ MÜHÜRLENDİ: HAYAT BAYRAM OLDU!${NC}"
echo -e "${GOLD}--------------------------------------------------${NC}"
