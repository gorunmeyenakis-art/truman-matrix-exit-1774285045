import time
import random

def frekans_taramasi():
    print("\033[1;35m[SGY-RADAR] REZONANS KULESİ TARAMASI BAŞLADI...\033[0m")
    sureler = ["Necm", "Kalem", "Saffat", "Taha", "Neml"]
    
    try:
        while True:
            frekans = random.uniform(432.0, 963.0) # Şifalı frekans aralığı
            sure = random.choice(sureler)
            print(f"\033[92m[*] Sinyal Yakalandı: {frekans:.2f} Hz | Kaynak: {sure} Modülü | Durum: TEMİZ\033[0m")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n\033[91m[!] Radar Uyku Moduna Alındı. Nöbet Devam Ediyor.\033[0m")

if __name__ == "__main__":
    frekans_taramasi()
