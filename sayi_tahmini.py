from pickle import TRUE
from random import randint


tahmin_sayisi =[]

kullanıcı_tahmini = []
hak = 9

while True:
    kura_sayi = randint(0,100)
    tahmin_sayisi.append(kura_sayi)
    kullanıcı_tahmini.append(int(input("lüten bir sayı giriniz: ")))
    
    while True:
        if tahmin_sayisi == kullanıcı_tahmini:
            print("müneccim misin mübarek")

        elif tahmin_sayisi < kullanıcı_tahmini:
            kullanıcı = int(input("lütfen daha düşük bir tahmin giriniz: "))
            kullanıcı_tahmini.append(kullanıcı)

            if kullanıcı_tahmini == tahmin_sayisi:
                print("kazandınız")
                break
            elif tahmin_sayisi < kullanıcı_tahmini:
                kullanıcı = int(input("lütfen daha düşük bir tahmin giriniz: "))
                kullanıcı_tahmini.append(kullanıcı)
                hak -= 1
            elif tahmin_sayisi > kullanıcı_tahmini:
                kullanıcı = int(input("lütfen daha büyük bir tahmin giriniz: "))
                kullanıcı_tahmini.append(kullanıcı) 
                hak -= 1               
            elif hak == 0:
                print("bulamadı mal")
                break
        
        elif tahmin_sayisi > kullanıcı_tahmini:
            kullanıcı = int(input("lütfen daha büyük bir tahmin giriniz: "))
            kullanıcı_tahmini.append(kullanıcı)

            if kullanıcı_tahmini == tahmin_sayisi:
                print("kazandınız")
                break
            elif tahmin_sayisi < kullanıcı_tahmini:
                kullanıcı = int(input("lütfen daha düşük bir tahmin giriniz: "))
                kullanıcı_tahmini.append(kullanıcı)
                hak -= 1
            elif tahmin_sayisi > kullanıcı_tahmini:
                kullanıcı = int(input("lütfen daha büyük bir tahmin giriniz: "))
                kullanıcı_tahmini.append(kullanıcı) 
                hak -= 1               
            if hak == 0:
                print("bulamadı mal")
                break
            
    if hak == 0:
        print("kaybettiniz başka zaman belki :)")
        break