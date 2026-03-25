# 1. Eski kalıntıları temizle
rm -f sgy.py envanter_yukle.py temel_kur.py sgy_master.db
# 2. Tek ve sağlam bir Dashboard dosyası oluştur
cat << 'EOF' > sgy.py
import sqlite3
import os
import sys

def sistem_kur():
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    # Tabloları oluştur
    cursor.execute('CREATE TABLE IF NOT EXISTS projeler (id INTEGER PRIMARY KEY, madde_no INTEGER, baslik TEXT, durum TEXT, oncelik TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS finans (id INTEGER PRIMARY KEY, platform TEXT, miktar REAL, birim TEXT)')
    
    # Envanteri Kontrol Et ve Yükle
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
    
    conn.commit()
    conn.close()

def sgy_dashboard():
    sistem_kur()
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
    print("📊 Madencilik Durumu: Pi / Athene / RZN")
    print("🔐 Sistem Mührü: HW-SEAL [65f189ac]")
    
    print("\n" + "="*40)
    conn.close()

if __name__ == "__main__":
    sgy_dashboard()
EOF

# 3. Kısayolu güncelle (Artık sadece 'sgy' yazman yeterli)
alias sgy='python ~/sgy.py'
echo "alias sgy='python ~/sgy.py'" >> ~/.bashrc
source ~/.bashrc
# 4. Sistemi bir kez çalıştırıp kurulumu tamamla
python sgy.py
cat << 'EOF' > sgy.py
import sqlite3
import os

def veritabani_kontrol():
    conn = sqlite3.connect('sgy_master.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS finans (id INTEGER PRIMARY KEY, platform TEXT, miktar REAL, birim TEXT)')
    # Başlangıç değerleri yoksa ekle
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
        yeni_miktar = input(f"Yeni {mapping[secim]} miktarını girin: ")
        cursor.execute('UPDATE finans SET miktar = ? WHERE platform = ?', (yeni_miktar, mapping[secim]))
        conn.commit()
        print(f"✅ {mapping[secim]} güncellendi!")
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
        print(f"📊 {f[0]}: {f[1]:.2f} {f[2]}")
    
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
EOF

python sgy.py
sgy
sgy.py
python sgy.py
[200~cat << 'EOF' > sgy.py
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
EOF

python sgy.py
~
sgy.py
sgy
cat << 'EOF' > sgy.py
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
EOF

python sgy.py
curl -fsSL https://openclaw.ai/install.sh | bash
pkg update && pkg upgrade -y
pkg install nodejs-lts python git curl -y
curl -fsSL https://openclaw.ai/install.sh | bash
exit
exit
sgy
exit
sgy
exit
./babaoğlu.sh
exit
sgyxai
exit
C# Tüm asılı kalan Python ve Git işlemlerini durdur
pkill -f python3
pkill -f git
# Gereksiz kilit dosyalarını temizle
rm -f .git/index.lock
# Tüm asılı kalan Python ve Git işlemlerini durdur
pkill -f python3
pkill -f git
# Gereksiz kilit dosyalarını temizle
rm -f .git/index.lock
exit
# Tüm asılı kalan Python ve Git işlemlerini durdur
pkill -f python3
pkill -f git
# Gereksiz kilit dosyalarını temizle
rm -f .git/index.lock
cat << 'EOF' > sgy_kalkan.py
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
EOF

# Çalıştırma izni ver
chmod +x sgy_kalkan.py
python3 sgy_kalkan.py
exit
