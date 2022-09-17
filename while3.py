
i = 3 



while i < 99:

    half = i // 2 
    asalik = True
    while half > 1:
        if i % half == 0:
            asalik = False
            break
        else:
            pass
        half -= 1 

    if asalik == True:
        print(i, " Asaldir.")
    else:
        print(i, "Asal degildir.")


    """
    if (i % half == 0):
        print(i, "Asal degil")
    else:
        print(i, "asaldir")
    """

    i += 1