#1 ile girilen sayi arasindaki sayilarin tek tek tam bolenleri toplamini bulsun.
n = int(input("n degeri giriniz :"))

i = n
while i>0:
    toplam=0
    t=i
    while t>0:
        if i % t == 0:
            toplam+=t
        t-=1
    print(i,"sayisinin tam bolenleri toplami :",toplam)
    i-=1