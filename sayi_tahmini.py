from random import randint


tahmin_sayisi = []
kullanıcı_tahmini = []
hak = 9
oyun_sayisi = 0

while True:
    kullanıcı_tahmini = []
    kura_sayi = randint(0,100)
    tahmin_sayisi.append(kura_sayi)
    print(tahmin_sayisi)

    while True:
        kullanıcı_tahmini.append(int(input("lüten bir sayı giriniz: ")))
        print(tahmin_sayisi,kullanıcı_tahmini,tahmin_sayisi==kullanıcı_tahmini)
        if tahmin_sayisi[oyun_sayisi] == kullanıcı_tahmini[-1]:
            print("müneccim misin mübarek")
            break
        elif tahmin_sayisi[oyun_sayisi] < kullanıcı_tahmini[-1]:
            print(("lütfen daha düşük bir tahmin giriniz: "))
        elif tahmin_sayisi[oyun_sayisi] > kullanıcı_tahmini[-1]:
            print("lütfen daha büyük bir tahmin giriniz: ")
            
    print("Kullanici Tahminleri : ",(kullanıcı_tahmini))
    tekrar = input("Tekrar oynamak istemisin(Y/N) :")
    if tekrar == "N":
        break
    else:
        oyun_sayisi +=1
    if hak == 0:
        print("kaybettiniz başka zaman belki :)")
        break