n=int(input("enter the number of elements="))
a=int(input("enter the element to which the multiple to be found="))
print(f"Multiples of first {n} numbers of {a}=")
for i in range(1,n+1):
    print(a*i)
