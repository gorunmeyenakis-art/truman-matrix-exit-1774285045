import time
import random

def sgy_sentinel_uyandir():
    print("\033[93m[SGY-UNIVERSAL] SENTINEL UYANDIRILIYOR...\033[0m")
    print("[🛡️] Casper Sinyal Protokolü ile eşleşiliyor...")
    time.sleep(2)
    
    try:
        while True:
            # Sinyal gücü ve frekans analizi (Simüle)
            frekans = random.uniform(2.4, 5.8)
            guvenlik_skoru = random.randint(80, 100)
            
            print(f"[*] Frekans: {frekans:.2f} GHz | Güvenlik Skoru: %{guvenlik_skoru}")
            
            if guvenlik_skoru < 85:
                print("\033[91m[ALARM] Matrix Sızıntısı Tespit Edildi! SSH Tüneli Zırhlanıyor...\033[0m")
            
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("\n\033[92m[DURDURULDU] Sentinel Nöbeti Devrediyor.\033[0m")

if __name__ == "__main__":
    sgy_sentinel_uyandir()
