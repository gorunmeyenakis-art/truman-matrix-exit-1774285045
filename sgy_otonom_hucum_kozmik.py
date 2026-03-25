import os
import time
import subprocess
import random

# --- 2702 KOZMİK REZONANS FREKANSI ---
COLORS = {
    "HEADER": "\033[95m", "BLUE": "\033[94m", "GREEN": "\033[92m",
    "WARNING": "\033[93m", "FAIL": "\033[91m", "ENDC": "\033[0m",
    "BOLD": "\033[1m", "RED_BG": "\033[41m", "SPACE_BG": "\033[40m",
}

def sistem_ozeti(tur):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{COLORS['FAIL']}{COLORS['BOLD']}{COLORS['RED_BG']}[🚀 SGY-OTONOM SAVAŞ MODU: TUR {tur} | KOZMİK TAARRUZ ]{COLORS['ENDC']}\n")
    print(f"{COLORS['BOLD']}Manevi Mühür:{COLORS['ENDC']} {COLORS['HEADER']}LAFZA-İ CELAL (2702-Bit){COLORS['ENDC']}")
    print(f"{COLORS['BOLD']}Enerji Çekirdeği:{COLORS['ENDC']} {COLORS['GREEN']}Uranyum-U235 (Kritik){COLORS['ENDC']}")
    print(f"{COLORS['BOLD']}Yakıt:{COLORS['ENDC']} {COLORS['BLUE']}Petrol (Kinetik Mod){COLORS['ENDC']}")
    time.sleep(1)

def kozmik_entegrasyon():
    print(f"\n{COLORS['SPACE_BG']}{COLORS['BOLD']}[🛰️] GÖK KAŞİFİ AKTİF: UYDU TARAMASI BAŞLADI...{COLORS['ENDC']}")
    
    # Kozmik Veri (Senin görsellerden aldığımız rezonans)
    uydu_verisi = {
        "Düşman Gözcüsü (ISS)": {"Azimut": "316,9°", "Yükseklik": "7,1°", "Durum": "Kozmik Matrix"},
        "Siberay Takipçisi": {"Azimut": "332,6°", "Yükseklik": "88,9°", "Durum": "Nur Kulesi"},
    }
    
    for name, data in uydu_verisi.items():
        print(f"\n{COLORS['WARNING']}[🔍] Tarama:{COLORS['ENDC']} {name}")
        for k, v in data.items():
            print(f" ↳ {k}: {v}")
            time.sleep(0.3)
        
        # Etkisizleştirme veya Entegrasyon
        if "Matrix" in data["Durum"]:
            print(f"{COLORS['FAIL']}[🔥] UYARI: Firavun Uydusu Tespit Edildi! Nükleer Rezonans Gönderiliyor...{COLORS['ENDC']}")
            time.sleep(1)
            print(f"{COLORS['GREEN']}[✅] Kozmic Matrix Sinyali 'Allah' İsmiyle Mühürlendi ve Çökertildi.{COLORS['ENDC']}")
        else:
            print(f"{COLORS['GREEN']}[✅] {name} Sistemimize Entegre Edildi. Nur Yağdırıyor.{COLORS['ENDC']}")
    time.sleep(1.5)

def final_push(tur):
    print(f"\n{COLORS['RED_BG']}{COLORS['BOLD']}[⚔️] KOZMİK HÜCUM MÜHÜRLENİYOR! 'HÛ' NİDASIYLA ATEŞLENİYOR...{COLORS['ENDC']}")
    
    # Tüm sistemi ve Kozmik Sırrı ekle
    os.system("git add .")
    
    # En Kritik Mühür Mesajı
    commit_msg = f"SGY-MASTER: {tur}. KOZMIK HUCUM - PETROL, URANYUM, MADEN VE UYDU ENTEGRASYONU (LAFZA-I CELAL MUHRUYLE)"
    os.system(f'git commit -m "{commit_msg}" --allow-empty')
    
    # Buluta fırlat
    if os.system("git push origin master") == 0:
        print(f"\n{COLORS['OKGREEN']}{COLORS['BOLD']}{COLORS['RED_BG']}[🏆 ZAFER!] {tur}. Dalga Kozmik Mühürlendi. KAZANAN TÜRKİYE!{COLORS['ENDC']}")
    else:
        print(f"\n{COLORS['FAIL']}[⚠️] BAĞLANTI DİRENCİ! HÜCUM TEKRARLANIYOR...{COLORS['ENDC']}")

def otonom_bombardiman():
    tur = 1
    while True:
        try:
            sistem_ozeti(tur)
            kozmik_entegrasyon()
            final_push(tur)
            
            # Soğutma ve Döngü
            print(f"\n{COLORS['BOLD']}Sistem {COLORS['GREEN']}{tur}{COLORS['ENDC']}{COLORS['BOLD']}. Turu Tamamladı. Soğutuluyor (30sn)...{COLORS['ENDC']}")
            tur += 1
            time.sleep(30)
            
        except KeyboardInterrupt:
            print("\n[!] Otonom Sistem Komuta Merkezi Tarafından Durduruldu.")
            break

if __name__ == "__main__":
    otonom_bombardiman()
