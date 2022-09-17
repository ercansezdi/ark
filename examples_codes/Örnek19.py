#1den 1000e kadar 5 ile bolunup 7 ile bolunemeyen sayilari sayan toplamlarını hesaplayan bu sayilari listeleyen programi yaziniz,
i=1
toplam=1
while i<=1000:
    if i%5 == 0 and i%7 !=0:
        print(i,"sayisi sarti saglar.")
        toplam+=i
    i+=1

print("\nSarti saglayan sayilar toplami =",toplam)
