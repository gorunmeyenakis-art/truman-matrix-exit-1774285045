import os
import datetime

def plani_yururluge_koy():
    bugun = datetime.datetime.now()
    plan = {
        "CUMARTESİ": "Ilgaz Efe ile GitHub Kalesi Kontrolü ve RZN Analizi.",
        "PAZAR": "Fiziksel Rezonans ve Doğa Yürüyüşü (SGY-AQUA).",
        "HEDEF": "158 Maddelik Manifestonun Hayata Entegrasyonu."
    }
    
    os.system('clear')
    print("\033[93m--- [👨‍👦 SGY-MASTER: BABA-OĞUL GELECEK PLANI ] ---\033[0m\n")
    print(f"\033[92m[!] Tarih: {bugun.strftime('%Y-%m-%d')} | Durum: STRATEJİK HAZIRLIK\033[0m\n")
    
    for gun, gorev in plan.items():
        print(f"\033[94m{gun}:\033[0m {gorev}")
    
    # GITHUB'A 'MİRAS PLANI' OLARAK İŞLE
    os.system("git add .")
    os.system('git commit -m "SGY-MASTER: BABA-OĞUL GELECEĞİ İNŞA PLANI YÜRÜRLÜĞE GİRDİ." --allow-empty')
    os.system("git push origin master")
    
    print("\n\033[92m[🏆] PLAN MÜHÜRLENDİ. ILGAZ EFE İÇİN YENİ BİR ÇAĞ BAŞLIYOR!\033[0m")

if __name__ == "__main__":
    plani_yururluge_koy()
