#1.wap to extract all the numeric values in a given collection
collection=eval(input('Enter a collection :'))
numbers=[]
for item in collection:
    if type(item) in [int,float,complex]:
        numbers.append(item)
print(f"All numbers in a collection are :{numbers}")
