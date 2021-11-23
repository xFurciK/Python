tab1=[2,8,3,'banan','cukierek','banan']
tab=['banan',3,8]
x=0
for j in tab:
    for i in tab1:
        if j==i:
            x+=1
        else:
            x+=0
length=len(tab)
if x>=length:
    print('subset')
else:
    print('no subset')
