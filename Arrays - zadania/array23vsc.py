tab1=[1,0,9,4,6]
tab2=[6,8,3,1,0,5,7]
tab3=[2,3,10,19,6,8]

def median(array):
    if len(array)%2!=0:
        a=int((len(array)-1)/2)
        for i in range (0,a):
            array.pop(0)
        for j in range (0,a):
            array.pop(-1)
        return array[0]
    else:
        b=int((len(array)/2)-1)
        for x in range (0,b):
            array.pop(0)
        for y in range (0,b):
            array.pop(-1)
        med=(array[0]+array[1])/2
        if med%2==0:
            return int(med)
        else:
            return med

print("Mediana wynosi",median(tab1)) 


