
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

''' 4. '''

class PrimeInf:
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
prime=PrimeInf()
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))

''' 5. '''

class FibSeries:
    def __init__(self):
        self.num1=0
        self.num2=1
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            value=self.num1
            self.num1,self.num2=self.num2,self.num1+self.num2
            return value
fib=FibSeries()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

''' 6. '''

class Armstrong:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        length=len(str(self.num))
        num=self.num
        arms=0
        while True:
            while num!=0:
                last_digit=num%10
                arms+=last_digit**length
                num//=10
            if arms==self.num:
                
                self.num+=1
                return self.num-1
            self.num+=1
            num = self.num
            arms = 0
            length = len(str(self.num))
armst=Armstrong()
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
print(next(armst))
        

