import datetime


class kac:
    def __init__(self):
        birthday = input("Doğum tarihinizi giriniz(gg.aa.yyyy) : ")

        time = datetime.datetime.today()

        birthday = datetime.datetime.strptime(birthday,"%d.%m.%Y")
        hour = int(datetime.datetime.strftime(time,"%H"))
        minute = int(datetime.datetime.strftime(time,"%M"))
        second = int(datetime.datetime.strftime(time,"%S"))

        yas = time - birthday
        genel = ((((int(yas.days)) * 24) * 60) * 60)
        print(type(hour))
        saat = (hour * 60 * 60)
        dakika = (minute * 60)
        saniye = second
        toplam_saniye = (genel + saat + dakika + saniye)

        print ( "{} saniye yaşadınız!!".format(toplam_saniye))


kac()