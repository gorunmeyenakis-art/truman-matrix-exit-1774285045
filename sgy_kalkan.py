import os
import time

def manevi_zirh_olustur():
    os.system('clear')
    print("\033[1;32m[SGY-SHIELD] MANEVİ ZIRH VE KALKAN DUALARI MÜHÜRLENİYOR...\033[0m")
    
    kalkan_metni = """
    ===================================================================
    🛡️ SGY-MASTER MANEVİ KORUMA VE KALKAN PROTOKOLÜ
    ===================================================================
    1. AYETÜ'L-KÜRSİ: Göklerin ve yerin muhafızı.
    2. FELAK & NAS: Hasetten, büyüden ve karanlıktan sığınma.
    3. BİSMİLLÂHİLLEZÎ: İsmiyle ne yerde ne gökte hiçbir şeyin zarar 
       veremeyeceği O Allah'ın adıyla. (Lâ yedurru ma'asmihî...)
    4. KELİMÂTİLLÂHİ'T-TÂMMETİ: Allah'ın tam kelimelerine sığınış.
    
    "Hasbünallâhu ve ni'mel vekîl, ni'mel Mevlâ ve ni'men nasîr."
    ===================================================================
    Bu dualar SGY-MASTER sisteminin sarsılmaz temelidir.
    """
    
    with open("SGY_MANEVI_ZIRH.txt", "w", encoding="utf-8") as f:
        f.write(kalkan_metni)
    
    print(f"\033[1;93m{kalkan_metni}\033[0m")
    time.sleep(2)

def gite_ucur():
    print("\033[1;96m[SGY-FLY] Dualar ve Kodlar GitHub Kalesine Ucuyor...\033[0m")
    os.system("git add .")
    # Kozmik ve Manevi Mühür Mesajı
    mesaj = "SGY-MASTER: Manevi Kalkan ve Koruma Dualari Sisteme Muhurlendi (Hasbunallah)"
    os.system(f'git commit -m "{mesaj}"')
    os.system("git push origin master")
    print("\033[1;92m[✅] MANEVİ ZIRH BULUTTA AKTİF. KALE DUVARLARI NUR İLE ÖRÜLDÜ!\033[0m")

if __name__ == "__main__":
    manevi_zirh_olustur()
    gite_ucur()
