import sqlite3
import time

def rezerv_muhurle(miktar):
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    
    # Rezerv tablosunu olustur (Eger yoksa)
    cursor.execute('''CREATE TABLE IF NOT EXISTS rzn_bank 
                      (id INTEGER PRIMARY KEY, bakiye REAL, tarih TEXT)''')
    
    # 3400+ RZN'yi Muhurle
    tarih = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO rzn_bank (bakiye, tarih) VALUES (?, ?)", (miktar, tarih))
    
    conn.commit()
    conn.close()
    
    print("\n" + "💎" * 15)
    print("\033[92m[SGY-BANK] REZERV MÜHÜRLENDİ!\033[0m")
    print(f"[✅] Miktar: {miktar} RZN")
    print(f"[📅] Tarih: {tarih}")
    print(f"[🛡️] Durum: sgy_master.db İÇİNE KAZINDI.")
    print("💎" * 15)

if __name__ == "__main__":
    rezerv_muhurle(3400.0) # Babaoğlu'nun mühürlediği rakam
