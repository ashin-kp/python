list = []
n = int(input("enter the no of colours"))
for i in range(n):
    item = input("enter a colour")
    list.append(item)
print(list)
print("first color in list=",list[0])
print("last color in list=",list[-1])
