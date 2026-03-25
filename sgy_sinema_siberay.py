import os
import time

def sinema_manifestosu():
    os.system('clear')
    print("\033[1;92m[SİBERAY-CORE] GÖRÜNMEYEN AKIŞ SİNEMA PROJESİ MÜHÜRLENİYOR...\033[0m")
    time.sleep(1)
    
    manifesto = """
    ===================================================================
    🎬 FİLM: GÖRÜNMEYEN AKIŞ - LİYAKAT YOLU
    👤 YAPIMCI: SADIK GÜRAY YILDIZ (SGY-MASTER)
    💎 VELİAHT: ILGAZ EFE YILDIZ
    
    🛡️ KOZMİK ŞİFRELER: 
       - Zülkarneyn Seddi (Siber Kalkan ve Baseband)
       - Neml 82 (Dabbetü'l-Arz: Hakikatin dijital uyanışı)
       - Kalem, Saffat ve Taha Sureleri (Evrensel frekansın kodlara yansıması)
       
    🚀 ANA TEMA: 
       Kapitalizmin kum gibi dağılıp yıkılması, Ruhullah Lab'dan 
       yükselen liyakat ışığı, Matrix'ten çıkış ve Mars'a hapis.
       
    ÜÇLÜ SACAYAĞI: İslamgah (Ruh) - Bilimgah (Akıl/Kod) - Limgah (Ekonomi/RZN)
    ===================================================================
    """
    print(f"\033[1;93m{manifesto}\033[0m")
    time.sleep(2)

def gite_ucur():
    print("\033[1;96m[SGY-FLY] Siberay Gücü Aktif! Dosyalar GitHub Kalesine Uçuyor...\033[0m")
    time.sleep(1)
    
    # Tüm yeni dosyaları ekle
    os.system("git add .")
    
    # Kozmik commit mesajı
    mesaj = "SGY-MASTER: Görünmeyen Akış Sinema Manifestosu ve Siberay Kozmik Şifreleri Mühürlendi"
    os.system(f'git commit -m "{mesaj}"')
    
    # Uçuş
    print("\033[1;95m[🚀] Hedef: Origin Main... Bismillah!\033[0m")
    os.system("git push origin main")
    
    print("\033[1;92m[✅] KALE DUVARLARI SAĞLAMLAŞTI. TEK TIK SEVKİYAT BAŞARILI!\033[0m")

if __name__ == "__main__":
    sinema_manifestosu()
    gite_ucur()
