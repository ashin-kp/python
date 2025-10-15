n=list(map(int,input("Enter the list of integers=").split()))
l=[]
for i in n:
    if i>100:
        l.append('over')
    else:
        l.append(i)
print(l)