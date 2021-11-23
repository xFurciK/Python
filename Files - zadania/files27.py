import re
file=open('task27.txt')
content=file.read()
atleast6=re.findall('[a-zA-Z]{6,}',content)
for i in atleast6:
    print(i)

