import os
import time
import subprocess

# --- 2702 KOZMİK VE SİBER HARP SKALASI ---
C = {"R": "\033[91m", "G": "\033[92m", "B": "\033[94m", "Y": "\033[93m", "C": "\033[96m", "END": "\033[0m", "BOLD": "\033[1m"}

def kuresel_algoritma_tetikleyici():
    tur = 1
    while True:
        os.system('clear')
        print(f"{C['R']}{C['BOLD']}[🚀 SGY-MASTER: KÜRESEL HARP OPERASYONU - TUR {tur} ]{C['END']}")
        print(f"{C['Y']}[☝️] MÜHÜR: LAFZA-İ CELAL (2702-Bit Manevi Kalkan){C['END']}")
        
        # Sosyal Medya Algoritma Sızması
        platformlar = ["X (Twitter) - Trend Topic Modu", "Instagram - Keşfet Entegrasyonu", "Facebook - Global Feed", "TikTok - Viral Liyakat"]
        
        for p in platformlar:
            print(f"{C['B']}[🛰️] {p} Algoritması 2702 Frekansına Ayarlanıyor...{C['END']}")
            time.sleep(0.5)

        # Gök Kaşifi ve Kaynak Yönetimi
        print(f"\n{C['C']}[🔍] KOZMIC REZONANS: Azimut 332,6° | Petrol ve Uranyum Aktif!{C['END']}")
        
        # Git Operasyonu (Dünyaya Mühür Çivileme)
        os.system("git add .")
        msg = f"SGY-GLOBAL-CIHAD: HEDEF 2702 - TUR {tur} - BIZ SIZIZ SIZ BIZ!"
        os.system(f'git commit -m "{msg}" --allow-empty')
        
        print(f"\n{C['G']}[✅] 2702. Zafer Mührü Sosyal Medya Kanallarına Fırlatıldı!{C['END']}")
        os.system("git push origin master")
        
        print(f"\n{C['BOLD']}Sistem Bir Sonraki Küresel Dalga İçin Hazırlanıyor (30sn)...{C['END']}")
        tur += 1
        time.sleep(30)

if __name__ == "__main__":
    try:
        kuresel_algoritma_tetikleyici()
    except KeyboardInterrupt:
        print("\n[!] Cihad Otonom Nöbete Alındı.")
