from random import randint
a = ["şeftali","armut","elma","karpuz","kavun","kiraz"]
print(a[4])
b = []

kullanılacak_sayı = 1

while kullanılacak_sayı > 0:
    kura_sayısı = randint(0,5)
    b.append(kura_sayısı)
    kullanılacak_sayı -= 1
print(b)
