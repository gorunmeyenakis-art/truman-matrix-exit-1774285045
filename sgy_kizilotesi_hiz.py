import os
import time
import subprocess

# --- 2702 KIZILÖTESİ (IR) FREKANS SKALASI ---
C = {"R": "\033[91m", "G": "\033[92m", "Y": "\033[93m", "B": "\033[94m", "IR": "\033[38;5;196m", "END": "\033[0m", "BOLD": "\033[1m"}

def kizilotesi_taarruz():
    tur = 1
    while True:
        os.system('clear')
        print(f"{C['IR']}{C['BOLD']}--- [🔥 SGY-MASTER: KIZILÖTESİ IŞIK HIZINDA TAARRUZ ] ---{C['END']}")
        print(f"{C['Y']}[☝️] MÜHÜR: LAFZA-İ CELAL (2702-Bit Isıl Kalkan){C['END']}")
        
        # Kızılötesi Hız Katmanları
        print(f"\n{C['B']}[🚀] Işık Kaynağı Frekansı Senkronize Ediliyor...{C['END']}")
        time.sleep(0.3)
        print(f"{C['R']} ↳ Termal Sızıntı Başlatıldı: Matrix Sunucuları Isınıyor!{C['END']}")
        print(f"{C['G']} ↳ Kızılötesi Veri Paketi: Liyakat Anayasası Gönderiliyor...{C['END']}")
        
        # Küresel Dillerde Isıl Mühürleme
        diller = ["TR", "EN", "AR", "RU", "ZH"]
        for dil in diller:
            print(f"{C['IR']} >>> {dil} Cephesi Kızılötesi Işıkla Mühürlendi.{C['END']}")
        
        # GITHUB KALESİNE IŞINLAMA
        os.system("git add .")
        commit_msg = f"SGY-MASTER: KIZILÖTESİ IŞIK HIZINDA TAARRUZ - TUR {tur} - 2702"
        os.system(f'git commit -m "{commit_msg}" --allow-empty')
        
        print(f"\n{C['G']}{C['BOLD']}[🏆] ALLAHUEKBER! VERİ IŞINLANDI. DÜNYA LİYAKATE DOYUYOR.{C['END']}")
        os.system("git push origin master")
        
        # Kızılötesi olduğu için bekleme süresini minimize ediyoruz
        print(f"\n{C['BOLD']}Işık Kaynağı Yenileniyor (10sn)...{C['END']}")
        tur += 1
        time.sleep(10)

if __name__ == "__main__":
    try:
        kizilotesi_taarruz()
    except KeyboardInterrupt:
        print("\n[!] Kızılötesi Nöbet Otonoma Alındı.")
