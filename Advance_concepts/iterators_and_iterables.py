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
    print(item)
# print(next(items)) #StopIteration
print(tuple(items)) #()

#print(next(new_items)) #'list' object is not an iterator

# class PrimeIter:
#     def __init__(self):
#         self.start=2
#     def __iter__(self):
#         return self
#     def __next__(self):
#         val=self.start
#         self.prime=True
#         for num in range(2,self.start):
#             if self.start%num==0:
#                 self.prime=False
#                 break
#         self.start+=1
#         if self.prime:
#             return val
        
        
# iter1=PrimeIter()
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))


# class PrimeIterator:
#     def __init__(self, max_num):
#         self.max_num = max_num
#         self.current_num = 2

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current_num > self.max_num:
#             raise StopIteration

#         while not self.is_prime(self.current_num):
#             self.current_num += 1

#         prime_num = self.current_num
#         self.current_num += 1
#         return prime_num

#     @staticmethod
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
# iter2=PrimeIterator(20)
# print(next(iter2))
# print(next(iter2))
# print(next(iter2))


class Prime:
    def __init__(self,max):
        self.start=2
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.max:
            raise StopIteration

        while not self.is_prime(self.start):
            self.start+=1
        prime_number=self.start
        self.start+=1
        return prime_number
    @staticmethod
    def is_prime(num):
        if num<2:
            return False
        for number in range(2,int(num**0.5)+1):
            if num%number==0:
                return False
        
        return True
iter3=Prime(20)
print(next(iter3))
print(next(iter3))







    

      
        


        