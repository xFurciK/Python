n = int(input("Enter N: "))

for n in range (n+1):
    if n > 1:
        for i in range (2, n):
            if (n % i) == 0:
                break
        else:
            print(n)