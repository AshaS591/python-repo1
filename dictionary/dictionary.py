'''
   Ordered collection
   1.data stored in the form of key-value pair
   2.Each key,value are separated by :
   3.key value pair separated by comma
   4.does not store duplicate key
   5. keys should of immutable datatype and values can be any datatype
'''

details={'name':'Asha S','roll_no':787,'CGPA':9.16,'Branch':'CSE'}

print(details.keys())

print(details.values())

print(details.items())

print(details.pop('Branch'))

new=details.copy()
print(new)

res=details.popitem()
print(res)


details.update({'age':21})
print(details)

details = {
    'names':{'name':['a','p','d']},
    'ages':{'age':'723098'}
}
print(details['names']['name'][0])
print(details['ages']['age'][0])
print(details.keys())