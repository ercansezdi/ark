
from random import randint
sayi_grubu1=[]

sayi_grubu2=[2,4,6,8]

Sehirler=["adana","istanbul","izmir","muş"]

istenen_sayi_miktari = 5

while istenen_sayi_miktari > 0:   #0 ile 100 arasında rastgele 5 sayı veriyor
    rastgele_sayi = randint(0,100)
    sayi_grubu1.append(rastgele_sayi)
    istenen_sayi_miktari -= 1
print(sayi_grubu1)

for i in range(0,5):           #bize 0 ile 10 arasında rastgele 5 sayı veriyo ve sayi_grubu2'ye ekliyor
    rastgele_sayi= randint(0,10)
    sayi_grubu2.append(rastgele_sayi)
sayi_grubu2.append("rasgele sayılar bunlar")
print(sayi_grubu2)

print(sayi_grubu2.index(8))    #8 sayısının indexte kaçıncı sırada olduğunu gösteriyor. yani 3

print(Sehirler.count("adana"))  #sehirler grubunda kaç adet adana var onu sayıyor(ercana sor harf harf nasıl aldırtırım)

print(Sehirler.count("a"))
#ercana reverse i tekrar anlattır!!
#['append', 'clear', 'copy', 'count', 'extend', 'index','insert', 'pop', 'remove', 'reverse', 'sort']


