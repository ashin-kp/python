def ingfy(str):
    if str.endswith("ing"):
        return str+"ly"
    return str+"ing"
input_str=input("Enter the string=")
print(ingfy(input_str))