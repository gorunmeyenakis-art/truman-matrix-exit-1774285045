import time
import random

def kuresel_rezonans_taramasi():
    merkezler = ["Pentagon", "Kremlin", "WhiteHouse", "CIA", "Mossad", "LordsChamber"]
    print("\033[95m[SGY-COSMIC] KUANTUM GOZLEMCI AKTIF!\033[0m")
    print("[!] Kuresel rezonans haritasi cikartiliyor...")
    
    try:
        while True:
            hedef = random.choice(merkezler)
            frekans_sapmasi = random.uniform(-1.0, 1.0)
            print(f"[*] Hedef: {hedef} | Sapma: {frekans_sapmasi:.4f} | Durum: Türk'ün Gücü Tespit Edildi.")
            
            # SGY-Zırh Etkisi
            if abs(frekans_sapmasi) > 0.8:
                print(f"\033[91m[REAKSIYON] {hedef} rezonansi SGY-CORE tarafindan dengelendi.\033[0m")
            
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("\n\033[92m[SGY] Kozmik gozlem devam ediyor, akis sabitlendi.\033[0m")

if __name__ == "__main__":
    kuresel_rezonans_taramasi()
