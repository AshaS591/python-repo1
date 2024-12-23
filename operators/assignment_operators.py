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
set1-={2,5,6} # => set1=set1-set2
print(set1) #{1, 3, 4}

############################################################################################

""" *= """

''' *= on numbers '''

num1=10
num1*=20 # =>num1=num1*20
print(num1) #200

''' *= on complex numbers '''

complex1=2+3j
complex1*=2 # =>complex1=complaex1*2
print(complex1) #(4+6j)

''' *= on bool'''
fare=True
fare*=False # 1*0=0
print(fare) #0

''' *= on strings'''
name='Asha S '
name*=5 # second operand must be number which represents number of occurances of a string 
print(name) #Asha S Asha S Asha S Asha S Asha S

''' *= on list'''
list1=[10,20,30]
#list1*=[20,30] #can't multiply sequence by non-int of type 'list'

list1*=2  # second operand must be number which represents number of occurances of an elements
print(list1) #[10, 20, 30, 10, 20, 30]


''' *= on tuple '''
tuple1=(9,10)
# tuple1*=(2,5) TypeError: can't multiply sequence by non-int of type 'tuple'

tuple1*=2
print(tuple1) #(9, 10, 9, 10)

dict1={'a':10,'b':20}
#dict1*=2 unsupported operand type(s) for *=: 'dict' and 'int'
#dict1*={'c':90} TypeError: unsupported operand type(s) for *=: 'dict' and 'dict'
print(dict1)