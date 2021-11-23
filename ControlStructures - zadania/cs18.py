kwota = int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {kwota} in coins: ")
ilosc_piatek = kwota // 5
jeden = kwota - ilosc_piatek*5
ilosc_dwojek = jeden // 2
dwa = kwota - ilosc_piatek*5 - ilosc_dwojek*2
ilosc_jedynek = dwa // 1
print(f"5 zł = {ilosc_piatek}")
print(f"2 zł = {ilosc_dwojek}")
print(f"1 zł = {ilosc_jedynek}")