# s=input("Enter the line of text:").split()

# count=0
# for i in word:
#     i=s
#     if i==word:
#         count=count+1
# print(f"Number of occurence{word}=",count)

text = "this is this is a text of text"
words = text.split()
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
for word in unique:
     print(word,":",words.count(word))