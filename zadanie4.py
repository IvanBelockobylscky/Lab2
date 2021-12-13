import math
print("Эта программа вычисляет косинус числа по формуле ряда Тейлора.")
x=int(input("Введите число x:"))
q=float(input("Введите число q:"))
while True:
    cos=1
    y=2
    k=-1
    n=0
    f=2
    sl=(math.pow(x,y)/math.factorial(f))
    cos+=sl*k
    y+=2
    f+=2
    k*=-1
    n+=1
    if math.fabs(sl)>q:
        print("Вычисленное нами значение=",cos)
        break

   
