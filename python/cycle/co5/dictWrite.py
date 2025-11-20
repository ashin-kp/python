import csv
data  = [
    {"name":"merly","age":20},
    {"name":"smija","age":30}
]
with open("output.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age"])
    for row in data:
        writer.writerow([row["name"],row["age"]])

with open("output.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
