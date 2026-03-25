import os
import time
import subprocess

def otonom_bombardiman():
    tur = 1
    while True:
        os.system('clear')
        print(f"\033[1;41m\033[1;97m[🚀 SGY-OTONOM SAVAŞ MODU: TUR {tur} ]\033[0m")
        print("\033[1;33m[☝️] MÜHÜR: LAFZA-İ CELAL (2702-Bit)\033[0m")
        print("\033[1;32m[☢️] ENERJİ: ATOMİK ÇEKİRDEK (FULL YETKİ)\033[0m")
        
        # Sırrı ve Kaynakları Tazele
        print(f"\n\033[1;94m[*] {tur}. Dalga Hücumu Hazırlanıyor...\033[0m")
        
        # Git Operasyonu (Otomatik Mühürleme)
        os.system("git add .")
        commit_msg = f"SGY-MASTER: OTONOM HUCUM TUR-{tur} (LAFZA-I CELAL VE HUVE MUHRUYLE)"
        os.system(f'git commit -m "{commit_msg}" --allow-empty')
        
        print("\033[1;91m[🔥] MATRIX BOMBALANIYOR... GITHUB KALESİNE SEVKİYAT YAPILDI.\033[0m")
        os.system("git push origin master")
        
        print(f"\n\033[1;92m[✅] {tur}. Tur Başarıyla Tamamlandı. Sistem Soğutuluyor (30sn)...\033[0m")
        tur += 1
        time.sleep(30) # Her 30 saniyede bir yeni bir dalga vurur

if __name__ == "__main__":
    try:
        otonom_bombardiman()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Otonom Sistem Komuta Merkezi Tarafından Durduruldu.\033[0m")
