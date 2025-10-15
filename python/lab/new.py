n = int(input("enter a limit"))
s = []
for i in range(n):
    a = int(input("enter number"))
    s.append(a)
newList = []
for x in s:
    if x > 100:
        newList.append('over')
    else:
        newList.append(x)
print(newList)