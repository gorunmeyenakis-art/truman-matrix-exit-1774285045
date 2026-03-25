import os
import time
import subprocess

# --- 2702 FREKANS VE MANEVİ REZONANS ---
def sirri_kodla():
    os.system('clear')
    print("\033[1;35m[☝️] SGY-MASTER: İSM-İ AZAM VE 'HÛ' PROTOKOLÜ AKTİF EDİLİYOR...\033[0m")
    time.sleep(1)
    
    adimlar = [
        "2702 Lafza-i Celâl Frekansı Tarandı...",
        "Petrol, Uranyum ve Maden Rezervleri Tek Noktada Sıkıştırıldı (Hû)...",
        "Matrix Sızıntıları 'Allah' İsmiyle Buharlaştırıldı...",
        "Ilgaz Efe Yıldız İçin Ebedi Mühür Vuruldu."
    ]
    
    for adim in adimlar:
        print(f"\033[1;92m[✅] {adim}\033[0m")
        time.sleep(0.8)

def ucur_ve_muhurle():
    print("\n\033[1;41m\033[1;97m[🚀] 'HÛ' NEFESİYLE GITHUB KALESİNE TAARRUZ! [🚀]\033[0m")
    
    # Tüm sistemi ve 'Sırrı' ekle
    os.system("git add .")
    
    # En Kritik Mühür Mesajı
    commit_msg = "SGY-MASTER: 100. SIR (ISM-I AZAM) VE 2702 FREKANSI ILE EBEDI MUHUR - HUVE"
    os.system(f'git commit -m "{commit_msg}"')
    
    # 2702-Bit Manevi Güçle Push
    check_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
    branch = check_branch.stdout.strip()
    
    print(f"\n\033[1;33m[🛰️] Sinyal Kalınlaştırılıyor (Saygı Göstergesi)... {branch} Hattı Açıldı.\033[0m")
    
    if os.system(f"git push -u origin {branch}") == 0:
        print("\n\033[1;42m\033[1;97m[🏆] ALLAHU EKBER! SIR MUHURLENDI. KAZANAN LIYAKAT!\033[0m")
    else:
        print("\n\033[1;91m[⚠️] MATRİX DİRENİYOR! AMA HAKİKAT KARŞISINDA DURAMAZLAR.\033[0m")

if __name__ == "__main__":
    sirri_kodla()
    ucur_ve_muhurle()
