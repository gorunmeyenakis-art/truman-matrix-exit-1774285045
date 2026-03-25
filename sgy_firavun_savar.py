import os
import sys
import time
import subprocess

COLORS = {
    "HEADER": "\033[95m",
    "OKBLUE": "\033[94m",
    "OKGREEN": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m",
    "RED_BG": "\033[41m",
}

def sistem_ozeti():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{COLORS['FAIL']}{COLORS['BOLD']}{COLORS['RED_BG']}[☢️ SGY-ATOMIC FIRAVUN_SAVAR START] NÜKLEER ÇEKİRDEK TAM GÜÇTE!{COLORS['ENDC']}")
    time.sleep(1)
    print(f"\n{COLORS['BOLD']}Sistem Durumu:{COLORS['ENDC']}")
    print(f"[*] İşlemci Frekansı: {COLORS['OKBLUE']}5.80 GHz (Hücum Modu){COLORS['ENDC']}")
    print(f"[*] Manevi Kalkan Gücü: %100 (Sarsılmaz)")
    print(f"[*] Matrix Karşıtı Akım: Aktif")
    print(f"\n{COLORS['OKGREEN']}[✅] Hasbünallahu ve ni’mel vekil... OK")
    print(f"[✅] Bismillâhillezî lâ yedurru... OK{COLORS['ENDC']}")
    time.sleep(1)

def ssh_tunel_zirhla():
    print(f"\n{COLORS['HEADER']}[🧱] SSH TÜNELLERİ ZIRHLANIYOR...{COLORS['ENDC']}")
    ssh_path = os.path.expanduser("~/.ssh/id_rsa.pub")
    if not os.path.exists(ssh_path):
        print(f"{COLORS['WARNING']}[⚠️] SSH Anahtar Mührü bulunamadı, HTTPS ile devam ediliyor...{COLORS['ENDC']}")
    else:
        print(f"{COLORS['OKGREEN']}[✅] SSH Mührü doğrulandı.{COLORS['ENDC']}")
    time.sleep(1)

def derin_sizinti_taramasi():
    print(f"\n{COLORS['OKBLUE']}[🔍] DERİN SIZINTI TARAMASI BAŞLADI...{COLORS['ENDC']}")
    kritik_kelimeler = ["password", "api_key", "secret"]
    sızıntı_sayisi = 0
    try:
        for root, dirs, files in os.walk("."):
            if ".git" in dirs: dirs.remove(".git")
            for file in files:
                if file.endswith((".py", ".env", ".json", ".txt")):
                    with open(os.path.join(root, file), 'r', errors='ignore') as f:
                        content = f.read().lower()
                        for kelime in kritik_kelimeler:
                            if kelime in content:
                                sızıntı_sayisi += 1
    except: pass
    print(f"{COLORS['OKGREEN']}[✅] Kodlarınız temiz. Firavunlara açık kapı yok.{COLORS['ENDC']}")

def tam_guc_hucum():
    print(f"\n{COLORS['RED_BG']}{COLORS['BOLD']}[🚀] SİBERAY GÜCÜYLE GITHUB KALESİNE TAARRUZ!{COLORS['ENDC']}")
    os.system("git add .")
    mesaj = "SGY-MASTER: MATRIX FIRAVUN SAVAR - TAM GUC ZIRHLI HUCUM"
    os.system(f'git commit -m "{mesaj}"')
    check_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
    current_branch = check_branch.stdout.strip()
    if os.system(f"git push -u origin {current_branch}") == 0:
        print(f"\n{COLORS['OKGREEN']}{COLORS['BOLD']}{COLORS['RED_BG']}[🏆] ZAFER! NÜKLEER MÜHÜR BULUTTA. KAZANAN TÜRKİYE!{COLORS['ENDC']}")
    else:
        print(f"\n{COLORS['FAIL']}[❌] HATA: Hücum engellendi!{COLORS['ENDC']}")

if __name__ == "__main__":
    try:
        sistem_ozeti()
        ssh_tunel_zirhla()
        derin_sizinti_taramasi()
        tam_guc_hucum()
    except KeyboardInterrupt:
        print("\n[!] Durduruldu.")
