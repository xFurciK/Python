name=input('Podaj nazwe pliku z roszerzeniem: ')
file=open(f'{name}')
ilosc_linii=0
for line in file:
    ilosc_linii+=1

print(f"File name: {name}")
print(f'Number of lines: {ilosc_linii}')