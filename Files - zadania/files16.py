file=open('stres.txt')
for i in range (5):
    print(file.readline())
for i in file:
    enter=str(input('Wcisnij Enter aby kontyunowac: '))
    if enter=='':
        print(i)
        for i in range (4):
            print(file.readline())
file.close()

            
