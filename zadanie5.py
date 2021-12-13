N=int(input("Введите натуральное число:"))
print("Комбинации натуральных чисел:")
s=0
for x in range(N):
    if x**3>N:
        break
    for y in range(N):
        if y**3+x**3>N:
            break
        for z in range(N):
            if y**3+x**3+z**3>N:
                break
            if x**3+y**3+z**3==N:
                print("x =",x,"y =",y,"z =",z)
                s+=1
if s==0:
    print('No such combinations')
