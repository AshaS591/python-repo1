'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
 '''
n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
print()

#################################################################
'''
* * * * *
* * * *
* * *
* *
*
'''
n=5
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
print()

#####################################################
'''
*
* *
* * *
* * * *
* * * * *
'''
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

####################################################
'''
* * * * *
* * * *
* * *
* *
*
'''

n=5
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()

###########################################################
'''
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4)
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4)
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4)
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4)
'''
for row in range(5):
    for col in range(5):
        print((row,col),end=' ')
    print()

#########################################################

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
        
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row>col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()