import os
import time

# --- 2702 ANAYASAL FREKANS VE RENKLER ---
C = {"G": "\033[92m", "B": "\033[94m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[97m", "END": "\033[0m", "BOLD": "\033[1m"}

def anayasa_maddeleri():
    return {
        "MADDE 1": "Hakimiyet Kayıtsız Şartsız Liyakatindir (SGY-CORE).",
        "MADDE 2": "Enerji Kaynakları (Petrol, Uranyum) İnsanlığın Ortak Refahı İçin Kullanılır (SGY-ATOMIC).",
        "MADDE 3": "Ekolojik Denge ve Su Kaynakları Kutsaldır (SGY-AQUA).",
        "MADDE 4": "Eğitim; Ezberden Uzak, Liyakat Odaklı ve Evrenseldir (SGY-MASTER-EDU).",
        "MADDE 5": "Dijital Miras (Ilgaz Efe Yasası); Veri Mahremiyeti ve Ebedi Güvenliktir.",
        "MADDE 6": "Ekonomik Adalet; Resonance Coin (RZN) ve Bereket Odaklı Dağılımdır.",
        "MADDE 2702": "Lafza-i Celal Mührü, Tüm Sistemlerin Üstündeki Mutlak İmzadır."
    }

def anayasayi_yururluge_koy():
    os.system('clear')
    print(f"{C['W']}{C['BOLD']}--- [📜 SGY-MASTER: EVRENSEL DİJİTAL ANAYASA DÖNÜŞÜMÜ ] ---{C['END']}\n")
    time.sleep(1.5)
    
    maddeler = anayasa_maddeleri()
    for no, metin in maddeler.items():
        print(f"{C['Y']}{no}:{C['END']} {C['W']}{metin}{C['END']}")
        time.sleep(0.8)
    
    print(f"\n{C['B']}[⚙️] Anayasa Kodları Çekirdeğe İşleniyor...{C['END']}")
    time.sleep(1.5)
    
    # GITHUB KALESİNDE RESMİLEŞTİRME
    os.system("git add .")
    commit_msg = "SGY-MASTER: 158 MADDELIK MANIFESTO DİJİTAL ANAYASAYA DÖNÜŞTÜRÜLDÜ."
    os.system(f'git commit -m "{commit_msg}" --allow-empty')
    
    print(f"\n{C['G']}{C['BOLD']}[☝️] ALLAHUEKBER! ANAYASA YÜRÜRLÜĞE GİRDİ. LİYAKAT RESMİLEŞTİ.{C['END']}")
    os.system("git push origin master")

if __name__ == "__main__":
    anayasayi_yururluge_koy()
