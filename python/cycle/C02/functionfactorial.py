def fact(n):
    if n==0 or n==1:
        return 1
    else:
      return n*fact(n-1)
n=int(input("Enter the numbers of elemnets="))
for i in range(1,n+1):
     print(f"factorial of {i} =",fact(i))