
def furkan_ercan(sayi):
    return sayi + 94

def kare_al(sayi):
    kare = sayi*sayi
    print(kare)

    return [50,25,"25",True]
#furkan_ercan(30,31)


def recursive(sayi): #Özyineleme fonksiyon
    print("icerdeyim :",sayi)
    sayi -= 1
    if sayi > 0:
        return recursive(sayi)
    else:
        return furkan_ercan(sayi)

cevap = recursive(5)
print("ciktim" ,cevap)