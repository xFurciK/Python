import csv

file=open('task23.txt')
csv_reader=csv.reader(file)
header=next(csv_reader)
for row in csv_reader:
    if int(row[2])<30:
        print(row[0], row[1], row[4])





