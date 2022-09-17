#while ile faktoriyel hesaplama programi yaziniz.

def fakto(x):
    carpim=1
    while x >0:
        carpim*=x
        x-=1
    return carpim

kontrol = "evet"
while kontrol == "evet":

    deger = int(input("faktoriyei alınacak sayiyi giriniz :"))
    print(fakto(deger))
    kontrol = input("Tekrar deger girmek istiyor musunuz evet/hayir :")
    while kontrol != "evet" and kontrol != "hayir":
        print("\nHatali giris yaptiniz !!!")
        kontrol = input("Tekrar deger girmek istiyor musunuz evet/hayir :")
    if kontrol == "hayir":
        print("Program sonlandiriliyor...")