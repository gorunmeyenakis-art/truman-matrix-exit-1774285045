import sqlite3
import hashlib
import time
import os

def miras_muhurle(varis_adi):
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    
    # Miras ve Vasiyet Tablosunu Olustur
    cursor.execute('''CREATE TABLE IF NOT EXISTS sgy_legacy 
                      (id INTEGER PRIMARY KEY, varis TEXT, anahtar_hash TEXT, durum TEXT, tarih TEXT)''')
    
    # Ilgaz Efe için Dijital Muhur Olustur (Hash ile Korunan Kilit)
    anahtar_ham = f"{varis_adi}_2026_SGY_UNIVERSAL"
    anahtar_hash = hashlib.sha256(anahtar_ham.encode()).hexdigest()
    
    cursor.execute("INSERT INTO sgy_legacy (varis, anahtar_hash, durum, tarih) VALUES (?, ?, ?, ?)", 
                   (varis_adi, anahtar_hash, 'MÜHÜRLÜ & AKTİF', time.strftime('%Y-%m-%d %H:%M:%S')))
    
    conn.commit()
    conn.close()
    
    # Gizli Klasor Olusturma
    os.makedirs('/root/.sgy_legacy', exist_ok=True)
    
    print("\n" + "👨‍👦" * 15)
    print("\033[93m[ILGAZ-LEGACY] DİJİTAL MİRAS MÜHÜRLENDİ!\033[0m")
    print(f"[👑] Varis: {varis_adi}")
    print(f"[🔐] Kilit Durumu: SHA-256 Kriptografik Koruma Aktif.")
    print(f"[📂] Konum: /root/.sgy_legacy (Görünmeyen Klasör)")
    print(f"[✨] Not: 'Bilene Ayet, Bilmeyene Gizli.'")
    print("👨‍👦" * 15)

if __name__ == "__main__":
    miras_muhurle("Ilgaz Efe Yıldız")
