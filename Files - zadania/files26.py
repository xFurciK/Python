# Without RegularExpressions
text = 'To be, or not to be, that is the question'
tab1=[]
tab1=text.split(' ')
print('Amount of words:',len(tab1))

#With RegEx
import re
words=re.findall('\w+',text)
print('Amount of words counted with RegEx:',len(words))