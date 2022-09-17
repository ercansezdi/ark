# 2.Klavyeden 1 ile 4 arasında bir değer alınız. Girilen değere göre mevsimleri ekrana yazan programı yazınız. (1-İlkbahar, 2-Yaz, 3-Sonbahar, 4-Kış) (10 Puan)
sayi = int(input("Sayi degeri giriniz :"))

if sayi == 1:
    print("Ilkbahar.")
elif sayi == 2:
    print("Yaz.")
elif sayi == 3:
    print("Sonbahar.")
elif sayi == 4:
    print("Kıs")
else:
    print("Hatali giris.")
    
