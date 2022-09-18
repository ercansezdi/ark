kullanici_bilgileri = {"username":"trforever","passwd":73480}



k_adi = input("k_adi giriniz :")
sifre = int(input("şifre giriniz : "))



if (kullanici_bilgileri["username"] == k_adi):
    if (kullanici_bilgileri["passwd"] == sifre):
        print("Giris yapabilirsiniz ")
    else:
        print("Sektir get")
else:
    print("Kullanici adi yanlis")