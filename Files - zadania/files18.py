file1=open('randomtext.txt')
filecopy=open('copy.txt','w')
for line in file1:
    filecopy.write(line)
filecopy.close()

filecopy=open('copy.txt')
print(filecopy.read())
