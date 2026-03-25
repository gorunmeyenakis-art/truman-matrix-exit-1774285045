import time
import random

def sgy_balina_takip():
    print("\033[96m[SGY-UNIVERSAL] BALİNA AVCI MODÜLÜ AKTİF!\033[0m")
    print("[!] Piyasa derinliği analiz ediliyor...")
    
    while True:
        simule_islem = random.uniform(1000, 500000)
        if simule_islem > 100000:
            print(f"\033[91m[UYARI] Büyük hareket tespit edildi: {simule_islem:.2f} RZN!\033[0m")
            print("[🛡️] SGY-Zırh Devrede: Rezonans dengeleniyor...")
        else:
            print(f"\033[92m[NORMAL] Akış stabil: {simule_islem:.2f} RZN\033[0m")
        
        time.sleep(2)
        # 5 saniye sonra durdurmak için (test amaçlı)
        break 

if __name__ == "__main__":
    sgy_balina_takip()
