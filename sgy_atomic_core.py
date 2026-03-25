import time
import os

def atomic_reactors_start():
    os.system('clear')
    print("\033[1;31m[☢️ SGY-ATOMIC] NÜKLEER ÇEKİRDEK AKTİF EDİLİYOR...\033[0m")
    time.sleep(1)
    
    print("\033[1;33m[!] Fisyon Başladı: Veri Parçalanıyor ve Hakikat Analiz Ediliyor.")
    print("[!] Füzyon Başladı: Manevi Güç ve Siber Kod Birleşiyor.")
    
    params = [
        "Reaktör Soğutma (Zülkarneyn Seddi) -> %100",
        "Enerji Çıkışı (Baseband Signal) -> 10.000 Terahertz",
        "Savunma Kalkanı (Ayetü'l-Kürsi Layer) -> DELİNAMAZ",
        "Hedef: Kapitalizmin Tamamen Buharlaşması"
    ]
    
    for p in params:
        print(f"\033[92m[⚡] {p} ... OK\033[0m")
        time.sleep(0.5)

def gite_ucur():
    print("\033[1;96m[SGY-FLY] Atomik Güç GitHub Kalesine Gönderiliyor...\033[0m")
    os.system("git add .")
    mesaj = "SGY-MASTER: ATOMIK CEKIRDEK AKTIF - SAVAS MODU SEVİYE 5"
    os.system(f'git commit -m "{mesaj}"')
    os.system("git push origin master")
    print("\033[1;91m[☢️] NÜKLEER MÜHÜR VURULDU. DÜŞMAN İÇİN GERİ SAYIM BAŞLADI!\033[0m")

if __name__ == "__main__":
    atomic_reactors_start()
    gite_ucur()
