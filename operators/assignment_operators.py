''' Assignment Operators '''

'''+= on numbers'''
num=10
num+=30 # =>num=num+10
print(num) #40

num2=9.9
num2+=2.8
print(num2) #12.7

'''+= on strings'''
name='Asha'
name+=' S' #performs concatenation
print(name) #=>Asha S

'''+= on list'''
names=['asha','shashi','abhi']
names+=['arya'] #performs concatenation
print(names) #['asha', 'shashi', 'abhi', 'arya'] 

'''+= on tuple'''
numbers=(10,20,90)
numbers+=(30,70) #performs concatenation
print(numbers) #(10, 20, 90, 30, 70)

