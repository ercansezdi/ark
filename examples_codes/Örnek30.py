# Fibonacci serisini ilk 15 terimini dizileri kullanarak ekrana yazdırın.  (0,1,1,2,3,5,8,13,21,34,55,… ) (20 puan)
import Örnek29.py

print("asd",Örnek30.fakt(5))



fibo =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fibo[0]=0
fibo[1]=1
i=0
while i<16:
    a=fibo[i]
    b=fibo[i+1]
    c = a+b
    fibo[i+2]=c
    print(fibo[i])
    
    i+=1

i=0
while i<15:
    print(fibo[i])
    i+=1

