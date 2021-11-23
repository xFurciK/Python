import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
inttemp=[]
for i in temperatures:
    inttemp.append(int(i))
suma=0
for temp in inttemp:
    suma+=temp
average_temp=(suma)/(len(inttemp))
print(f'Srednia temperatura wynosi {average_temp}C')


