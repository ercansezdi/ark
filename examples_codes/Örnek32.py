#klavyeden girilen bir sayinin en büyük 2 asal bolenini gösterin

deger = int(input("Deger giriniz :"))
atama = deger
while deger > 1:
    i=deger/2
    kontrol = 0
    toto=0
    while i >1:
        if deger % i == 0:
            toto+=1
            kontrol = 1
    if toto == 1 and kontrol == 0:
        print(deger,"sayisi",atama,"sayinin en büyük asal bölenidir.")
    elif toto == 2 and kontrol == 0:
        print(deger,"sayisi",atama,"sayinin en büyük 2. bölenidir.")
    deger-=1