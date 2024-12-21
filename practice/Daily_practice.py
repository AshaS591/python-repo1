# #1.To print square of a number entered by user
# num=int(input('enter a number :'))
# square=num**2
# print(f'Square of {num} is {square}')       

# #2.To print cube of a number entered by user
# num=int(input('enter a number :'))
# cube=num**3
# print(f'Cube of {num} is {cube}')

# #3. To print last element from the list entered by user
# user_list=eval(input('enter a list :'))
# last_element=user_list[-1]
# print(f"The last element of the user entered list is {last_element}")

# #4.To print the element present in the index position entered by user
# user_list=eval(input('enter a list :'))
# index=int(input('enter a index :'))
# print(f'element present in the index position entered by user is {user_list[index]}')

# #5.To print the remove element present in the index position entered by user
# user_list=eval(input('enter a list :'))
# index=int(input('enter a index :'))
# print(user_list.pop(index))

# #6.To print the reverse of a word entered by user
# word=input('enter a word :')
# print(f"revere of {word} is {word[::-1]}")

# #7.To perform basic mathematical operations on 2 no entered by the user and print result using print function
# num1=int(input('enter first no :'))
# num2=int(input('enter second no :'))
# sum=num1+num2
# diff=num1-num2
# product=num1*num2
# div=num1/num2
# mod=num1%num2
# floor=num1//num2
# print(f"sum is {sum},diffrence is {diff},product is {product},true division is {div},mod is {mod},floor division is {floor}")

# #8.wap to print sum of the  digits of a 3 digit number entered by the user
# number=input('enter a number')
# a,b,c=number[0],number[1],number[2]
# sum=int(a)+int(b)+int(c)
# print(sum)

# # 34.Write a program to check whether the first value present inside the given list is complex or not.
# items=eval(input('Enter a list of values :'))
# if type(items[0])==complex:
#     print(f"Datatype of {items[0]} is complex ")
# else:
#     print(f"Datatype of {items[0]} is not complex ")

# #35.Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.
# items=eval(input('Enter two items of a tuple :'))
# if type(items[0])==type(items[1]):
#     print(f"{items} is a homogeneous tuple")
# else:
#     print(f"{items} is a heterogeneous tuple")

#36.Write a program to check whether the given integer number is multiple of 10 or not.
# number = int(input('Enter a number :'))
# if number%10==0:
#     print(f"{number} is multiple of 10")
# else:
#     print(f"{number} is not multiple of 10")

# #Write a program to check whether the given string is palindrome or not.
# string = input('Enter a string :')
# reverse=string[::-1]
# if reverse==string:
#     print(f"{string} is a palindrome...")
# else:
#     print(f"{string} is not a palindrome...")

#39.Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.
# string = input('Enter a string :')
# length=len(string)
# if length>3:
#     print(f"Length of the string {string} is {length} ")
# else:
#     print(f"string is {string}")

# # 21/11/2024 (every day five programs)
# #1 wap to check whether a number is armstrong no or not using while loop
# number=int(input('enter a number :'))
# num=number
# armstrong_num=0
# while num!=0:
#     last_digit=num%10
#     armstrong_num+=last_digit**len(str(number))
#     num//=10
# if number==armstrong_num:
#     print(f"{number} is armstrong number...")
# else:
#     print(f"{number} is not armstrong number...")

# #2 wap to find factorial of a number using recursive functions
# def factorial(num):
#     if num==0:
#         return 1
#     else:
#         return num*factorial(num-1) 
# number=int(input('Enter a number :'))
# print(f"factorial of {number} is {factorial(number)}")

# #3 wap to  create dictionary where keys are each characters in a sentance and values are numbers of occurances of characters using for loop
# sentence=input('Enter a sentance :')
# collection={}
# for each_char in sentence:
#     if each_char in collection:
#         collection[each_char]+=1
#     else:
#         collection[each_char]=1
# print(collection)

# #4 wap to reverse a string without using builtin method
# string=input('Enter a string :')
# index=0
# reverse=''
# while index<len(string):
#     char=string[index]
#     reverse=char+reverse
#     index+=1
# print(f'Reverse of {string} : {reverse}')

# #5 wap to get the following output
# # input ='hai hello good morning'
# # output={'hai':'a','hello':'l','good':'gd','morning':'n'}

# line=input('Enter a sequence of words :')
# words=line.split()
# output={}
# for word in words:
#     if len(word)%2==0:
#         output[word]=word[0]+word[-1]
#     else:
#         output[word]=word[len(word)//2]
# print(output)

