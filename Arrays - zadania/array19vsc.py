tab=[2,3,2,5,8,1,9,8]
unique_tab=[]
def array2str(array):
    strarray=''
    for i in array:
        strarray+=str(f'{i} ')
    return strarray

for i in tab:
    x=tab.count(i)
    if x==1:
        unique_tab.append(i)

print('Array:', array2str(tab))
print('Unique elements:', array2str(unique_tab))



