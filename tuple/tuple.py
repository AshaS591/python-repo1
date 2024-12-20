#tuple supports only indexing and slicing because it is immutable
#we can check length and count of element

lap=('dell','lenevo','hp','mac','asus')
print(lap.count('dell'))  #count method
print(lap.index('mac'))   #index method
print(lap.index('mac',1,4))
rings=('gold','silver','bronze','copper','platinum','diamond')
print(len(rings))
print(rings[2][2:5:2])