import os
import time

# --- 1916-1923 İSTİKLAL VE MANEVRA REZONANSI ---
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "W": "\033[97m", "END": "\033[0m", "BOLD": "\033[1m"}

def ata_mirasini_tescil_et():
    os.system('clear')
    print(f"{C['BOLD']}{C['R']}--- [🇹🇷 SGY-MASTER: MEHMET SADIK YILDIZ ATA MİRASI TESCİLİ ] ---{C['END']}\n")
    
    tarihce = {
        "1916 (Manevra)": "Cihan Harbi'nin en çetin yılında subay liderliği ve kıvrak savaş stratejisi.",
        "1923 (İstiklal)": "Büyük Taarruz'dan Cumhuriyete uzanan bağımsızlık mücadelesinin resmî subay mührü.",
        "DOKTRİN": "Atamın düşmanı düşmanım, dostu dostumdur! Soyumu şerefle temsil ediyorum.",
        "SOY": "Torun Sadık Güray Yıldız: Atasının İzinde, Liyakat Nöbetinde."
    }
    
    for yil, olay in tarihce.items():
        print(f"{C['Y']}{yil}:{C['END']} {C['W']}{olay}{C['END']}")
        time.sleep(1)

    # GITHUB KALESİNE ATALIK MÜHRÜ VE İMZA
    os.system("git add .")
    commit_msg = "SGY-MASTER: ATA MEHMET SADIK YILDIZ'IN RUHU SISTEME MUHURLENDI. 1916-1923"
    os.system(f'git commit -m "{commit_msg}" --allow-empty')
    os.system("git push origin master")
    
    print(f"\n{C['G']}{C['BOLD']}[☝️] ALLAHUEKBER! ATA MİRASI ŞEREFLE MÜHÜRLENDİ.{C['END']}")

if __name__ == "__main__":
    ata_mirasini_tescil_et()