#Day 2
#1. wap in which function takes another function an argument
# def add(num1,num2):
#     return num1+num2
# def diff(num1,num2):
#     return num1-num2
# def product(num1,num2):
#     return num1*num2
# def arithmetic(sum,product,diff,num1,num2):
#     return f"sum of {num1} and {num2} is {sum(num1,num2)}",f"Difference of {num1} and {num2} is {diff(num1,num2)}",f"product of {num1} and {num2} is {product(num1,num2)}"
# print(arithmetic(add,product,diff,10,40))

# #2 wap which is based on miscelleneous function
# def login(username,password):
#     name=input('Enter a name :')
#     if name==username:
#         print('valid username...')
#         pass_key=input('Enter a password :')
#         if pass_key==password:
#             print("Login succesfull...")
#         else:
#             count=0
#             while count<3:
#                 pass_key=input('Enter a password :')
#                 if pass_key==password:
#                      print("Login succesfull...")
#                      break
#                 else:
#                     if count<2:
#                         print('Enter correct password...')
#                     else:
#                         print('Currently your account is blocked,Try after 24 hours')
#                 count+=1     
#     else:
#         print('Invalid username')
# sign_in=login
# sign_in(username='Asha',password='asha@1405s')

#3 wap using concept of kwargs(keyword arguments)
# def voter_list(*ages,**names):
#     user_name = input("Enter your name :")
#     user_age = int(input('Enter your age :'))
#     for age in ages:
#         if age==user_age:
#             print('Eligible to vote....allow us to verify with other details as well...')
#             for name in names:
#                 if names[name]==user_name:
#                     print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
#                 else:
#                     count=0
#                     while count<len(names):
#                         user_name = input("Enter your name :")
#                         if user_name==names[name]:
#                             print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
#                             break
#                         else:
#                             print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
#                         count+=1
#             else:
#                 print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
#         else:
#             count1=0
#             while count1<len(ages):
#                 user_age = int(input('Enter your age :'))
#                 if age==user_age:
#                     print('Eligible to vote....allow us to verify with other details as well...')
#                     for name in names:
#                         if names[name]==user_name:
#                             print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
#                         else:
#                             count=0
#                             while count<len(names):
#                                 user_name = input("Enter your name :")
#                                 if user_name==names[name]:
#                                     print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
#                                     break
#                                 else:
#                                     print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
#                                 count1+=1
#                     else:
#                         print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
#                 else:
#                     print('You are minor not eligible to vote')
# voter_list(10,20,name1='asha',name2='anu')

#1.categorize all vowels in a string
# char=input('enter a char')
# if char.isalpha():
#     if char in 'aeiouAEIOU':
#         list1=[]
#         list1.append(char)
#         print(list1)
#     else:
#         print(ord(char))

# #2 greatest among 3 numbers
# num1=int(input('enter num1 :'))
# num2=int(input('enter num2 :'))
# num3=int(input('enter num3 :'))
# if num1>num2:
#     if num1>num3:
#         print(f"{num1} is greatest")
#     else:
#         print(f"{num3} is greatest")
# else:
#     if num2>num3:
#         print(f"{num2} is greatest")
#     else:
#         print(f"{num3} is greatest")

# #3. wap to check for leap year 
# year=304
# if year%4==0 and year%100!=0 or year%400==0:
#     print('leap year')
# else:
#     print("not")

# #wap to print roots of a quadratic equation
# a=int(input('enter a:'))
# b=int(input('enter b:'))
# c=int(input('enter c:'))
# d=(b**2)- 4* a*c
# e=d**0.5
# root1=(-b+e)/2*a
# root2=(-b-e)/2*a
# print(f"Roots of {a}x^2{+(b)}x+{c} is {root1} and {root2}")

# #wap to swap to numbers
# num1=int(input("enter a number 1: "))
# num2=int(input("enter a number 2: "))
# temp=num1
# num1=num2
# num2=temp
# print(f"the numbers after swaping are num1={num1},num2={num2}")

# #wap to swap to numbers without using temp variable
# num1=int(input("enter a number 1: "))
# num2=int(input("enter a number 2: "))
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
# print(f"the numbers after swaping are num1={num1},num2={num2} without using temp variable")

# #wap to print no of vowels in string
# string=input('enter a sequence :')
# low=string.lower()
# a=low.count('a')
# e=low.count('e')
# i=low.count('i')
# o=low.count('o')
# u=low.count('u')
# print(f"count of vowels in {string} is {a+e+i+o+u}")


# # string palindrome progarame
# string=input('enter the word :')
# rev_str=string[::-1]
# if rev_str==string:
#     print('palindrome')

