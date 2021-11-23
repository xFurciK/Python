def power(x,n):
    if x == 0 and n==0:
        return 'niezdefiniowane'
    elif n==0:
        return 1
    else:
        return x * power(x,n-1)
x=int(input("wprowadz liczbe ktora chcesz podniesc do potegi: "))
n=int(input("wprowadz potege do ktorej chcesz podniesc liczbe: "))

print(f"{x} do potegi {n} wynosi {power(x,n)}")
        