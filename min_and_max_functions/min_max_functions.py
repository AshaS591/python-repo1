#min and max functions

#1.finding max among three numbers
num1=90
num2=10
num3=60
print(max(num1,num2,num3))

#2.finding max among three floating numbers
num1=9.99
num2=10
num3=9.9
print(max(num1,num2,num3))

#3.finding max among two complex numbers
# num1=9+0j
# num2=10+9j
# num3=9.9+7j
# print(max(num1,num2,num3)) complex does not supports max fun^n

#4.finding max among three characters
char1='n'
char2='N'
char3='Z'
print(max(char1,char2,char3))

#5.finding max among three strings(checks ascii value of characters)
str1='asha'
str2='appa'
str3='family'
print(max(str1,str2,str3))

str1='a6578a'
str2='a7990a'
str3='@#&'
print(max(str1,str2,str3))

#6.finding max char in a string
str1='max char'
print(max(str1))

district='kolar'
print(max(district))

#7.finding max element in a list (homogeneous list)
names=['asha','haripriya','anu','shashi','chandu']
print(max(names))

#8.finding max char in element in a list (homogeneous list)
sections=['5cse11','8cse09','7cse01','2cse06']
print(max(sections[1]))

#9.finding max element in a list (heterogeneous list)
elements=[10,29.80,True,False]
print(max(elements)) #support for only single valued datatype

