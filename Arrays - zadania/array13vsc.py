tab=[8,2,5,1,9]    
def firstpower(array):
    first=''
    for x in range(0,len(array)):
        first+=str(f'{array[x]} ')
    return first
def secondpower(array):
    second=''
    for y in array:
        sec=y**2
        second+=str(f'{sec} ')
    return second
print('Array:',firstpower(tab))
print("Second power:",secondpower(tab))