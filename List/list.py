collection=[]
for num in range(10):
    collection.append(num) #append method
print(collection)

flowers=['jasmine','lily','sun flower','marrigold']
new_flowers=flowers.copy() #copy method
print(new_flowers)

new_flowers.remove('marrigold')
print(new_flowers)