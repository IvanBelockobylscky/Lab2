a=int(input("Vvedite peremennuyu a:"))
b=int(input("Vvedite peremennuyu b:"))
c=int(input("Vvedite peremennuyu c:"))
D=b**2-4*a*c
if(D>0):
    x1=(-b+D**(1/2))/2*a
    x2=(-b-D**(1/2))/2*a
    print("Vashi korni, sir: x1=",x1,",x2=",x2)
elif(D==0):
    x=-b/2*a
    print("Vash koren', sir: x=",x)
else:
    D=complex(D)
    x1=(-b+D**(1/2))/2*a
    x2=(-b-D**(1/2))/2*a
    print("Vashi complexnie korni, sir: x1=",x1,",x2=",x2)
    
