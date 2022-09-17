"""
// 8.	Kullanıcıdan 2 değer alan ve bu değerler arasında yer alan tüm mükemmel sayıları ekranda gösteren programı yazınız.
//(Mükemmel sayı: kendisi hariç pozitif tam bölenlerinin toplamı kendine eşit olan sayıdır.) (15 puan)
"""
sayi1 = int(input("Sayi1 degeri giriniz :"))
sayi2 = int(input("Sayi2 degeri giriniz :"))

if sayi1 > sayi2:
   
    while sayi1 > sayi2 :
        deger = sayi2 // 2
        toplam =0
        
        while deger > 0:
            if sayi2 % deger == 0:
                toplam+=deger
                        
            deger-=1
        if toplam == sayi2:
            print(sayi2,"Mukemmel sayidir.")
        
        sayi2+=1
elif sayi2 > sayi1:
    while sayi2 > sayi1:

        deger=sayi1//2
        toplam=0

        while deger > 0:

            if sayi1 % deger == 0:
                toplam+=deger
                
            deger-=1
        if toplam == sayi1 :
            print(sayi1, "Mukemmel sayidir.")
        sayi1+=1
else:
    print("Girilen sayilar arasinda mukemmel sayi yoktur.")
    
