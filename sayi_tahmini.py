from pickle import TRUE
from random import randint

tahmin_sayisi =[]

kullanıcı_tahmini = []
hak = 10

while kullanıcı_tahmini in TRUE:
    kura_sayi = randint(0,100)
    tahmin_sayisi.append(kura_sayi)
    input("lütfen 0 ile 100 arasında bir tahmin giriniz:")
    if 50< tahmin_sayisi <=100:
        kullanıcı = input("lütfen 50 ile 100 arasında bir tahmin giriniz: ")
        kullanıcı_tahmini.append(kullanıcı)
        if kullanıcı_tahmini == tahmin_sayisi:
            print("kazandınız")
            break
        else:
            input("lütfen tekrardeneyin:")
            hak-=1
    elif 0< tahmin_sayisi<=50:
        kullanıcı = input("lütfen 0 ile 50 arasında bir tahmin giriniz: ")
        kullanıcı_tahmini.append(kullanıcı)
        if kullanıcı_tahmini == tahmin_sayisi:
            print("kazandınız")
            break
        else:
            input("lütfen tekrardeneyin:")
            hak-=1
    else:
        print("hacı abi naptın ya")
if hak == 0:
    print("kaybettiniz başka zaman belki :)")

