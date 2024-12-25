""" 1.set is unordered collection
    2.stores only immutable data inside it
    3. does not supports indexing and slicing
    4.does not supports duplicates
"""
colors={'pink','orange','red','white','blue'}
colors.add('black')
print(colors)

new_colors=colors.copy()
print(new_colors)

new_colors.clear()
print(new_colors)

res=colors.pop()
print(res)
print(colors)

set1={1,2,3,4,5}
set2={1,2,3}

res=set1.intersection(set2)
print(res)

res=set1.difference(set2)
print(res)

res=set1.union(set2)
print(res)

set1.update(set2)
print(set1)

set1.difference_update(set2)
print(set1)

set3={True,0,3,5}
set4={1,0,3,5,5,7}
print(set3.issubset(set4))

print(set4.issuperset(set3))

print(set4.isdisjoint(set3))

print(set4.discard(set3))


