faktoriyel = int(input("bir sayı giriniz: "))
AraToplam = faktoriyel

while faktoriyel-1 > 0:

    AraToplam=AraToplam*(faktoriyel-1)

    faktoriyel-=1
    
print(AraToplam)