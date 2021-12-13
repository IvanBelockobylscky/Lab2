from math import sqrt
a=float(input("Vvedite 1-e veschestvennoe chislo:"))
b=float(input("Vvedite 2-e veschestvennoe chislo:"))
if(a<0)or(b<0):
        print("Error")
elif(b<a):
        print("Kvadratniyiy koren' menschego chisla:",sqrt(b))
elif(a<b):
        print("Kvadratniyiy koren' menschego chisla:",sqrt(a))
else:
        print("Derzji oba:",sqrt(a),sqrt(b))
k=0
a=int(input("Vvedite chislo ot 1 do 10000:"))
while 1<a<10000:
    for i in range(1,a+1):
        if a%i==0:
            if i!=a and i%2:
                print(str(i))
            if i==a and i%2:
                print(str(i))
            k+=1
    break
else:
    print("Chitai vnimatel'nee uslovie")

