
ad = str(input("Adinizi Giriniz :"))
soyad = str(input("Soyadnizi Giriniz :"))
not_ = int(input("Notunuzu Giriniz :"))
not_str = ""


if not_ >= 90:
    not_str = "AA"
elif not_ >= 80:
    not_str = "BA"
elif not_ >= 70:
    not_str = "BB" 
elif not_ >= 60:
    not_str = "CB"
elif not_ >= 50:
    not_str = "CC"
elif not_  >= 40:
    not_str = "CD"
else:
   not_str = "Okdugun mektebin amk"



print("Syn. ", ad," ", soyad," sinavdan aldiginiz not :",not_str)

