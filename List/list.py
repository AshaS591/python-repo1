''' List is a collection
    * mutable
    * stores homogeneous and heterogeneous elements
    * supports slicing and indexing
    * ordered collection'''

collection=[]
for num in range(10):
    collection.append(num) #append method
print(collection)

flowers=['jasmine','lily','sun flower','marrigold']
new_flowers=flowers.copy() #copy method
print(new_flowers)

new_flowers.remove('marrigold') #remove method
print(new_flowers)

new_flowers.clear() #clear method
print(new_flowers)

flowers.extend(['rose','lotus','hibiscus']) #extend method
print(flowers)

flowers.pop() #popmethod
print(flowers)

flowers.pop(-1) #pop method with index
print(flowers)

print(flowers.count('rose')) # count method

print(flowers.index('jasmine')) #index method

flowers.reverse() #reverse method
print(flowers)

flowers.insert(2,'lavender') #insert method
print(flowers)

flowers.sort() #sort method
print(flowers)