def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
input_str = input("enter a string:")
result = char_frequency(input_str)
print("character frequency = ",result)