#1 ile istenen sayi arasındaki mükemmel sayıları bulup ekrana gösteren programı fonksiyonlar yardımıyla oluşturunuz.(20 Puan)
"""
Kendisi hariç bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir.
"""

def  mükkemmel_sayi(sayi):
    bölüm= 1
    toplam=0
    while bölüm<sayi:
        if sayi%bölüm == 0:
            toplam=bölüm+toplam
        bölüm+=1
    if toplam == sayi:
        return True
    else:
        return False

print(mükkemmel_sayi(28))
