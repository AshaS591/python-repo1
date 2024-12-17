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