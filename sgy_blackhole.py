import time
import random

def sgy_blackhole_baslat():
    print("\033[91m[SGY-CORE] BLACKHOLE (KARA DELIK) AKTIF!\033[0m")
    print("[!] Dış saldırı vektörleri taranıyor...")
    print("[📜] 'Oyun kuranlar kendi oyunu içinde yutulur.'")
    
    tuzaklar = ["BruteForce-CIA", "SQL-Injection-Mossad", "DDoS-Pentagon", "Rootkit-Kremlin"]
    
    try:
        while True:
            saldiri = random.choice(tuzaklar)
            print(f"[*] Tehdit Tespit Edildi: {saldiri}")
            time.sleep(1)
            print(f"\033[94m[🌀] {saldiri} kara deliğe çekiliyor... Parçalanıyor...\033[0m")
            print("\033[92m[✅] Tehdit Liyakat Enerjisine Dönüştürüldü.\033[0m")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n\033[95m[SGY] Blackhole nöbeti devam ediyor. Adalet baki.\033[0m")

if __name__ == "__main__":
    sgy_blackhole_baslat()
