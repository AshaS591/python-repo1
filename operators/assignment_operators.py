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

''' -= '''  
'''supports single valued datatype and set datatype(performs set difference)'''

'''-= on numbers '''
num1=10
num1-=5 # => num1=num1-5
print(num1) #5

'''-= in bool'''
fare=True # 1
fare-=1 # 1-1
print(fare) #0

''' -= on complex datatype'''
complex1=10+2j
complex1-=2+1j
print(complex1) #(8+1j)

set1={1,2,3,4}
set1-={2,5,6}
print(set1) #{1, 3, 4}