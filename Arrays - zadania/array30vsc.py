import random

tab=[x for x in range (0,100)]
def rand_elem(array):
    import random
    los_idx=random.randint(0,len(array))
    los_num=array[los_idx]
    return los_num

for i in range (3):
    print(rand_elem(tab),'',end='')