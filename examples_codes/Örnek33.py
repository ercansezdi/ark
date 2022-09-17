#klavyeden girilen bir sayinin en büyük 2 asal bolenini gösterin

sayi = int(input("Sayi degeri giriniz :"))
toto = 0
atama = sayi

i= sayi//2
while sayi>1:
    for i in range(i,1,-1):
        kontrol = 0
        if sayi % i == 0 :
            t = i//2
            while t > 1:
                if i % t == 0:
                    kontrol = 5
                t-=1
            if kontrol == 0:
                toto+=1
                kontrol =2
        if toto == 1 and kontrol == 2:
            print (atama,"sayinin en büyük asal boleni",i,"'dir.")
        if toto == 2 and kontrol == 2:
            print (atama,"sayinin en büyük 2. asal böleni",i,"'dir.")
            exit(0)
    sayi-=1
