'''verilen aralıktaki sayı asal mı değil mi
ercana sor bir aralık girilmesi isteme nasıl yapılır'''

sayi= 100

while sayi<=150:

    half=sayi//2
    asallık= True

    while sayi>1:
        if sayi%half==0:
            asallık=False
            break
        else:
            pass
            half-=1
    if asallık==True:
        print(sayi,"Asaldır")
    else:
        print(sayi, "Asal değildir")


