# n=int(input('enter n value:'))
# for row in range(n+1):
#     for col in range(row):
#         print(col+1,end=' ')
#     print()

# n=int(input('enter n value:'))
# num=1
# for row in range(n+1):
#     for col in range(row):
#         print(num,end=' ')
#         num+=1
#     print()

# n=int(input('enter n value:'))
# num=1
# for row in range(n+1):
#     for col in range(row):
#         print(num,end=' ')
#         num+=2
#     print()

# n=int(input('enter n value:'))
# num=1
# for row in range(n+1):
#     for col in range(row):
#         if num>9:
#            num=1
#            print(num,end=' ')
#            num+=1
#         else:
#             print(num,end=' ')
#             num+=1
#     print()

# n=int(input('enter n value:'))
# num=1
# for row in range(n,0,-1):
#     for col in range(row):
#         if num<1:
#            num=9
#            print(num,end=' ')
#            num-=1
#         else:
#             print(num,end=' ')
#             num-=1
#     print()

# n=int(input('enter n value:'))
# num=1
# for row in range(n):
#     print('  '*(n-row),end='')
#     for col in range(row):
#         if num>9:
#            num=1
#            print(num,end=' ')
#            num+=1
#         else:
#             print(num,end=' ')
#             num+=1
#     print()

# n=int(input('enter n value:'))
# num=1
# for row in range(n):
#     print(' '*(n-row),end='')
#     for col in range(row):
#         if num>9:num=1
#         print(num,end=' ')
#         num+=1
#     print()

# n=int(input('enter  n value :'))
# for row in range(n,0,-1):
#     for col in range(row):
#         print(col+1,end=" ")
#     print()

n=int(input('enter  n value :'))
num=1
for row in range(n,0,-1):
    for col in range(row):
        if num>9:num=1
        print(num,end=" ")
        num+=1
    print()