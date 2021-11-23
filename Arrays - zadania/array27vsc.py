tab=[2,5,7,9,5,6]
def przecinki(array):
    strarray=''
    last=array[-1]
    array.pop(-1)
    for i in array:
        strarray+=str(f'{i}, ')
    zdanie=str(f'{strarray}{last}')
    return zdanie

print("Array:",tab)
print("String:",przecinki(tab))
