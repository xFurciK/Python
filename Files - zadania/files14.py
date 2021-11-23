with open("randomtext.txt") as file:
    content=file.read()
for line in content:
    print(line, end="")
file.close()
