string = "You never get a second chance to make a first impression"
def how_many(letter):
    z = string.lower()
    x = z.count(f"{letter}")
    print(x)
how_many('e')
