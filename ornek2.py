from math import sin,pi



islem = input("isleminizi giriniz (+,-,/,*,sin(x)): ")

if islem == "+":
    a = float(input("1. sayiyi giriniz :"))
    b = float(input("2. sayiyi giriniz :"))
    print(a+b)
elif islem == "-":
    a = float(input("1. sayiyi giriniz :"))
    b = float(input("2. sayiyi giriniz :"))
    print(a-b)
elif islem == "*":
    a = float(input("1. sayiyi giriniz :"))
    b = float(input("2. sayiyi giriniz :"))
    print(a*b)
elif islem == "/":
    a = float(input("1. sayiyi giriniz :"))
    b = float(input("2. sayiyi giriniz :"))
    print(a/b)
elif (islem == "sin"):
    x = float(input("x derecesini giriniz :"))
    print(sin((x*pi)/180))
