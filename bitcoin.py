'''eğer bitcoin 30000 den küçükse al, değilse bekle'''

bitcoin=int(input("bitcoin value :"))
if bitcoin <= 30000 :
    print("take it")
elif 30000<bitcoin<=35000 :
    print("dont be idiot, just wait a bit")
else :
    print("wait for deals")