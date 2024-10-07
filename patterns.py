n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
print()

n=5
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
print()

n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

n=5
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()

for row in range(5):
    for col in range(5):
        print((row,col),end=' ')
    print()

for row in range(5):
    for col in range(row+1):
        print("*",end=' ')
    print()
print()

for row in range(5,0,-1):
    for col in range(row):
        print("*",end=' ')
    print()
print()

for row in range(5):
    for col in range(5):
        if row>col:
            print(" ",end=' ')
        else:
            print("*",end=" ")
    print()

for row in range (5,0,-1):
    for col in range(row):
        print('*',end=' ')
    print()
        
    