names=['Genowefa','Onufry','Celestyna','Alojzy','Pankracy']
length=[]

for i in range(0,len(names)):
    quantity=len(names[i])
    length.append(quantity)
max_quantity=(length.index(max(length)))
names_index=names[max_quantity]

strarray=''
for j in names:
    strarray+=str(f'{j} ')


print('Names:',strarray)
print('Longest name:',names_index)








