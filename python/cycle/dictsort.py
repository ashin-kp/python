my_dict = {'b': 2, 'a': 5, 'c': 1}
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)

sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
print(sorted_by_keys_desc)
