tab=[15, 38, 7, 23, 14]
def occurs(number,array):
    for x in array:
        if number==x:
            return True

num=int(input("Enter the number: "))

def str2array(array):
    strarray=''
    for i in array:
        strarray+=str(f'{i} ')
    return strarray

print(f"Number: {num}")
print("Array: ", str2array(tab))
if occurs(num,tab)==True:
    print(f'Result: number {num} appears in the array')
else:
    print(f'Result: number {num} does not appear in the array')
