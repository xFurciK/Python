a = int(input("podaj a: "))
b = int(input("podaj b: "))
print('*' * b)
for i in range(a-2):
    print("*" + " " * (b-2) + "*")
print("*" * b)