n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
print("choose operation:")
print("1:addition")
print("2:substration")
print("3:multiplication")
print("4:division")
print("5:floor division")
print("6:modulus")
print("7:exponent")

choice = int(input("enter a choice 1-7"))
if choice == 1:
    print("addition =",n1+n1)
elif choice == 2:
    print("substraction =",n1-n1)
elif choice == 3:
    print("multiplication =",n1*n1)
elif choice == 4:
    print("division =",n1/n1)
elif choice == 5:
    print("floor division =",n1//n1)
elif choice == 6:
    print("modulus =",n1%n1)
elif choice == 7:
    print("exponent =",n1**n1)
else:
    print("invalid choice")