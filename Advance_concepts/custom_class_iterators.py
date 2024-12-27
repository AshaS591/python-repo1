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
