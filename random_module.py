import random
# print(help('random'))

print(random.random)

print(random.random())

print(random.randint(1,10))

print(random.randrange(1,10,2))

colors=['pink','white','grey','blue','red','orange']
random.shuffle(colors)
print(colors)

print(random.choice(colors))

print(random.choices([1,2],weights=[-2,3],k=8))

print(random.choices([1,2],weights=[0.9,0.1],k=8))

print(random.choices([1,2],weights=[-5,6],k=3))

print(random.choices([9,10],weights=[0.9,0.1],k=5))
