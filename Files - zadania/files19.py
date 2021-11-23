file1=open('MeatAndFish.txt')
file2=open('GrainsAndBread.txt')

file3=open('shoppinglist.txt','w')
for line in file1:
    file3.write(line)
file3.close()
file3=open('shoppinglist.txt','a')
for lines in file2:
    file3.write(lines)
file3.close()

file3=open('shoppinglist.txt')
print(file3.read())

