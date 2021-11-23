import re
text = 'To be, or not to be, that is the question'
vowels=re.findall('[aeiou]',text)
print('Number of vowels in text: ', len(vowels))
