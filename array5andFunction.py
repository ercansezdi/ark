""" 3)Kullanıcıdan aldığı iki sayının ebob’unu bulan programı ebob() fonksiyonu tanımlayarak oluşturunuz.(15 Puan)
4)Kullanıcıdan aldığı iki sayının ekok’unu bulan programı ekok() fonksiyonu tanımlayarak oluşturunuz.(15 Puan)"""





def obeb(sayi1,sayi2):
    enB = 0
    counter = 1
    obeb_sayisi = -1
    if sayi1 > sayi2:
        enB = sayi1
    elif sayi2 > sayi1:
        enB = sayi2 
    else:
        return sayi1

    while counter <= enB:
        if sayi1 % counter == 0 and sayi2 % counter == 0:
            obeb_sayisi = counter
        counter += 1
    return obeb_sayisi
    
    
    
        
    
def okek(sayi1,sayi2): #ortak katlarin en kücügü
    if sayi1 > sayi2:
        bolum_sayisi = sayi1
    elif sayi2 > sayi1:
        bolum_sayisi = sayi2
    else:
        bolum_sayisi = sayi2

    while True:
        if  bolum_sayisi % sayi1 == 0 and  bolum_sayisi % sayi2 == 0:
            return  bolum_sayisi
        bolum_sayisi += 1
    
answer = obeb(1944,int(input("2. sayi gir amk :")))
print("OBEB :",answer)
answer = okek(5000,1298)
print("OKEK :",answer)
answer = obeb(25,50)
print("OBEB :",answer)
answer = okek(27,28)
print("OKEK :",answer)
answer = obeb(424,42424)
print("OBEB :",answer)
answer = okek(4242,27575)
print("OKEK :",answer)