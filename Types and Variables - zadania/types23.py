print("Obliczanie VAT")
amount = float(input("Prosze podac kwote: "))
VAT = (23/100) * amount
print(f"Amount = {amount}")
print(f"VAT =",round(VAT, 2))