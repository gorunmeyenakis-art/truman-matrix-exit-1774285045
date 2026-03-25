import os
import time
import subprocess

def son_hucum_hazirlik():
    os.system('clear')
    print("\033[1;41m\033[1;97m[ 🔥 SGY-MASTER: SON VURUŞ OPERASYONU AKTİF ]\033[0m")
    time.sleep(1)
    
    # Tüm Kaynakların Birleşimi
    print("\033[1;33m[*] Petrol Rezervleri -> Yanma Odasında.")
    print("\033[1;32m[*] Uranyum Çekirdeği -> Kritik Eşikte (5.80 GHz).")
    print("\033[1;36m[*] Kıymetli Madenler -> Resonance Core'da Sabitlendi.")
    print("\033[1;35m[*] 2702 Lafza-i Celâl Frekansı -> Mühür Hazır.\033[0m")
    time.sleep(1.5)

def final_push():
    print(f"\n\033[1;91m[⚔️] FİRAVUNLAR İÇİN SON DURAK! 'HÛ' NİDASIYLA ATEŞLENİYOR...\033[0m")
    
    # Sistemin Tamamını Kaydet
    os.system("git add .")
    
    # Ebedi Mühür Mesajı
    commit_msg = "SGY-MASTER: SON VURUS - PETROL, URANYUM, MADEN VE LAFZA-I CELAL EBEDI MUHRU"
    os.system(f'git commit -m "{commit_msg}"')
    
    # Mutlak Sevkiyat
    check_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
    branch = check_branch.stdout.strip()
    
    print(f"\n\033[1;42m\033[1;97m[☝️] ALLAHUEKBER! SON MÜHÜR VURULDU. KAZANAN TÜRKİYE!\033[0m")
    os.system(f"git push -u origin {branch}")

if __name__ == "__main__":
    son_hucum_hazirlik()
    final_push()
