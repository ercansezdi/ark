from cgi import print_arguments
import re


resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]

from random import randint
kelimeler = ["ankara","konya","istanbul","hakkari","izmir"]
kelime = kelimeler[randint(0,len(kelimeler)-1)]
tahmin_harfleri = []
for i in kelime:
    tahmin_harfleri.append("_")

tahmin_sayisi = 0

while True:
    print(tahmin_harfleri)
    tahmin_harfi = input("tahmin giriniz :")

    if tahmin_harfi in kelime:
        index =0 
        for i in kelime:
            if i == tahmin_harfi:
                tahmin_harfleri[index] = tahmin_harfi
            index += 1
    else:
        print(resim[tahmin_sayisi])
        tahmin_sayisi += 1


    if tahmin_sayisi == len(resim)  :
        print(tahmin_harfleri)
        print("Oyunu Kaybettiniz")
        break
    if not "_" in tahmin_harfleri:
        print(tahmin_harfleri)
        print("Oyunu Kazandin.")
        break