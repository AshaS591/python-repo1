''' Map function to find cube of each number of a collection'''
def cube(num):
    return num**3
nums=[10,20,21,90,15]
res=map(cube,nums)
print(next(res))

''' map function to find square of each number of a coolection'''
numbers=[2,3,4,5,9]
res=map(lambda num:num**2,numbers)
print(list(res))

''' map function to find factorial of each number of a coolection'''

numbers=[2,3,5,6]
from math import factorial
res=map(factorial,numbers)
for num in res:
    print(num)
