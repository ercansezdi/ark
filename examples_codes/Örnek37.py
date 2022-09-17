"""
Tamsayi girişi yaptığımız her sayi için bu sayiların toplamını , çarpımını ,en buyuk sayi ,en kucuk sayi , tek ve çift sayilarn sayisi
ve virgulden sonra 3 basamak oalcak şekilde ortalmasini yazan progmram
"""
dizi = []

while True:
    Eleman=0
    tekSayi = 0
    ciftSayi = 0
    ToplamSayi = 0
    carpim = 1
    toplam = 0
    giris = int(input("\n\nSayi degeri giriniz :"))
    dizi.append(giris)
    Eleman=len(dizi)
    for i in dizi:
        ToplamSayi+=1
    dizi.sort()
    print('En kucuk sayi :',dizi[0])
    dizi.reverse()
    print('En buyuk sayi :', dizi[0])

    for i in dizi:
        toplam+=i;
    print("Sayilarin toplami :",toplam)

    for j in dizi:
        carpim*=j
    print("Sayilarin carpimi :",carpim)


    for i in dizi:
        if i % 2 == 0:
            ciftSayi+=1
        else:
            tekSayi+=1
    print("Tek sayi sayisi :",tekSayi)
    print("Cift sayi sayisi :",ciftSayi)
    v=toplam/(Eleman)
    v = str(v)
    giris=0
    kontrol=0
    print("Sayilarin ortalaması :",end="")
    for i in v:


        if giris==0:
            print(i,end="")

        if giris == 1:
            kontrol +=1
            print(i,end="")
            if kontrol == 3:
                break
        if i == '.':
            giris = 1











