k=int(input("Введите кол-во слагаемых:"))
p=1
n=3
while k>0:
    for i in range(k-1):
        if i%2==0:
            p=p-1/n
        else:
            p=p+1/n
        n+=2
    print("Приближенное значение числа пи:",p*4)
    break
else:
    print("Ошибка ввода.")

   
