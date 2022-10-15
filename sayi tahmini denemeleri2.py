from random import randint
#tahmin sayısına yaklaştıkça sıcak soğuk şeklinde yazdırsın
hak=10
kura_sayısı=randint(0,100)
kullanıcı_tahminleri=[]
print("toplam hakkınız:",hak)
print(kura_sayısı)

while True:
    Alınan_sayi=int(input("lütfen bir sayı giriniz:"))
    kullanıcı_tahminleri.append(Alınan_sayi)
    print(kullanıcı_tahminleri)

    if Alınan_sayi>kura_sayısı:
        if 0<Alınan_sayi-kura_sayısı<=3:
            print("yanıyosun fuat abi")
            hak-=1
            print("kalan hakkınız:",hak)
        elif 3<Alınan_sayi-kura_sayısı<=5:
            print("çok sıcak")
            hak-=1
            print("kalan hakkınız:",hak)
        elif 5<Alınan_sayi-kura_sayısı<=10:
            print("sıcak")
            hak-=1
            print("kalan hakkınız:",hak)
        elif 10<Alınan_sayi-kura_sayısı<=20:
            print("soğuk")
            hak-=1
            print("kalan hakkınız:",hak)
        else:
            print("buz gibi")
            hak-=1
            print("kalan hakkınız:",hak)
        if hak==0:
            print("kaybettiniz")
            break
        elif Alınan_sayi==kura_sayısı:
            print("tebrikler doğru tahmin")
            break
    elif Alınan_sayi<kura_sayısı:

        if 0<kura_sayısı-Alınan_sayi<=3:
            print("yanıyosun fuat abi")
            hak-=1
            print("kalan hakkınız:",hak)
        elif 3<kura_sayısı-Alınan_sayi<=5:
            print("çok sıcak")
            hak-=1
            print("kalan hakkınız:",hak)
        elif 5<kura_sayısı-Alınan_sayi<=10:
            print("sıcak")
            hak-=1
            print("kalan hakkınız:",hak)
        elif 10<kura_sayısı-Alınan_sayi<=20:
            print("soğuk")
            hak-=1
            print("kalan hakkınız:",hak)
        else:
            print("buz gibi")
            hak-=1
            print("kalan hakkınız:",hak)
        if hak==0:
            print("kaybettiniz")
            break
        elif Alınan_sayi==kura_sayısı:
            print("tebrikler doğru tahmin")
            break
    else:
        print("müneccim mübarek")
        break
