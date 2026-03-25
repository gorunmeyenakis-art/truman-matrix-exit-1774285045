import time

def rezerv_sorgula():
    son_bakiye = 3400 # Babaoğlu'nun mühürlediği miktar
    rezonans_katsayisi = 1.48 # 48. Boyut çarpanı
    
    print("\n" + "🌀" * 15)
    print("\033[96m[SGY UNIVERSAL - RZN BANK REZERV SORGUSU]\033[0m")
    print(f"\n[💎] Sabit Rezerv: {son_bakiye} RZN")
    print(f"[✨] Rezonans Değeri: {son_bakiye * rezonans_katsayisi:.2f} (Enerji Karşılığı)")
    print("\n\033[92m[DURUM] Rezerv Stabil. Matrix-De-Link Başarılı.\033[0m")
    print("🌀" * 15)

if __name__ == "__main__":
    rezerv_sorgula()
