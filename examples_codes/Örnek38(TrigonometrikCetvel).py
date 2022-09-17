def fakt(x):
    carpim = 1
    while x >= 1:
        carpim *= x
        x -= 1
    return carpim


pi = 3.14155926
i = 1
kontrol = 1
radyan = 1
sin_toplam = 0.0
cos_toplam = 0.0
hassasiyet = 171
while i < 180:
    t = 1
    kontrol = 1
    sin_toplam = 0
    cos_toplam = 0
    radyan = i * pi / 180
    while t < hassasiyet:
        if kontrol % 2 == 1:
            sin_toplam += pow(radyan, t) / fakt(t)
        elif kontrol % 2 == 0:
            sin_toplam += (-1) * pow(radyan, t) / fakt(t)
        t += 2;
        kontrol += 1
    t = 0
    kontrol = 1
    while t < hassasiyet:
        if kontrol % 2 == 1:
            cos_toplam += pow(radyan, t) / fakt(t)
        elif kontrol % 2 == 0:
            cos_toplam += (-1) * pow(radyan, t) / fakt(t)
        t += 2
        kontrol += 1
    print("sin(", i, ") :", sin_toplam, sep="")
    print("cos(", i, ") :", cos_toplam, sep="")
    print("tan(", i, ") :", sin_toplam / cos_toplam, sep="")
    print("cot(", i, ") :", cos_toplam / sin_toplam, sep="")
    print("\n")

    i += 1
