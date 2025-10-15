year=int(input("Enter the current year="))
y=int(input("Enter the final year="))
for i in range(year,y+1):
    if (i%4==0 and i%100!=0) or (i%400==0):
        print(f"{i} is a leap years")
