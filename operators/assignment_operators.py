''' Assignment Operators '''
""" += ,-= ,*= ,/= ,%= ,//= """

'''+= on numbers'''

'''int'''
num=10
num+=30 # =>num=num+10
print(num) #40

'''float'''
num2=9.9
num2+=2.8
print(num2) #12.7

'''complex'''
complex1=2+3j
complex1+=1+9j
print(complex1) #(3+12j)

'''bool'''
truth=True #True =>1 and False =>0
truth+=False  # 1+0 => 1
print(truth) # 1

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

'''+= on dictionary'''
info={'name':'asha'}
# info+={'age':21}
# print(info) unsupported operand type(s) for +=: 'dict' and 'dict'

'''+= on set'''
set1={12,23}
# set1+={4,5}
# print(set1)  unsupported operand type(s) for +=: 'set' and 'set'

##############################################################################################