lists=[1,2,3,4,5]
print(lists)
l=[]
for i in lists:
    if i%2!=0:
        l.append(i)
print("List after removing even numbers=",l)