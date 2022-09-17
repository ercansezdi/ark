#1 ile istenen sayi arasındaki mükemmel sayıları bulup ekrana gösteren programı fonksiyonlar yardımıyla oluşturunuz.(20 Puan)
"""
Kendisi hariç bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir.
"""
def mukemmel_sayi(sayi):
    while sayi > 0:
        bolen_sayi = sayi // 2
        toplam = 0
        while bolen_sayi > 0:
            if sayi % bolen_sayi == 0:
                toplam+=bolen_sayi
            bolen_sayi-=1
        if toplam == sayi:
            print(sayi,"sayisi mukemmel sayidir.")
        sayi-=1
        






deger = int(input("1 ile hangi sayi arasindaki mukemmel sayilar bulsun giriniz :"))
mukemmel_sayi(deger)
