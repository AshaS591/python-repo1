
''' Custom Class Iterators'''

''' 1 '''
class Add:
    def __init__(self,collection,num):
        self.collection=collection
        self.num=num
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.collection):
            value=self.collection[self.index]+self.num
            self.index+=1
            return value
        else:
            raise StopIteration
items=[23,4,58,9,1]
num=20
obj=Add(items,num)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
# print(next(obj)) StopIteration

''' 2. '''
class Multiply:
    def __init__(self,collection,num):
        self.collection=collection
        self.num=num
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.collection):
            value=self.collection[self.index]*self.num
            self.index+=1
            return value
        else:
            raise f'No Number to multiply'
items=[23,4,58,9,1]
num=20
obj=Add(items,num)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
# print(next(obj)) StopIteration

''' 3. '''
class Nums:
    def __init__(self,collection,num):
        self.collection=collection
        self.num=num
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):

        if self.index<len(self.collection):
            value=self.collection[self.index]+self.index
            self.index+=1
            return value
        
        else:
            raise StopIteration
        
items=[23,4,58,9,1]
num=20
obj=Add(items,num)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
# print(next(obj)) StopIteration


class prime_inf:
    def __init__(self):
        self.num=2
    def __iter__(self):
        return self
    def __next__(self):
       
        while True:
            for num in range(2,int(self.num**0.5)+1):
                if self.num%num==0:
                    break
            else:
                
                value=self.num
                self.num+=1
                return value
            self.num+=1
prime=prime_inf()
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))

