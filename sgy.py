import sqlite3
import os

def veritabani_kontrol():
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS finans (id INTEGER PRIMARY KEY, platform TEXT, miktar REAL, birim TEXT)')
    cursor.execute('SELECT COUNT(*) FROM finans')
    if cursor.fetchone()[0] == 0:
        cursor.executemany('INSERT INTO finans (platform, miktar, birim) VALUES (?, ?, ?)', 
                          [('Pi', 0.0, 'PI'), ('Athene', 0.0, 'ATH'), ('RZN', 0.0, 'RZN')])
    conn.commit()
    conn.close()

def finans_guncelle():
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    print("\n[ 💰 VERİ GÜNCELLEME ]")
    print("1- Pi | 2- Athene | 3- RZN | 0- İptal")
    secim = input("Seçiminiz: ")
    
    mapping = {"1": "Pi", "2": "Athene", "3": "RZN"}
    if secim in mapping:
        try:
            yeni_input = input(f"Yeni {mapping[secim]} miktarını girin: ")
            yeni_miktar = float(yeni_input.replace(',', '.')) # Virgül girilirse noktaya çevirir
            cursor.execute('UPDATE finans SET miktar = ? WHERE platform = ?', (yeni_miktar, mapping[secim]))
            conn.commit()
            print(f"✅ {mapping[secim]} güncellendi!")
        except ValueError:
            print("❌ Hata: Lütfen sadece sayı girin!")
    conn.close()

def sgy_dashboard():
    veritabani_kontrol()
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    os.system('clear')
    
    print("========================================")
    print("   🛡️  SGY UNIVERSAL MASTER - V3.5 OMNI")
    print("      RUHULLAH LAB - ANA KOMUTA")
    print("========================================")
    
    print("\n[ 🛰️  STRATEJİK MODÜLLER ]")
    cursor.execute('SELECT madde_no, baslik, durum FROM projeler ORDER BY madde_no ASC')
    for m in cursor.fetchall():
        simge = "💎" if "RZN" in m[1] or "CORE" in m[1] else "🛡️"
        print(f"{simge} {m[0]:02d} | {m[1]:<25} | {m[2]}")
        
    print("\n[ 💰 RZN FINANSAL KATMAN ]")
    cursor.execute('SELECT platform, miktar, birim FROM finans')
    for f in cursor.fetchall():
        # Veriyi çekerken sayıya dönüştüğünden emin oluyoruz
        deger = float(f[1]) if f[1] is not None else 0.0
        print(f"📊 {f[0]:<7}: {deger:>10.2f} {f[2]}")
    
    print(f"\n🔐 Sistem Mührü: HW-SEAL [65f189ac]")
    print("========================================")
    print("G- Güncelle | X- Çıkış")
    
    komut = input("\nKomuta Merkezi Seçimi: ").lower()
    if komut == 'g':
        conn.close()
        finans_guncelle()
        sgy_dashboard()
    elif komut == 'x':
        conn.close()
        print("Sistem güvenli moda alındı.")
    else:
        conn.close()
        sgy_dashboard()

if __name__ == "__main__":
    sgy_dashboard()
