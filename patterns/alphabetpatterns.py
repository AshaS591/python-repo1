'''
A B C D E 
A B C D E
A B C D E
A B C D E
A B C D E
'''
n=int(input('enter number :'))
for row in range(n):
    char='A'
    for col in range(n):
        print(char,end=' ')
        char=chr(ord(char)+1)
    print()

'''
A 
A B
A B C
A B C D
A B C D E
'''
n=int(input('enter number :'))
for row in range(n):
    char='A'
    for col in range(row+1):
        print(char,end=' ')
        char=chr(ord(char)+1)
    print()

'''
A A A A A 
B B B B B
C C C C C
D D D D D
E E E E E
'''
n=int(input('enter number :'))
char='A'
for row in range(n):
    for col in range(n):
        print(char,end=' ')   
    print()
    char=chr(ord(char)+1)

'''
A 
B B
C C C
D D D D
E E E E E
'''
n=int(input('enter number :'))
char='A'
for row in range(n):
    for col in range(row+1):
        print(char,end=' ')   
    print()
    char=chr(ord(char)+1)

'''
A B C D E 
F G H I J
K L M N O
P Q R S T
U V W X Y
'''
n=int(input('enter number :'))
char='A'
for row in range(n):
    for col in range(n):
        print(char,end=' ')   
        char=chr(ord(char)+1)
    print()

'''
A B C D E 
B C D E F
C D E F G
D E F G H
E F G H I
'''
n=int(input('enter number :'))
char1='A'
for row in range(n):
    new_char=char1
    for col in range(n):
        print(new_char,end=' ') 
        new_char=chr(ord(new_char)+1) 
    print()
    char1=chr(ord(char1)+1)
    
'''
A B C B A 
B C D C B
C D E D C
D E F E D
E F G F E
'''
n=int(input('enter number :'))
char1='A'
for row in range(n):
    new_char=char1
    for col in range(n):
        if col<=n//2:
            print(new_char,end=' ') 
            new_char=chr(ord(new_char)+1) 
        elif col==n//2+1:
            new_char=chr(ord(new_char)-2) 
            print(new_char,end=' ') 
        else:
            new_char=chr(ord(new_char)-1) 
            print(new_char,end=' ')
    print()
    char1=chr(ord(char1)+1)