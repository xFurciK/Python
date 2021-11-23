import random
file=open('task21.txt','w')
for i in range (50):
    num=random.randint(100,999)
    file.write(f'{num}' + '\n')
file.close()

