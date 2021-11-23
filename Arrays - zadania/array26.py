tab1=[x for x in range (1,10)]
even_odd=[]
for i in tab1:
    if i%2==0:
        even_odd.append(i)
for j in tab1:
    if j%2!=0:
        even_odd.append(j)



print(even_odd)
