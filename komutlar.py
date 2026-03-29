def ilim_ekle(harita):
    # Rastgele 3 şehirde ilim seviyesini artır (canlı hücre sayısını artır)
    for _ in range(3):
        x, y = random.randint(0, len(harita)-1), random.randint(0, len(harita[0])-1)
        harita[x][y] = 1
    return harita

def dusmani_yoket(harita):
    # "Düşman" olarak ölü hücrelerin etrafını temizle
    for x in range(len(harita)):
        for y in range(len(harita[0])):
            if harita[x][y] == 0:  # Ölü hücre (düşman bölgesi)
                if random.random() < 0.3:  # %30 ihtimalle yok et
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            nx, ny = x + i, y + j
                            if 0 <= nx < len(harita) and 0 <= ny < len(harita[0]):
                                harita[nx][ny] = 0  # Yok et
    return harita

def osmanli_topraklarini_geri_al(harita):
    # Haritanın sağ tarafına (Osmanlı toprakları) canlı hücreler ekle
    for x in range(len(harita)):
        for y in range(len(harita[0])//2, len(harita[0])):
            if random.random() < 0.2:  # %20 ihtimalle geri al
                harita[x][y] = 1
    return harita
