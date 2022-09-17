#Kullanıcıdan eşkenar üçgenin yüksekliğini isteyen ve bu eşkenar üçgenin alanını ekrana yazan programı fonksiyonlar yardımıyla oluşturunuz.(15 Puan)

def alan(yuksek):
    kokuc=3**(0.5)
    kenar=(yukseklik*2)/kokuc

    alandegeri=(kenar*kenar)*kokuc/4

    return alandegeri


yukseklik=int(input("yukseklik degerini giriniz :"))

print("Yüksekliği girilen üçgenin alanı :",alan(yukseklik))

