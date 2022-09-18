from random import randint
array2 = [10]
array = [10,5.5,"ercan",'b']


i = 10
while i > 0:
    random_sayi = randint(0,100)
    array.append(random_sayi)
    i -= 1
#['append', 'clear', 'copy', 'count', 'extend', 'index','insert', 'pop', 'remove', 'reverse', 'sort']
print(array)
for gez in range(0,10):
    random_sayi = randint(0,10)
    array2.append(random_sayi)
print(array2)
array2.append(5.5)
print(array2)
print(array2.index(5.5))
print(array2.count(3))
array2.sort(reverse=False)
print(array2)

