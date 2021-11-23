tab=[x for x in range (0,51)]
greater=[]
num=int(input('Enter the number: '))
if num>=max(tab):
    print('Nothing is greater in the given array')
elif num<=min(tab):
    print('Whole array is greater then the given number')
else:
    for i in range (num,max(tab)):
        greater.append(i)
    quantity=len(greater)
    print(f'There is/are {quantity} greater element(s)')

