from asyncio.windows_events import ERROR_CONNECTION_ABORTED
from random import randint
import math

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
    mutlakDeger = abs(Alınan_sayi-kura_sayısı)
    if 0<mutlakDeger<=3:
        print("yanıyosun fuat abi")
        hak-=1
        print("kalan hakkınız:",hak)
    elif 3<mutlakDeger<=5:
        print("çok sıcak")
        hak-=1
        print("kalan hakkınız:",hak)
    elif 5<mutlakDeger<=10:
        print("sıcak")
        hak-=1
        print("kalan hakkınız:",hak)
    elif 10<mutlakDeger<=20:
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