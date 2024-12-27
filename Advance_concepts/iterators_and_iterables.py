''' Iterables '''

''' All collections in python are iterables(are objects) whose classes have implementation to __iter__ method and these can be used any number of times in loops'''

colors=['black','red','orange','white'] # object of class list
print(dir(colors))

animals=('lion','tiger','elephant','gorilla')# object of class tuple
print(dir(animals))

numbers={1,5,6,7,8,9,1,4,2,3} # object of class set
print(dir(numbers))

word='Euphoria' # object of class str
print(dir(word))

emp_info={'name':'asha','roll_no':787,'dob':'14/01/2002'}# object of class dict
print(dir(emp_info))

""" Iterators """

''' Iterator is an object which has implementation to iterator protocol '''

''' 1. __iter__ and __next__ method together called iterator protocol

    2. there is no predefined iterators whenever needed we have to create one

    3. to look into the elements of an iterators ,we can use the following 3 ways
       i.by using iter and next functions 
       ii.by using iterator in for loop
       iii.by typecasting an iterator
    
    '''

''' iter function is used to create an iterator which takes iterable as an argument'''

colors=['black','red','orange','white']
items=iter(colors)  #we can use iterator only once
# print(items) #we get address
# print(next(items)) # gives one item at a time
# print(next(items))
# print(next(items))
# print(next(items)) # once its reaches to last element if use next method again it raises an exception i.e stop iteration

# for item in items:
#     print(item)
# print(next(items))# once its reaches to last element if use next method again it raises an exception i.e stop iteration

new_items=list(items)
print(new_items)
for item in new_items:
    print(new_items)


#print(next(new_items)) #'list' object is not an iterator

