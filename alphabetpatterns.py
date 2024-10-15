# n=int(input('enter number :'))
# for row in range(n):
#     char='A'
#     for col in range(n):
#         print(char,end=' ')
#         char=chr(ord(char)+1)
#     print()

# n=int(input('enter number :'))
# for row in range(n):
#     char='A'
#     for col in range(row):
#         print(char,end=' ')
#         char=chr(ord(char)+1)
#     print()

# n=int(input('enter number :'))
# char='A'
# for row in range(n):
#     for col in range(n):
#         print(char,end=' ')   
#     print()
#     char=chr(ord(char)+1)

# n=int(input('enter number :'))
# char='A'
# for row in range(n):
#     for col in range(row+1):
#         print(char,end=' ')   
#     print()
#     char=chr(ord(char)+1)

n=int(input('enter number :'))
char='A'
for row in range(n):
    for col in range(n):
        print(char,end=' ')   
        char=chr(ord(char)+1)
    print()

n=int(input('enter number :'))
char1='A'
for row in range(n):
    new_char=char1
    for col in range(n):
        print(new_char,end=' ') 
        new_char=chr(ord(new_char)+1) 
    print()
    char1=chr(ord(char1)+1)
    
n=int(input('enter number :'))
char1='A'
for row in range(n):
    new_char=char1
    for col in range(n):
        if col<=n//2:
            print(new_char,end=' ') 
            new_char=chr(ord(new_char)+1) 
        else:
            new_char=chr(ord(new_char)-2) 
            print(new_char,end=' ') 
    print()
    char1=chr(ord(char1)+1)