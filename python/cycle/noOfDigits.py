n = int(input("enter a number"))
num = abs(n)
count = 0
if num == 0:
    count = 1
else:
    while(num > 0):
        num = num // 10
        count += 1
print(count)


    