import sqlite3
import os

def sistem_insa_et():
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    # Tablo Yapıları
    cursor.execute('CREATE TABLE IF NOT EXISTS projeler (id INTEGER PRIMARY KEY, madde_no INTEGER, baslik TEXT, durum TEXT, oncelik TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS finans (id INTEGER PRIMARY KEY, platform TEXT, miktar REAL, birim TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS manifesto (id INTEGER PRIMARY KEY, madde_no INTEGER, baslik TEXT, aciklama TEXT, kategori TEXT, ilerleme INTEGER DEFAULT 0)')
    
    # 15 Temel Modülün Yeniden Mühürlenmesi
    cursor.execute('SELECT COUNT(*) FROM projeler')
    if cursor.fetchone()[0] == 0:
        envanter = [
            (1, "SGY-CORE v11.0 Asayiş", "AKTİF", "KRİTİK"),
            (2, "SGY-BEREKET v12.0 Teşvik", "PLANLANDI", "YÜKSEK"),
            (3, "SGY-ISLAH v13.0 Adalet", "PLANLANDI", "YÜKSEK"),
            (4, "SGY-TRAFİK v14.1 Ulaşım", "BEKLEMEDE", "ORTA"),
            (5, "SGY-MİRAS v15.1 Miras", "GELİŞTİRİLİYOR", "KRİTİK"),
            (6, "SGY-AQUA v15.3 Ekoloji", "PLANLANDI", "YÜKSEK"),
            (7, "SGY-SANAYİ v17.0 Üretim", "PLANLANDI", "ORTA"),
            (8, "SGY-NİMET v18.0 Gıda", "PLANLANDI", "YÜKSEK"),
            (9, "SGY-YAPI v20.0 Mimari", "PLANLANDI", "ORTA"),
            (10, "SGY-AKADEMİ v21.0 Eğitim", "PLANLANDI", "YÜKSEK"),
            (11, "SGY-GRID v22.0 Enerji", "TASLAK", "KRİTİK"),
            (12, "SGY-NİHAİ v23.0 Entegrasyon", "TASLAK", "KRİTİK"),
            (13, "AETHER v4.0 Frekans", "DENEYSEL", "KRİTİK"),
            (14, "RZN CORE v9.0 Finans", "GELİŞTİRİLİYOR", "KRİTİK"),
            (15, "158 MADDE v1.0 Manifesto", "MÜHÜRLENDİ", "KRİTİK")
        ]
        cursor.executemany('INSERT INTO projeler (madde_no, baslik, durum, oncelik) VALUES (?, ?, ?, ?)', envanter)
    
    # Finans Başlangıç
    cursor.execute('SELECT COUNT(*) FROM finans')
    if cursor.fetchone()[0] == 0:
        cursor.executemany('INSERT INTO finans (platform, miktar, birim) VALUES (?, ?, ?)', 
                          [('Pi', 0.0, 'PI'), ('Athene', 0.0, 'ATH'), ('RZN', 0.0, 'RZN')])
    
    conn.commit()
    conn.close()

def sgy_dashboard():
    sistem_insa_et()
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    os.system('clear')
    
    print("========================================")
    print("   🛡️  SGY UNIVERSAL MASTER - V4.0 OMNI")
    print("      TANRI'NIN GÖZÜ - AKTİVASYON")
    print("========================================")
    
    # Stratejik Akış
    print("\n[ 🛰️  STRATEJİK MODÜLLER ]")
    cursor.execute('SELECT madde_no, baslik, durum FROM projeler ORDER BY madde_no ASC')
    for m in cursor.fetchall():
        simge = "💎" if "RZN" in m[1] or "CORE" in m[1] else "🛡️"
        print(f"{simge} {m[0]:02d} | {m[1]:<25} | {m[2]}")
        
    print("\n[ 💰 RZN FINANSAL KATMAN ]")
    cursor.execute('SELECT platform, miktar, birim FROM finans')
    for f in cursor.fetchall():
        print(f"📊 {f[0]:<7}: {f[1]:>10.2f} {f[2]}")
    
    print(f"\n🔐 Sistem Mührü: HW-SEAL [65f189ac]")
    print(f"📍 Konum: Büyükçekmece, İstanbul")
    print("========================================")
    conn.close()

if __name__ == "__main__":
    sgy_dashboard()
