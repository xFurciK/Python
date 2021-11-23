x = 0
y = 1
n = int(input("enter n: "))
for z in range(n):
    print(x+y)
    x+=y
    print(y+x)
    y+=x
