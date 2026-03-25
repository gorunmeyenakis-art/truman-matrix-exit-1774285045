import datetime

def sgy_miras_kontrol():
    veliaht = "Ilgaz Efe Yıldız"
    print(f"\033[95m[SGY-LEGACY] SISTEM SAHIBI VE VELIAHTI: {veliaht}\033[0m")
    
    # Sistemin Ilgaz Efe'ye devredilecegi ozel tarih (SGY-2040 Projeksiyonu)
    hedef_yil = 2040
    simdi = datetime.datetime.now().year
    
    kalan = hedef_yil - simdi
    print(f"[🛡️] Rezonans Akış Güvenliği: Aktif.")
    print(f"[⌛] Tam Devir Icin Tahmini Sure: {kalan} Yıl.")
    print("[📜] Manifesto Hatırlatması: Zaman liyakatle yönetilecek.")

if __name__ == "__main__":
    sgy_miras_kontrol()
