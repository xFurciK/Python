count = 0
i = 1
sum = 0
while i != 0:
    i = int(input("Enter the number: "))
    count += 1
    sum += i
    ilosc = count -1
    if i!=0:
        continue
    else:
        mean = sum / ilosc
print(f"RESULT: Quantity={ilosc}, Sum={sum}, Mean={mean}")


    
    
    