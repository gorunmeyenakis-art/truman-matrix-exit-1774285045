import os
import time

# --- 1916-1923 İSTİKLAL REZONANSI ---
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "W": "\033[97m", "END": "\033[0m", "BOLD": "\033[1m"}

def ata_mirasini_tescil_et():
    os.system('clear')
    print(f"{C['BOLD']}{C['R']}--- [🇹🇷 SGY-MASTER: ATA MİRASI VE GAZİ RUHU TESCİLİ ] ---{C['END']}\n")
    
    tarihce = {
        "1916": "Mehmet Sadık Yıldız: Cihan Harbi ve Manevra Kahramanı.",
        "1923": "İstiklal Harbi Zaferi: Cumhuriyet'in Resmî Subay Mührü.",
        "SOY": "Sadık Güray Yıldız: Atasının İzinde, Liyakat Nöbetinde.",
        "DOKTRİN": "Dedemin düşmanı düşmanım, dostu dostumdur!"
    }
    
    for yil, olay in tarihce.items():
        print(f"{C['Y']}{yil}:{C['END']} {C['W']}{olay}{C['END']}")
        time.sleep(1)

    # GITHUB KALESİNE ATALIK MÜHRÜ
    os.system("git add .")
    commit_msg = "SGY-MASTER: ATA MEHMET SADIK YILDIZ'IN RUHU SISTEME ENTEGRE EDILDI. 1916-1923"
    os.system(f'git commit -m "{commit_msg}" --allow-empty')
    os.system("git push origin master")
    
    print(f"\n{C['G']}{C['BOLD']}[☝️] ALLAHUEKBER! SOYUNUN ŞEREFİ SİBER DEVLETİMİZE MÜHÜRLENDİ.{C['END']}")

if __name__ == "__main__":
    ata_mirasini_tescil_et()
