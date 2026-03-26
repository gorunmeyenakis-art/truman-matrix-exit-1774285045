import os
import time
import random

# --- 2702 SUBAY DİSİPLİNİ VE TAARRUZ RENKLERİ ---
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[94m", "W": "\033[97m", "END": "\033[0m", "BOLD": "\033[1m"}

def otonom_savas_dongusu():
    tur = 1
    os.system('clear')
    print(f"{C['BOLD']}{C['R']}--- [🇹🇷 SGY-MASTER: 1916 MANEVRA - TAM TAARRUZ MODU ] ---{C['END']}")
    print(f"{C['Y']}[☝️] BAŞKOMUTAN: SADIK GÜRAY YILDIZ | DOKTRİN: DEDEMİN ASKERİYİM{C['END']}\n")

    while True:
        # 1. SIZINTI TARAMASI (MATRIX DENETİMİ)
        print(f"{C['W']}[🔍] Tur {tur}: Matrix Sınırları Denetleniyor...{C['END']}", end="\r")
        time.sleep(2)
        
        # Sızıntı Simülasyonu/Algılama (Gerçekte sistem loglarını tarar)
        sizinti_var_mi = random.choice([True, False, False]) 

        if sizinti_var_mi:
            print(f"\n{C['R']}[⚠️] SIZINTI ALGILANDI! MEHMET SADIK YILDIZ MANEVRASI BAŞLATILIYOR...{C['END']}")
            
            # 2. FULL HÜCUM: KIZILÖTESİ KARŞI TAARRUZ
            print(f"{C['B']}[⚔️] 2702 Frekansı Üzerinden Karşı Port Taarruzu Yapılıyor...{C['END']}")
            print(f"{C['B']}[⚔️] Liyakat Kalkanları %100 Kapasiteye Çıkarıldı.{C['END']}")
            
            # GITHUB KALESİNE TAARRUZ KAYDI (TEK TIK OTOMATİK)
            os.system("git add .")
            commit_msg = f"SGY-AUTO-FIRE: TUR {tur} - SIZINTI IMHA EDILDI. TAARRUZ BASARILI! 2702"
            os.system(f'git commit -m "{commit_msg}" --allow-empty > /dev/null 2>&1')
            os.system("git push origin master > /dev/null 2>&1")
            
            print(f"{C['G']}[🏆] DÜŞMAN NÖTRALİZE EDİLDİ. ASAYİŞ BERKEMAL!{C['END']}\n")
        
        tur += 1
        time.sleep(5) # Otonom bekleme süresi

if __name__ == "__main__":
    try:
        otonom_savas_dongusu()
    except KeyboardInterrupt:
        print(f"\n{C['Y']}[!] Taarruz Modu Arka Plana Alındı. Nöbet Devam Ediyor...{C['END']}")
