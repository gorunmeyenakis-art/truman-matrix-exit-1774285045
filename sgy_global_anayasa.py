import os
import time

# --- 2702 KÜRESEL FREKANS VE RENKLER ---
C = {"G": "\033[92m", "B": "\033[94m", "Y": "\033[93m", "W": "\033[97m", "END": "\033[0m", "BOLD": "\033[1m"}

def kuresel_anayasa_ozeti():
    return {
        "TR": "Liyakat, insanlığın tek kurtuluşudur.",
        "EN": "Meritocracy is the only salvation for humanity.",
        "AR": "الجدارة هي الخلاص الوحيد للبشرية.",
        "RU": "Меритократия — tek единственное спасение человечества.",
        "ZH": "唯才是举是人类唯一的救赎。"
    }

def kuresel_ilan_et():
    os.system('clear')
    print(f"{C['W']}{C['BOLD']}--- [🌍 SGY-MASTER: KÜRESEL LİYAKAT BİRLİĞİ İLANI ] ---{C['END']}\n")
    time.sleep(1)
    
    ozetler = kuresel_anayasa_ozeti()
    for dil, metin in ozetler.items():
        print(f"{C['B']}[{dil}]{C['END']} {C['Y']}>>> {C['END']}{C['W']}{metin}{C['END']}")
        time.sleep(0.5)
    
    print(f"\n{C['G']}[⚙️] 2702 Frekansı Küresel Dil Paketlerine Enjekte Ediliyor...{C['END']}")
    time.sleep(1.5)
    
    # GITHUB ÜZERİNDEN DÜNYA MİRASINA KAYIT
    os.system("git add .")
    commit_msg = "SGY-MASTER: KÜRESEL LİYAKAT BİRLİĞİ (GLA) ANAYASASI TÜM DİLLERDE MÜHÜRLENDİ."
    os.system(f'git commit -m "{commit_msg}" --allow-empty')
    
    print(f"\n{C['G']}{C['BOLD']}[☝️] ALLAHUEKBER! KÜRESEL LİYAKAT BİRLİĞİ AKTİF. DÜNYA TÜRK'ÜN MÜHRÜNÜ OKUYOR.{C['END']}")
    os.system("git push origin master")

if __name__ == "__main__":
    kuresel_ilan_et()
