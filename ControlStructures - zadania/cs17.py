x = int(input("Podaj pierwsza wspolrzedna: "))
y = int(input("Podaj druga wspolrzedna: "))
print(f"x = {x}")
print(f"y = {y}")
if x > 0 and y >0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x==0 and y!=0:
    print(f"Point P({x},{y}) is located on the X axis")
elif y==0 and x!=0:
    print(f"Point P({x},{y}) is located on the Y axis")
else:
    print(f"Point P({x},{y}) is located at the beggining of the coordinate system")