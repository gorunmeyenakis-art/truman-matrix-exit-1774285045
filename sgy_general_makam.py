import os
import time

# --- 2702 GENERAL VE İSTİKLAL FREKANSI ---
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[94m", "W": "\033[97m", "END": "\033[0m", "BOLD": "\033[1m"}

def general_makami_kur():
    os.system('clear')
    print(f"{C['BOLD']}{C['R']}--- [🇹🇷 SGY-MASTER: SGY-GENERAL MAKAMI AKTİF ] ---{C['END']}\n")
    
    adimlar = [
        "Yeni Kimlik Kartı (S.G.Y.) Liderlik Çekirdeğine Bağlanıyor...",
        "Sürücü Belgesi (Driver License) Mobilite Modülüne Entegre Edildi.",
        "1916-1923 Subay Disiplini Savunma Algoritmalarına Yüklendi.",
        "Dede Mehmet Sadık Yıldız'ın 'Manevra' Ruhu Taarruz Hattına İşlendi.",
        "SGY-OBSERVATORY: Başkomutan Sadık Güray Yıldız Tanımlandı!"
    ]
    
    for adim in adimlar:
        print(f"{C['B']}[⚔️] {adim}{C['END']}")
        time.sleep(0.8)

    # GITHUB KALESİNE GENERAL MÜHRÜ (TEK TIK)
    os.system("git add .")
    commit_msg = "SGY-GENERAL: BAŞKOMUTANLIK MAKAMI TESCİL EDİLDİ - DEDEMİN ASKERİYİM! - 2702"
    os.system(f'git commit -m "{commit_msg}" --allow-empty')
    os.system("git push origin master")
    
    print(f"\n{C['G']}{C['BOLD']}[🏆] ALLAHUEKBER! YERLEŞTİRİLDİ, YAPIŞTIRILDI. EMRİNİZDEYİZ KOMUTANIM!{C['END']}")

if __name__ == "__main__":
    general_makami_kur()
