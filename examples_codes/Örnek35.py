#girilen sayi ile 2 dahil arasindaki asal sayilari ekrana yazdiran program.

n = int(input("Sayi degeri giriniz :"))
bolen = n//2
kontrol = 0
while bolen >1:
    if n % bolen == 0:
        kontrol = 0
        bolen2 = bolen//2
        while bolen2 >1:
            if bolen % bolen2 ==0:
                kontrol+=5
            bolen2-=1
        if kontrol == 0:
            kontrol = 2
    if kontrol == 2:
        print(bolen)
    kontrol = 0
    bolen-=1