"""
*
* *
* * *
* * * *
* * * * *

"""
for row in range(5):
    for col in range(row+1):
        if col<=row:
            print('*',end=' ')
    print()

""" 
1
2 3
4 5 6
7 8 9 10

"""
count=0
for row in range(7):
    for col in range(row):
        count+=1
        print(count,end=' ')
    print()

"""
1
2 2
3 3 3
4 4 4 4
"""
count=0
for row in range(5):
    count+=1
    for col in range(row+1):
        print(count,end=' ')
    print()

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
for row in range(5):
    count=0
    for col in range(row+1):
        count+=1
        print(count,end=' ')
    print( )
print()
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
'''
for row in range(5):
    for col in range(5):
        print(row+1,end=' ')
    print()

'''
4 4 4 4 4
3 3 3 3 3 
2 2 2 2 2
1 1 1 1 1
'''
for row in range(6,0,-1):
    for col in range(6):
        print(row,end=' ')
    print()

'''
9
8 7
6 5 4
3 2 1 0
'''
count=9
for row in range(5):
    for col in range(row):
        print(count,end=' ')
        count-=1
    print()

'''
* * * *
* * *
* *
* * *
* * * *
'''
for row in range(10):
    for col in range(10):
        if row+col<10 or  col<=row :
            print('*',end=' ')
    print()
print()
'''
* * * * *
* * * *
* * * * *
* * * * *
* * * * * 
'''

for row in range(9):
    for col in range(9):
        if row==0 or col==0 or row==9 or row+col<9 or row>=9//2:
            print("*",end=' ')
    print()


# find factorial of a number using recursion
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
       return num*factorial(num-1)
        
print(factorial(6))

add=lambda num1,num2,num3:print(f'sum is {num1+num2+num3}') if (num1+num2+num3)%2==0 else print('sum is odd')
add(10,20,30)

from math import factorial
print(factorial(10))

from math import floor
print(floor(10.9))

def demo(func):
    return func
fact=demo(factorial)
res=fact(7)
print(res)

'''
A B C B A
D E F E D
G H I H G
J K L K J
M N O N M
'''
char=64
temp=0
for row in range(5):
    for col in range(5):
        if col<=5//2:
            char+=1
            print(chr(char),end=' ')
            
            temp=char
        else:
            temp-=1
            print(chr(temp),end=' ')
    print()

"""
* * * * *
* * * *
* * *
* *
*
"""
for row in range(5):
    for col in range(5,0,-1):
        if col>row:
            print('*',end=' ')
    print()

"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
for row in range(5):
    for col in range(5):
        if col<row:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()

'''
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
char=65
for row in range(5):
    for col in range(5):
        print(chr(char),end=' ')
    print()
    char+=1

"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""
print()
for row in range(5):
    char=65
    for col in range(5):
        print(chr(char),end=' ')
        char+=1
    print()
print()

'''
Find all of the numbers from 1-1000 that are divisible by 7
'''
numbers=[num for num in range(0,1000,7)]
print(numbers)

'''
Find all of the numbers from 1-1000 that have a 3 in them
'''
numbers=[num for num in range(1,1000) if str(3) in str(num)]
print(numbers)

'''
Count the number of spaces in a string
'''
string='Count the number of spaces in a string'
count=0
spaces_count=sum([count+1 for char in string if char==' '])
print(f'Count of spaces in {string} is {spaces_count}')

'''
Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
'''
string='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
consonants=[char for char in string if char not in 'AEIOUaeiou']
print(consonants)

'''
Get the index and the value as a tuple for items in the list 'hi', 4, 8.99, 'apple', (‘t,b’,’n’). Result would look like (index, value), (index, value)
'''
items=['hi', 4, 8.99, 'apple', ('t','b','n')]
new_items=[(items.index(item),item) for item in items ]
print(new_items)

'''
Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
'''
list_a=[1, 2, 3, 4]
list_b=[2, 3, 4, 5]
common_elements=[item for item in list_a if item in list_b]
print(common_elements)

'''
Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
'''
sentence='In 1984 there were 13 instances of a protest with over 1000 people attending'
list_numbers=sentence.split()
digits=[int(number) for number in list_numbers if number.isnumeric()]
print(digits)

'''
Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
'''
output=['even' if num%2==0 else 'odd' for num in range(20)]
print(output)

'''
Find all of the words in a string that are less than 4 letters
'''
string='Find all of the words in a string that are less than 4 letters'
words=string.split()
new_words=[word for word in words if len(word)<4]
print(new_words)