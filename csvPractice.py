import csv

with open("data/menu.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

for row in reader: 
    price = int(row[2])
    print(price+5)
    
