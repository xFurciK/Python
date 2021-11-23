tab=[4,2,8,4,7,9,5]
smallest_largest=[]

def maxmin(array):
    smallest_largest.append(min(array))
    smallest_largest.append(max(array))
    return smallest_largest

print('Array:',tab)
print('Result:', maxmin(tab))






