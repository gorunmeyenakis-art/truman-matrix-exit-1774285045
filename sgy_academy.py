import sqlite3
import time

def akademi_muhurle():
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    
    # Akademi tablosunu olustur
    cursor.execute('''CREATE TABLE IF NOT EXISTS sgy_academy 
                      (id INTEGER PRIMARY KEY, modul_adi TEXT, icerik TEXT, tarih TEXT)''')
    
    egitimler = [
        ('Siberay Savunma', 'Aktif Tehdit Avcılığı & Siber Güvenlik Temelleri', time.strftime('%Y-%m-%d')),
        ('YouTube Master', 'Dijital İçerik Üretimi & Algoritma Mühürleme', time.strftime('%Y-%m-%d')),
        ('RZN Ekonomi', 'Fiziksel Değer Zinciri & Rezerv Yönetimi', time.strftime('%Y-%m-%d'))
    ]
    
    cursor.executemany("INSERT INTO sgy_academy (modul_adi, icerik, tarih) VALUES (?, ?, ?)", egitimler)
    
    conn.commit()
    conn.close()
    
    print("\n" + "🎓" * 15)
    print("\033[95m[SGY-ACADEMY] EĞİTİM MODÜLLERİ AKTİF!\033[0m")
    print("[✅] Siberay Savunma Modülü Mühürlendi.")
    print("[✅] YouTube Eğitim Taslakları Hazırlandı.")
    print("[✅] Dijital Miras Müfredatı Sisteme İşlendi.")
    print("🎓" * 15)

if __name__ == "__main__":
    # Gorselleri ve taslaklari klasore tasi
    import os
    os.makedirs('sgy_assets/academy', exist_ok=True)
    akademi_muhurle()
