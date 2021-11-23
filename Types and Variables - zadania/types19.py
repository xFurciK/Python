print("Obliczanie pola trojkata, wzor Herona")
a=float(input("Prosze podac dlugosc boku a: "))
b=float(input("Prosze podac dlugosc boku b: "))
c=float(input("Prosze podac dlugosc boku c: "))
p=(a+b+c) * 1/2
pole=(p*(p-a)*(p-b)*(p-c))**(1/2)
print(f"Szukane pole wynosi {pole}")