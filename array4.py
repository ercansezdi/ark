from random import randint

array = []



for i in range(0,20):
    array.append(randint(0,5))
print(array)
carpim_sayisi = 5
i = 0
while i < len(array):
    array[i] *= carpim_sayisi

    i += 1
print(array)
