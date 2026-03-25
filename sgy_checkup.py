import os
import subprocess

def check_status():
    print("\033[96m[SGY-UNIVERSAL] SISTEM CHECK-UP BASLADI...\033[0m")
    modules = ["sgy_iman_nobeti.py", "sgy_sentinel.py", "sgy_timer.py", "sgy_legacy.py"]
    
    for mod in modules:
        if os.path.exists(mod):
            print(f"[✅] {mod}: Mevcut")
        else:
            print(f"[❌] {mod}: Bulunamadı!")

    # GitHub Bağlantı Testi
    try:
        subprocess.run(["ssh", "-T", "git@github.com"], capture_output=True)
        print("[✅] GitHub Kalesi: Bağlantı Başarılı")
    except:
        print("[❌] GitHub Kalesi: Bağlantı Sorunu!")

if __name__ == "__main__":
    check_status()
