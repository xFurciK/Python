file=open('task22.txt','w')
for i in range (1,11):
    second=i**2
    third=i**3
    file.write(f'{i},{second},{third}'+'\n')
file.close()

file=open('task22.txt')
print(file.read())
file.close()
