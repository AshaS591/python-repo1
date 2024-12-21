''' NUMBER PATTERNS'''

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
n=int(input('enter n value:'))
for row in range(n+1):
    for col in range(row):
        print(col+1,end=' ')
    print()
###########################################################

'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n=int(input('enter n value:'))
num=1
for row in range(n+1):
    for col in range(row):
        print(num,end=' ')
        num+=1
    print()

########################################################
'''
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
'''
n=int(input('enter n value:'))
num=1
for row in range(n+1):
    for col in range(row):
        print(num,end=' ')
        num+=2
    print()

###################################################

'''
1
2 3
4 5 6
7 8 9 1
2 3 4 5 6
'''
n=int(input('enter n value:'))
num=1
for row in range(n+1):
    for col in range(row):
        if num>9:
           num=1
           print(num,end=' ')
           num+=1
        else:
            print(num,end=' ')
            num+=1
    print()

#######################################################

"""
1 9 8 7 6 
5 4 3 2
1 9 8
7 6
5
"""
n=int(input('enter n value:'))
num=1
for row in range(n,0,-1):
    for col in range(row):
        if num<1:
           num=9
           print(num,end=' ')
           num-=1
        else:
            print(num,end=' ')
            num-=1
    print()

#######################################################

'''
        1
      2 3
    4 5 6
  7 8 9 1
2 3 4 5 6 
'''
n=int(input('enter n value:'))
num=1
for row in range(n):
    print('  '*(n-row),end='')
    for col in range(row+1):
        if num>9:
           num=1
           print(num,end=' ')
           num+=1
        else:
            print(num,end=' ')
            num+=1
    print()

#####################################################
'''
    1
   2 3
  4 5 6
 7 8 9 1
'''
n=int(input('enter n value:'))
num=1
for row in range(n):
    print(' '*(n-row),end='')
    for col in range(row):
        if num>9:num=1
        print(num,end=' ')
        num+=1
    print()

######################################################
'''
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
'''
n=int(input('enter  n value :'))
for row in range(n,0,-1):
    for col in range(row):
        print(col+1,end=" ")
    print()

##################################################

'''
5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1
'''
n=int(input('enter  n value :'))
num=1
for row in range(n,0,-1):
    for col in range(row):
        print(row,end=' ')
    print()

##################################################

'''
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
n=int(input('enter  n value :'))
num=1
for row in range(n):
    for col in range(row+1):
        print(num,end=' ')
    num+=1
    print()

