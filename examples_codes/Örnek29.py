#kullanıcıdan n ve r olmak üzere iki sayı alan ve n’in r’li permütasyonlarının sayısını ekrana gösteren programı permutasyon() fonksiyonunu tanımlayarak oluşturunuz.(20 puan)

def fakt (sayi):
    carpim=1
    while sayi>0:
        carpim*=sayi
        sayi-=1
    return carpim
def perm(n,r):
    sonuc=(fakt(n)/(fakt(n-r)*fakt(r)))
    print(sonuc)



print("/","n","\\","\n","\\","r","/",sep="",end="")
n = int(input("\n\nn degerini giriniz :"))
r = int(input("r degerini giriniz :"))
perm(n,r)
