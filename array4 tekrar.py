from random import randint

tckimlikno = []

for i in range(0,11):
    tckimlikno.append(randint(0,9))
 
print(tckimlikno)

a = 0

while a < len(tckimlikno):
    tckimlikno[a] *= 5
    a += 1
print(tckimlikno)

