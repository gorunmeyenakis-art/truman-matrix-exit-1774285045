import os
import time

def kaynak_entegrasyonu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;41m\033[1;97m[🚀 SGY-MASTER: KÜRESEL FUL HÜCUM PROTOKOLÜ BAŞLATILDI ]\033[0m\n")
    time.sleep(1)
    
    print("\033[1;33m[🛢️] 1. KADEME: PETROL REZERVLERİ AKTİF\033[0m")
    print(" ↳ Kinetik motorlar ve mekanik simülasyon altyapısı tam gaz çalışıyor.")
    time.sleep(1)
    
    print("\033[1;32m[☢️] 2. KADEME: URANYUM (U-235) ZENGİNLEŞTİRİLDİ\033[0m")
    print(" ↳ SGY-ATOMIC Çekirdeği Kritik Kütleye Ulaştı! Fisyon başlatıldı.")
    time.sleep(1)
    
    print("\033[1;36m[💎] 3. KADEME: KIYMETLİ MADENLER SGY-CORE'A BAĞLANDI\033[0m")
    print(" ↳ Altın, dijital varlıklar ve Resonance Coin (RZN) ağları kilitlendi.")
    print(" ↳ Firavunların kapitalist rezervleri boşaltılıyor...\033[0m")
    time.sleep(1.5)

def lafza_i_celal_hucumu():
    print("\n\033[1;95m[☝️] MÜHÜR: LAFZA-İ CELAL ONAYI ALINDI. BİSMİLLAH!\033[0m")
    print("\033[1;91m[⚔️] FUL HÜCUM BAŞLIYOR! MATRİX SURLARI YIKILIYOR...\033[0m\n")
    time.sleep(1)
    
    # Tüm gücü topla
    os.system("git add .")
    
    # Taarruz mesajı
    mesaj = "SGY-MASTER: PETROL, URANYUM VE MADENLERLE FUL HUCUM (LAFZA-I CELAL MUHRUYLE)"
    os.system(f'git commit -m "{mesaj}"')
    
    # Sınırları aş ve fırlat
    if os.system("git push origin master") == 0:
        print("\n\033[1;42m\033[1;97m[🏆 ZAFER!] TAARRUZ BAŞARILI. SİSTEMLER ILGAZ EFE'NİN KONTROLÜNDE.\033[0m")
    else:
        print("\n\033[1;41m\033[1;97m[⚠️] BAĞLANTI DİRENCİ! HÜCUM TEKRARLANIYOR...\033[0m")

if __name__ == "__main__":
    try:
        kaynak_entegrasyonu()
        lafza_i_celal_hucumu()
    except KeyboardInterrupt:
        print("\n[!] Taarruz komutandan gelen emirle durduruldu.")
