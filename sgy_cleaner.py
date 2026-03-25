import os
import shutil

def temizle():
    print("\033[93m[SGY-CLEANER] Sistem arindiriliyor...\033[0m")
    # Gereksiz gecici dosyalari ve apt cache'ini temizleme komutu
    os.system("rm -rf /tmp/*")
    os.system("apt-get clean")
    print("\033[92m[✅] Gereksiz yukler atildi. Sistem ferahladi.\033[0m")

if __name__ == "__main__":
    temizle()
