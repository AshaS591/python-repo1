import re

''' 1. ? -> 0 or 1 time occurance of char '''

string='hello my name is asha or asa'
pattern='ash?a'
result=re.findall(pattern,string)
print(result)

string='pink is a color or colour'
pattern='colou?r'
result=re.findall(pattern,string)
print(result)

''' 2. [] - > char set (one character ata time) '''

string=' i got 99 out of 100 in maths'
pattern='[0-9]+'
result=re.findall(pattern,string)
print(result)

string='i am 2024 passed out batch with 87 percent'
pattern='[0-9]+'
result=re.findall(pattern,string)
print(result)

''' 3. + one or more characters '''

string='hey stop there,heyyy i am coming...'
pattern='hey+'
result=re.findall(pattern,string)
print(result)

string='hello hellllo...'
pattern='hell+o'
result=re.findall(pattern,string)
print(result)

''' 4. . - > any character '''

string='hey stop there,heyyy i am coming...'
pattern='i.'
result=re.findall(pattern,string)
print(result)

string='hey stop there,heyyy i am coming...'
pattern='hey.'
result=re.findall(pattern,string)
print(result)

''' 5. [^characters] negation of a char set'''

string='hey stop there,heyyy i am coming...'
pattern='[^aeiou\W]' #except vowels
result=re.findall(pattern,string)
print(result)

string='hey stop there,heyyy i am coming...'
pattern='[^\s]'
result=re.findall(pattern,string)
print(result)

''' 6. ^[characters] startswith'''

string='hey stop there,heyyy i am coming...'
pattern='^hey'
result=re.findall(pattern,string)
print(result)

string='my name is asha'
pattern='^asha'
result=re.findall(pattern,string)
print(result)

''' 7. $ -> endswith '''

string='my name is asha and my father call me shashi'
pattern='shashi$'
result=re.findall(pattern,string)
print(result)

string='hey stop there,heyyy i am coming...'
pattern='coming..$'
result=re.findall(pattern,string)
print(result)