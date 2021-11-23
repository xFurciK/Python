tab1=[4,36,12,28,9,44,5]
tab2=[5,1,36]
tab3=[]
for i in tab1:
    x=tab2.count(i)
    if x==0:
        tab3.append(i)

strarray=''        
for j in tab3:
    strarray+=str(f'{j} ')
print(strarray,'or',tab3)


