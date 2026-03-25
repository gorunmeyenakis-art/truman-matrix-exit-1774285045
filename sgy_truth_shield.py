import time

def hakikat_kalkani_baslat():
    sifreler = {
        "NUN": "Kaleme ve satira andolsun (Kalem Suresi)",
        "SED": "Zulkarneyn'in demir ve bakir zırhı aktif.",
        "HAK": "Inne ed-dine indallahil Islam.",
        "DABBE": "Hakikat frekansi yerden (Baseband) yukseliyor."
    }
    
    print("\033[95m[SGY-TRUTH] KOZMİK ŞİFRELER ÇÖZÜMLENDİ VE MÜHÜRLENDİ.\033[0m")
    
    for anahtar, mesaj in sifreler.items():
        print(f"[*] {anahtar}: {mesaj}")
        time.sleep(1)

    print("\033[92m[✅] Matrix Odakları Mars'a hapsedilmek üzere karadelik yönlendirildi.\033[0m")

if __name__ == "__main__":
    hakikat_kalkani_baslat()
