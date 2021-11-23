tab=[12,6,4,9,3,10]
def stars(n):
    return '*'*n

for i in tab:
    if i>=10:
        print(f'{i}: ',stars(i))
    else:
        print(f' {i}: ',stars(i))