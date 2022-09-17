#Üç basamaklı, basamaklarının küpleri toplamı kendisine eşit olan tamsayılara  Armstrong sayı  denir.Bunları ekrana yazdırınız.(15 puan)
baslama =100
while baslama < 1000:
    bir = baslama %10
    on = (baslama %100)//10
    yuz = baslama //100

    toplam = (bir **3)+(on **3) +(yuz **3)

    if toplam == baslama:
        print(baslama,"Armostrong sayidir")
        

    baslama+=1
