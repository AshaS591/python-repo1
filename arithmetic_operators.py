# arithmetic operators on integer numbers
num1=20
num2=90
res=num1+num2
print('sum is ',res)
res=num1-num2
print('difference is ',res)
res=num1*num2
print('product is ',res)
res=num1/num2
print('division res is ',res)
res=num1//num2
print('floor res is ',res)
n=3
res=num1**n
print('power of res is ',res)
res=num1%num2
print('modulo res is ',res)

##########################################################################

# arithmetic operators on float numbers
num1=79.99
num2=5.5
res=num1+num2
print('sum is ',res)
res=num1-num2
print('difference is ',res)
res=num1*num2
print('product is ',res)
res=num1/num2
print('division res is ',res)
res=num1//num2
print('floor res is ',res)
n=3
res=num1**n
print('power of res is ',res)
res=num1%num2
print('modulo res is ',res)

##########################################################################

# arithmetic operators on collections(supports +,*)
# + performs concatenation on strings
quote='old friends are like a gold and new friend are like a diamonds'
complete_quote=quote+" Don't forget old friends when you get new friends because only gold can hold a diamond"
print(complete_quote.title())

##########################################################################

# * represents no of occurances of a string ,
# it works only when one operand is number and other is collection
word='hello medam '
word=word*4
print(word)

##########################################################################

# same on list also
l1=['amar','20',90,'cse0787','hello']
l2=[20,'hey','old lady','playground']
l1=l1+l2
print(l1)

l1=l1*2
print(l1)

##########################################################################

# same on tuple also
tup=(10,'20','30',20,30)
tup1=('90',80,45)
tup=tup+tup1
print(tup)
tup=tup*2
print(tup)

##########################################################################

'''dic={1:'asha',2:'anu'}
dict2={3:'arya',4:'mary'}  dictionary doesn't support any arithmetic operator
dic=dic+dict2
print(dic)'''

##########################################################################

#set supports only - operator which performs set difference
set1={1,2,'asha'}
set2={9,0,3,1}
set1=set1-set2
print(set1)