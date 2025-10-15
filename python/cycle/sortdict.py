data = {'banana': 3, 'apple': 5, 'orange': 2, 'mango': 4}

# Convert dict items to list of tuples
items = list(data.items())

# Bubble Sort (Ascending by key)
n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][0] > items[j + 1][0]:
            items[j], items[j + 1] = items[j + 1], items[j]

# Convert back to dict
sorted_dict_asc = {}
for key, value in items:
    sorted_dict_asc[key] = value

print("Ascending:", sorted_dict_asc)

#Descending order

# Bubble Sort (Descending by key)
n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        if items[j][0] < items[j + 1][0]:
            items[j], items[j + 1] = items[j + 1], items[j]

# Convert back to dict
sorted_dict_desc = {}
for key, value in items:
    sorted_dict_desc[key] = value

print("Descending:", sorted_dict_desc)
