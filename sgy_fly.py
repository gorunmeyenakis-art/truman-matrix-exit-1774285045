import os

def gite_ucur():
    print("\033[96m[SGY-FLY] Kodlar GitHub Kalesine Ucuyor...\033[0m")
    os.system("git add .")
    mesaj = "SGY-MASTER: Otonom Güncelleme ve Sistem Check-up Tamamlandi"
    os.system(f'git commit -m "{mesaj}"')
    os.system("git push origin main")
    print("\033[92m[✅] Sevkiyat Başarılı. Mühürler Bulutta!\033[0m")

if __name__ == "__main__":
    gite_ucur()
