tab=[15,8,31,47,2,19]
def existed(array):
    ex=""
    for i in range(0,len(array)):
        ex+=str(f'{array[i]} ')
    return ex

def reverse(array):
    rev=""
    for i in range(len(array),0,-1):
        rev+=str(f'{array[i-1]} ')
    return rev

print('existed array: ',existed(tab))
print('reverse array: ',reverse(tab))
