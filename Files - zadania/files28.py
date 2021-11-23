import re
with open('task28.txt') as file:
    content=file.read()
grades=re.findall('\d[.]\d',content)
suma=0
for i in grades:
    suma+=float(i)
arith=round(suma/len(grades),2)
print(arith)

