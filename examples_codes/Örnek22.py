"""
// 6- Kullanıcıdan adını,soyadını,yaşını alınız.Eğer yaşı 18'den büyükse “Oy kullanabilirsiniz” yazsın.Eğer yaşı 18'den küçükse “Yaşınız tutmuyor” yazsın 
//ve Oy kullanabilirsiniz yazana kadar kullanıcının yaşını üçer üçer arttırsın.(20 puan)

"""
ad = input("Adınızı giriniz :")
soyad = input("Soyadinizi giriniz :")
yas = int(input("Yasinizi giriniz :"))

if yas >=18:
    print("Syn",ad," ",soyad,"oy kullanabilirsiniz.")
    
else:
    while yas <=18:
        yas+=3
        print(yas)
        if yas >=18:
            print("Syn",ad," ",soyad,"oy kullanabilirsiniz.")
