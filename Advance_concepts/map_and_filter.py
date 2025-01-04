''' Map function to find cube of each number of a collection'''
def cube(num):
    return num**3
nums=[10,20,21,90,15]
res=map(cube,nums)
print(next(res))

''' map function to find square of each number of a collection'''
numbers=[2,3,4,5,9]
res=map(lambda num:num**2,numbers)
print(list(res))

''' map function to find factorial of each number of a collection'''

numbers=[2,3,5,6]
from math import factorial
res=map(factorial,numbers)
for num in res:
    print(num)

'''wap to return ascii value of first character in each name using map function'''
names=['asha','suki','bhavani','shashi']
res=map(lambda name:ord(name[0]),names)
print(list(res))

'''wap to return reverse of name of each item in a collection using map function'''
names=['asha','suki','bhavani','shashi']
res=map(lambda name:name[::-1],names)
print(list(res))

''' wap to get vowels from each name in a collection using map function'''
cities=['kolar','bengaluru','delhi','mysore']
def get_vowels(city):
    vowels=''
    for char in city:
        if char in 'aeiouAEIOU':
            vowels+=char
    return vowels
res=map(get_vowels,cities)
print(list(res))

'''wap to find square root of each number in a collection using map function'''
numbers=[2,8,4,9,12,16]
res=map(lambda num:num**0.5,numbers)
print(list(res))

# or

def sq_root(num):
    return num**0.5
res=map(sq_root,numbers)
print(list(res))

'''wap to return the last item of nested collection if the length is morethan 3 else return first item from ollection using map function'''
collections=[(10,40),'lion',['hi','bye'],'python',[1,2,3,4,5]]
res=map(lambda collection:collection[-1] if len(collection)>3 else collection[0],collections)
for item in res:
    print(item)