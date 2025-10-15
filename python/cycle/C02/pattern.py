# right angle triangle
# n=int(input("Enter the numbers of rows="))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# reversed right angled triangle
# n = int(input("enter the no of rows:"))
# for i in range(n , 0 , -1):
#     for j in range(i):
#         print( j+1 , end="")
#     print()

# pyramid
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))

n = int(input("enter the no of rows:"))
for i in range(1,n+1):
    print(" "*(n-i) + "*" * (2 * i - 1))
for i in range(n-1 , 0 , -1):
    print(" "*(n-i) + "*" * (2 * i - 1))
