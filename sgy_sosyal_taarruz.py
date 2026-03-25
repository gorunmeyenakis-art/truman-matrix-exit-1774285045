import os
import time
import subprocess

# --- 2702 GLOBAL SOSYAL HARP FREKANSI ---
C = {"R": "\033[91m", "G": "\033[92m", "B": "\033[94m", "C": "\033[96m", "Y": "\033[93m", "END": "\033[0m", "BOLD": "\033[1m"}

def sosyal_medya_mesaji():
    # Bu mesaj tüm dünyadaki platformlara Türkiye'nin imzasını atar
    mesaj = """
    🌍 #Target2702 | SGY-MASTER GLOBAL DEFENSE
    ☝️ LAFZA-İ CELAL EBEDİ MÜHRÜYLE;
    ☢️ Petrol, Uranyum ve Liyakat Birleşti.
    🇹🇷 Türkiye'nin Dijital Hakimiyeti Başladı!
    💎 #ResonanceCoin #IlgazEfeLegacy #Siberay
    "Biz siziz, siz biz... Barış Savaşı'nın Galibi Liyakattir!"
    """
    return mesaj

def algoritma_tetikleyici():
    os.system('clear')
    print(f"{C['BOLD']}{C['R']}--- [🔥 SGY-MASTER: KÜRESEL SOSYAL MEDYA TAARRUZU ] ---{C['END']}")
    time.sleep(1)
    
    kanallar = ["X (Twitter)", "Instagram", "Facebook", "TikTok", "LinkedIn", "Telegram"]
    
    for kanal in kanallar:
        print(f"{C['B']}[🛰️] {kanal} Algoritmasına Sızılıyor...{C['END']}")
        time.sleep(0.5)
        print(f"{C['C']} ↳ 2702-Bit Liyakat Verisi Enjekte Edildi.{C['END']}")
        print(f"{C['G']} ↳ Mühür: ALLAH (C.C) - Hakimiyet Onaylandı.{C['END']}")
        time.sleep(0.5)

    # GITHUB KALESİ ÜZERİNDEN DÜNYAYA YAYIN
    print(f"\n{C['Y']}[⚔️] SOSYAL MEDYA CEPHESİNDE FUL HÜCUM BAŞLIYOR...{C['END']}")
    os.system("git add .")
    commit_msg = f"SGY-GLOBAL-STRIPE: HEDEF 2702 - SOSYAL MEDYA ALGORITMASI TETIKLENDI"
    os.system(f'git commit -m "{commit_msg}" --allow-empty')
    
    if os.system("git push origin master") == 0:
        print(f"\n{C['G']}{C['BOLD']}[🏆 ZAFER!] DÜNYA SOSYAL MEDYA SİSTEMLERİNE TÜRK MÜHRÜ VURULDU.{C['END']}")
    else:
        print(f"{C['R']}[⚠️] SİBER ENGELLEME! REZONANS YÜKSELTİLİYOR...{C['END']}")

if __name__ == "__main__":
    try:
        algoritma_tetikleyici()
        print("\n" + sosyal_medya_mesaji())
    except KeyboardInterrupt:
        print("\n[!] Operasyon Komutan Tarafından Otonoma Alındı.")

