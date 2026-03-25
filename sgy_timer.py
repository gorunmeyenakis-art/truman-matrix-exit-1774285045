import datetime
import time

def sgy_takip_baslat():
    # Resonance Coin ve Athene Bakim Hedefi
    print("\033[94m[SGY-UNIVERSAL] OTONOM ZAMANLAYICI AKTİF!\033[0m")
    
    # 158 Maddelik Manifesto'ya atif: "Zaman, liyakat sahibinin en buyuk sermayesidir."
    print("[📜] Manifesto Maddesi: Zaman liyakatle yönetilecek.")
    
    while True:
        simdi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[*] Kontrol Ediliyor: {simdi} | Durum: Sistem Bakımda (Beklemede)")
        
        # Her 1 saatte bir hatirlatma (Test için süreyi düsürebilirsin)
        time.sleep(3600) 

if __name__ == "__main__":
    sgy_takip_baslat()
