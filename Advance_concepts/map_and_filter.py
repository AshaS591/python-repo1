''' Map function to print cube of each number of a collection'''
def cube(num):
    return num**3
nums=[10,20,21,90,15]
res=map(cube,nums)
print(next(res))