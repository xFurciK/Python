tab=[2,2,2,5,5,5,3,3,3]
def bubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

print(bubblesort(tab))




