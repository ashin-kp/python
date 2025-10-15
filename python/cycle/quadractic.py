import math
a=int(input("Enter number"))
b=int(input("Enter number"))
c=int(input("Enter number"))
d=b**2-4*a*c
if d==0:
    print("One real root exist")
    root=-b/(2*a)
    print("Root=",root)
elif d>0:
    print("2 real roots exist")
    root1=(-b+(math.sqrt(d)))/(2*a)
    root2=(-b-(math.sqrt(d)))/(2*a)
    print("Root1=",root1)
    print("Root2=",root2)
else:
    print("complex roots exist")
    real=-b/(2*a)
    imag=(math.sqrt(-d))/(2*a)
    root1=complex(real,imag)
    root2=complex(real,-imag)
    print("Root1=",root1)
    print("Root2=",root2)
    


