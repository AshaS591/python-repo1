#A
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row==0 and (col>0 and col<n-1))  or (col==0 and (row>0 and row<=n-1)) or (col==n-1 and (row>0 and row<=n-1)) or row==n//2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#B
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row==0 and col<=n-2) or (row==n-1 and col<=n-2) or col==0 or (col==n-1 and (row>0 and row<n//2)) or (col==n-1 and (row<n-1 and row>n//2)) or (row==n//2 and col<n-1):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
#c
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

# D
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row==0 and col<=n-2) or (row==n-1 and col<=n-2) or col==0 or (col==n-1 and (row>0 and row<=n//2)) or (col==n-1 and (row<n-1 and row>=n//2)):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#E
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or col==0:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#F
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n//2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#G
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or (col==n-1 and row>=n//2) or (row==n//2 and col>=n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#H
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#I
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
#J
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2 or (row==n-1 and col<=n//2) or (col==0 and row>=n//2) :
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

# # K
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col==0 or (col+row==n//2) or(row-col==n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#L
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#M
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or (row==col and row<=n//2) or (row+col==n-1 and col>=n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#N
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==col:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#O
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#P
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0  or row==n//2 or col==0 or (col==n-1 and row<=n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#Q
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row==0 and (col>0 and col<n-1)) or (col==0 and (row>0 and row<n-2)) or (row==n-2 and (col>0 and col<n-1)) or (col==n-1 and (row>0 and row<n-2)) or (row==col and row>=n//2)  :
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
    
# R
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (col==0 and (row>0 and row<=n-1)) or (col==n-1 and (row!=n//2) and row>0) or (row==n//2 and col<n-1) or (row==0 and col<=n-2) :
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#S
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or (col==0 and row<=n//2) or (col==n-1 and row>=n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#T
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if row==0 or col==n//2:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#U

n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row==n-1 and (col>0 and col<n-1)) or (col==0 and row!=n-1) or (col==n-1 and row!=n-1):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

# # V

n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if (row==col and  row<=n//2) or (col+row==n-1 and col>=n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#W
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or (row==col and row>=n//2) or (row+col==n-1 and col<=n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#X
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if col==row or row+col==n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#Y
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if  (row==col and row<=n//2) or (row+col==n-1 and col>=n//2) or (col==n//2 and row>=n//2):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

#Z
n=int(input('enter n value :'))
for row in range(n):
    for col in range(n):
        if  row==0 or row==n-1 or row+col==n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()