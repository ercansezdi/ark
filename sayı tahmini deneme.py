from random import randint

hak=10
tahmin_sayisi=randint(0,100)

while True:
    kullanıcı_tahmini=int(input("lütfen bir sayı giriniz: "))
    #print(tahmin_sayisi)
    
    if tahmin_sayisi<kullanıcı_tahmini:
        print("daha küçük bir sayı dene:")
        hak-=1
        print("kalan hak :",hak)
    elif tahmin_sayisi>kullanıcı_tahmini:
        print("daha büyük bir sayı dene:")
        hak-=1
        print("kalan hak:",hak)
    else:
        print("doğru tahmin tebrikler")
    if hak==0:
        print("kaybettiniz.")
        break
    elif kullanıcı_tahmini==tahmin_sayisi:
        break