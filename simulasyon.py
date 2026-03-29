import numpy as np
import time
import os
import random

# Türkiye haritası (basit 20x20 grid)
genislik, yukseklik = 20, 20
harita = np.zeros((yukseklik, genislik), dtype=int)

# Başlangıç: Türkiye'nin bazı şehirleri canlı hücre olarak
harita[5][5] = 1  # İstanbul
harita[10][10] = 1  # Ankara
harita[15][3] = 1  # İzmir
harita[2][18] = 1  # Trabzon

# Conway kuralları
def komsular(x, y):
    toplam = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < yukseklik and 0 <= ny < genislik:
                toplam += harita[nx][ny]
    return toplam

def adim():
    global harita
    yeni_harita = np.zeros((yukseklik, genislik), dtype=int)
    for x in range(yukseklik):
        for y in range(genislik):
            canli_komsu = komsular(x, y)
            if harita[x][y] == 1:  # Canlı hücre
                if canli_komsu < 2 or canli_komsu > 3:
                    yeni_harita[x][y] = 0  # Ölür
                else:
                    yeni_harita[x][y] = 1  # Yaşar
            else:  # Ölü hücre
                if canli_komsu == 3:
                    yeni_harita[x][y] = 1  # Doğar
    harita = yeni_harita

# Ekranı temizle
def temizle():
    os.system('clear')

# Haritayı çiz
def ciz():
    temizle()
    for x in range(yukseklik):
        for y in range(genislik):
            if harita[x][y] == 1:
                print("🟩", end=" ")  # Canlı hücre (Türkiye şehirleri)
            else:
                print("⬛", end=" ")  # Ölü hücre
        print()
    print("\n--- Türkiye Cennet Simülasyonu ---")
    print("Komutlar:")
    print("1: Adım ilerlet | 2: Rastgele şehir ekle | 3: Şehir sil | 4: Temizle | 5: Çıkış")

# Tanrısal komutlar
def komut_al():
    secim = input("Komut girin (1/2/3/4/5): ")
    if secim == "1":
        adim()
    elif secim == "2":
        x, y = random.randint(0, yukseklik-1), random.randint(0, genislik-1)
        harita[x][y] = 1
    elif secim == "3":
        x = int(input("Satır (0-19): "))
        y = int(input("Sütun (0-19): "))
        harita[x][y] = 0
    elif secim == "4":
        harita = np.zeros((yukseklik, genislik), dtype=int)
    elif secim == "5":
        exit()
    else:
        print("Geçersiz komut!")

# Ana döngü
while True:
    ciz()
    komut_al()
