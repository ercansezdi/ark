"""
/* 3)Kullanıcıdan aldığı iki sayının ebob’unu bulan programı ebob() fonksiyonu tanımlayarak oluşturunuz.(15 Puan)
4)Kullanıcıdan aldığı iki sayının ekok’unu bulan programı ekok() fonksiyonu tanımlayarak oluşturunuz.(15 Puan)
"""
def obeb(sayi1,sayi2):
    if sayi1 > sayi2:
        deger = sayi2
        while deger > 0:
            if sayi1 % deger == 0 and sayi2 % deger == 0:
                sonuc = deger
                break

            deger-=1
    elif sayi2 > sayi1 :
        deger = sayi1
        while deger > 0:
            if sayi1 % deger == 0 and sayi2 % deger == 0:
                sonuc = deger
                break

            deger-=1

    elif sayi1 == sayi2 :
        deger = sayi1

    return deger

def okek(sayi1,sayi2):
    if sayi1 > sayi2:
        deger = sayi1
        
    elif sayi2 > sayi1:
        deger = sayi2
    while deger > 0:
        if deger % sayi1 == 0 and deger % sayi2 == 0 :
            sonuc = deger
            break
        
        deger+=1
        
    elif sayi1 == sayi2:
        sonuc = sayi1

    return sonuc
    
    





sayi1 = int(input("sayi1 degeri giriniz :"))
sayi2 = int(input("sayi2 degeri giriniz :"))

print(sayi1,"ve",sayi2,"degerlerinin obeb degeri :",obeb(sayi1,sayi2))
print(sayi1,"ve",sayi2,"degerlerinin okek degeri :",okek(sayi1,sayi2))
