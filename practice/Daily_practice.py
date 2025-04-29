# # #1.To print square of a number entered by user
# # num=int(input('enter a number :'))
# # square=num**2
# # print(f'Square of {num} is {square}')       

# # #2.To print cube of a number entered by user
# # num=int(input('enter a number :'))
# # cube=num**3
# # print(f'Cube of {num} is {cube}')

# # #3. To print last element from the list entered by user
# # user_list=eval(input('enter a list :'))
# # last_element=user_list[-1]
# # print(f"The last element of the user entered list is {last_element}")

# # #4.To print the element present in the index position entered by user
# # user_list=eval(input('enter a list :'))
# # index=int(input('enter a index :'))
# # print(f'element present in the index position entered by user is {user_list[index]}')

# # #5.To print the remove element present in the index position entered by user
# # user_list=eval(input('enter a list :'))
# # index=int(input('enter a index :'))
# # print(user_list.pop(index))

# # #6.To print the reverse of a word entered by user
# # word=input('enter a word :')
# # print(f"revere of {word} is {word[::-1]}")

# # #7.To perform basic mathematical operations on 2 no entered by the user and print result using print function
# # num1=int(input('enter first no :'))
# # num2=int(input('enter second no :'))
# # sum=num1+num2
# # diff=num1-num2
# # product=num1*num2
# # div=num1/num2
# # mod=num1%num2
# # floor=num1//num2
# # print(f"sum is {sum},diffrence is {diff},product is {product},true division is {div},mod is {mod},floor division is {floor}")

# # #8.wap to print sum of the  digits of a 3 digit number entered by the user
# # number=input('enter a number')
# # a,b,c=number[0],number[1],number[2]
# # sum=int(a)+int(b)+int(c)
# # print(sum)

# # # 34.Write a program to check whether the first value present inside the given list is complex or not.
# # items=eval(input('Enter a list of values :'))
# # if type(items[0])==complex:
# #     print(f"Datatype of {items[0]} is complex ")
# # else:
# #     print(f"Datatype of {items[0]} is not complex ")

# # #35.Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.
# # items=eval(input('Enter two items of a tuple :'))
# # if type(items[0])==type(items[1]):
# #     print(f"{items} is a homogeneous tuple")
# # else:
# #     print(f"{items} is a heterogeneous tuple")

# #36.Write a program to check whether the given integer number is multiple of 10 or not.
# # number = int(input('Enter a number :'))
# # if number%10==0:
# #     print(f"{number} is multiple of 10")
# # else:
# #     print(f"{number} is not multiple of 10")

# # #Write a program to check whether the given string is palindrome or not.
# # string = input('Enter a string :')
# # reverse=string[::-1]
# # if reverse==string:
# #     print(f"{string} is a palindrome...")
# # else:
# #     print(f"{string} is not a palindrome...")

# #39.Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.
# # string = input('Enter a string :')
# # length=len(string)
# # if length>3:
# #     print(f"Length of the string {string} is {length} ")
# # else:
# #     print(f"string is {string}")

# # # 21/11/2024 (every day five programs)
# # #1 wap to check whether a number is armstrong no or not using while loop
# # number=int(input('enter a number :'))
# # num=number
# # armstrong_num=0
# # while num!=0:
# #     last_digit=num%10
# #     armstrong_num+=last_digit**len(str(number))
# #     num//=10
# # if number==armstrong_num:
# #     print(f"{number} is armstrong number...")
# # else:
# #     print(f"{number} is not armstrong number...")

# # #2 wap to find factorial of a number using recursive functions
# # def factorial(num):
# #     if num==0:
# #         return 1
# #     else:
# #         return num*factorial(num-1) 
# # number=int(input('Enter a number :'))
# # print(f"factorial of {number} is {factorial(number)}")

# # #3 wap to  create dictionary where keys are each characters in a sentance and values are numbers of occurances of characters using for loop
# # sentence=input('Enter a sentance :')
# # collection={}
# # for each_char in sentence:
# #     if each_char in collection:
# #         collection[each_char]+=1
# #     else:
# #         collection[each_char]=1
# # print(collection)

# # #4 wap to reverse a string without using builtin method
# # string=input('Enter a string :')
# # index=0
# # reverse=''
# # while index<len(string):
# #     char=string[index]
# #     reverse=char+reverse
# #     index+=1
# # print(f'Reverse of {string} : {reverse}')

# # #5 wap to get the following output
# # # input ='hai hello good morning'
# # # output={'hai':'a','hello':'l','good':'gd','morning':'n'}

# # line=input('Enter a sequence of words :')
# # words=line.split()
# # output={}
# # for word in words:
# #     if len(word)%2==0:
# #         output[word]=word[0]+word[-1]
# #     else:
# #         output[word]=word[len(word)//2]
# # print(output)

# #Day 2
# #1. wap in which function takes another function an argument
# # def add(num1,num2):
# #     return num1+num2
# # def diff(num1,num2):
# #     return num1-num2
# # def product(num1,num2):
# #     return num1*num2
# # def arithmetic(sum,product,diff,num1,num2):
# #     return f"sum of {num1} and {num2} is {sum(num1,num2)}",f"Difference of {num1} and {num2} is {diff(num1,num2)}",f"product of {num1} and {num2} is {product(num1,num2)}"
# # print(arithmetic(add,product,diff,10,40))

# # #2 wap which is based on miscelleneous function
# # def login(username,password):
# #     name=input('Enter a name :')
# #     if name==username:
# #         print('valid username...')
# #         pass_key=input('Enter a password :')
# #         if pass_key==password:
# #             print("Login succesfull...")
# #         else:
# #             count=0
# #             while count<3:
# #                 pass_key=input('Enter a password :')
# #                 if pass_key==password:
# #                      print("Login succesfull...")
# #                      break
# #                 else:
# #                     if count<2:
# #                         print('Enter correct password...')
# #                     else:
# #                         print('Currently your account is blocked,Try after 24 hours')
# #                 count+=1     
# #     else:
# #         print('Invalid username')
# # sign_in=login
# # sign_in(username='Asha',password='asha@1405s')

# #3 wap using concept of kwargs(keyword arguments)
# # def voter_list(*ages,**names):
# #     user_name = input("Enter your name :")
# #     user_age = int(input('Enter your age :'))
# #     for age in ages:
# #         if age==user_age:
# #             print('Eligible to vote....allow us to verify with other details as well...')
# #             for name in names:
# #                 if names[name]==user_name:
# #                     print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
# #                 else:
# #                     count=0
# #                     while count<len(names):
# #                         user_name = input("Enter your name :")
# #                         if user_name==names[name]:
# #                             print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
# #                             break
# #                         else:
# #                             print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
# #                         count+=1
# #             else:
# #                 print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
# #         else:
# #             count1=0
# #             while count1<len(ages):
# #                 user_age = int(input('Enter your age :'))
# #                 if age==user_age:
# #                     print('Eligible to vote....allow us to verify with other details as well...')
# #                     for name in names:
# #                         if names[name]==user_name:
# #                             print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
# #                         else:
# #                             count=0
# #                             while count<len(names):
# #                                 user_name = input("Enter your name :")
# #                                 if user_name==names[name]:
# #                                     print(f"Your are deatils are there in voterlist and you are eligible to vote... your details are  name :{user_name} and age :{user_age}")
# #                                     break
# #                                 else:
# #                                     print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
# #                                 count1+=1
# #                     else:
# #                         print(f'You are eligible to vote but you not applied for voter id or not registered for election... your details are  name :{user_name} and age :{user_age}')
# #                 else:
# #                     print('You are minor not eligible to vote')
# # voter_list(10,20,name1='asha',name2='anu')

# #1.categorize all vowels in a string
# # char=input('enter a char')
# # if char.isalpha():
# #     if char in 'aeiouAEIOU':
# #         list1=[]
# #         list1.append(char)
# #         print(list1)
# #     else:
# #         print(ord(char))

# # #2 greatest among 3 numbers
# # num1=int(input('enter num1 :'))
# # num2=int(input('enter num2 :'))
# # num3=int(input('enter num3 :'))
# # if num1>num2:
# #     if num1>num3:
# #         print(f"{num1} is greatest")
# #     else:
# #         print(f"{num3} is greatest")
# # else:
# #     if num2>num3:
# #         print(f"{num2} is greatest")
# #     else:
# #         print(f"{num3} is greatest")

# # #3. wap to check for leap year 
# # year=304
# # if year%4==0 and year%100!=0 or year%400==0:
# #     print('leap year')
# # else:
# #     print("not")

# # #wap to print roots of a quadratic equation
# # a=int(input('enter a:'))
# # b=int(input('enter b:'))
# # c=int(input('enter c:'))
# # d=(b**2)- 4* a*c
# # e=d**0.5
# # root1=(-b+e)/2*a
# # root2=(-b-e)/2*a
# # print(f"Roots of {a}x^2{+(b)}x+{c} is {root1} and {root2}")

# # #wap to swap to numbers
# # num1=int(input("enter a number 1: "))
# # num2=int(input("enter a number 2: "))
# # temp=num1
# # num1=num2
# # num2=temp
# # print(f"the numbers after swaping are num1={num1},num2={num2}")

# # #wap to swap to numbers without using temp variable
# # num1=int(input("enter a number 1: "))
# # num2=int(input("enter a number 2: "))
# # num1=num1+num2
# # num2=num1-num2
# # num1=num1-num2
# # print(f"the numbers after swaping are num1={num1},num2={num2} without using temp variable")

# # #wap to print no of vowels in string
# # string=input('enter a sequence :')
# # low=string.lower()
# # a=low.count('a')
# # e=low.count('e')
# # i=low.count('i')
# # o=low.count('o')
# # u=low.count('u')
# # print(f"count of vowels in {string} is {a+e+i+o+u}")


# # # string palindrome progarame
# # string=input('enter the word :')
# # rev_str=string[::-1]
# # if rev_str==string:
# #     print('palindrome')

# # """
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *

# # """
# # for row in range(5):
# #     for col in range(row+1):
# #         if col<=row:
# #             print('*',end=' ')
# #     print()

# # """ 
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10

# # """
# # count=0
# # for row in range(7):
# #     for col in range(row):
# #         count+=1
# #         print(count,end=' ')
# #     print()

# # """
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # """
# # count=0
# # for row in range(5):
# #     count+=1
# #     for col in range(row+1):
# #         print(count,end=' ')
# #     print()

# # '''
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
# # '''
# # for row in range(5):
# #     count=0
# #     for col in range(row+1):
# #         count+=1
# #         print(count,end=' ')
# #     print( )
# # print()
# # '''
# # 1 1 1 1 1
# # 2 2 2 2 2
# # 3 3 3 3 3
# # 4 4 4 4 4
# # '''
# # for row in range(5):
# #     for col in range(5):
# #         print(row+1,end=' ')
# #     print()

# # '''
# # 4 4 4 4 4
# # 3 3 3 3 3 
# # 2 2 2 2 2
# # 1 1 1 1 1
# # '''
# # for row in range(6,0,-1):
# #     for col in range(6):
# #         print(row,end=' ')
# #     print()

# # '''
# # 9
# # 8 7
# # 6 5 4
# # 3 2 1 0
# # '''
# # count=9
# # for row in range(5):
# #     for col in range(row):
# #         print(count,end=' ')
# #         count-=1
# #     print()

# # '''
# # * * * *
# # * * *
# # * *
# # * * *
# # * * * *
# # '''
# # for row in range(10):
# #     for col in range(10):
# #         if row+col<10 or  col<=row :
# #             print('*',end=' ')
# #     print()
# # print()
# # '''
# # * * * * *
# # * * * *
# # * * * * *
# # * * * * *
# # * * * * * 
# # '''

# # for row in range(9):
# #     for col in range(9):
# #         if row==0 or col==0 or row==9 or row+col<9 or row>=9//2:
# #             print("*",end=' ')
# #     print()

# # # find factorial of a number using recursion
# # def factorial(num):
# #     if num==0 or num==1:
# #         return 1
# #     else:
# #        return num*factorial(num-1)
        
# # print(factorial(6))

# # add=lambda num1,num2,num3:print(f'sum is {num1+num2+num3}') if (num1+num2+num3)%2==0 else print('sum is odd')
# # add(10,20,30)

# # from math import factorial
# # print(factorial(10))

# # from math import floor
# # print(floor(10.9))

# # def demo(func):
# #     return func
# # fact=demo(factorial)
# # res=fact(7)
# # print(res)

# # '''
# # A B C B A
# # D E F E D
# # G H I H G
# # J K L K J
# # M N O N M
# # '''
# # char=64
# # temp=0
# # for row in range(5):
# #     for col in range(5):
# #         if col<=5//2:
# #             char+=1
# #             print(chr(char),end=' ')
            
# #             temp=char
# #         else:
# #             temp-=1
# #             print(chr(temp),end=' ')
# #     print()

# # """
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
# # """
# # for row in range(5):
# #     for col in range(5,0,-1):
# #         if col>row:
# #             print('*',end=' ')
# #     print()

# # """
# # * * * * *
# #   * * * *
# #     * * *
# #       * *
# #         *
# # """
# # for row in range(5):
# #     for col in range(5):
# #         if col<row:
# #             print(' ',end=' ')
# #         else:
# #             print('*',end=' ')
# #     print()

# # '''
# # A A A A A
# # B B B B B
# # C C C C C
# # D D D D D
# # E E E E E
# # '''
# # char=65
# # for row in range(5):
# #     for col in range(5):
# #         print(chr(char),end=' ')
# #     print()
# #     char+=1

# # """
# # A B C D E
# # A B C D E
# # A B C D E
# # A B C D E
# # A B C D E
# # """
# # print()
# # for row in range(5):
# #     char=65
# #     for col in range(5):
# #         print(chr(char),end=' ')
# #         char+=1
# #     print()
# # print()

# # '''
# # Find all of the numbers from 1-1000 that are divisible by 7
# # '''
# # numbers=[num for num in range(0,1000,7)]
# # print(numbers)

# # '''
# # Find all of the numbers from 1-1000 that have a 3 in them
# # '''
# # numbers=[num for num in range(1,1000) if str(3) in str(num)]
# # print(numbers)

# # '''
# # Count the number of spaces in a string
# # '''
# # string='Count the number of spaces in a string'
# # count=0
# # spaces_count=sum([count+1 for char in string if char==' '])
# # print(f'Count of spaces in {string} is {spaces_count}')

# # '''
# # Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
# # '''
# # string='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
# # consonants=[char for char in string if char not in 'AEIOUaeiou']
# # print(consonants)

# # '''
# # Get the index and the value as a tuple for items in the list 'hi', 4, 8.99, 'apple', (‘t,b’,’n’). Result would look like (index, value), (index, value)
# # '''
# # items=['hi', 4, 8.99, 'apple', ('t','b','n')]
# # new_items=[(items.index(item),item) for item in items ]
# # print(new_items)

# # '''
# # Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
# # '''
# # list_a=[1, 2, 3, 4]
# # list_b=[2, 3, 4, 5]
# # common_elements=[item for item in list_a if item in list_b]
# # print(common_elements)

# # '''
# # Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
# # '''
# # sentence='In 1984 there were 13 instances of a protest with over 1000 people attending'
# # list_numbers=sentence.split()
# # digits=[int(number) for number in list_numbers if number.isnumeric()]
# # print(digits)

# # '''
# # Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
# # '''
# # output=['even' if num%2==0 else 'odd' for num in range(20)]
# # print(output)

# # '''
# # Find all of the words in a string that are less than 4 letters
# # '''
# # string='Find all of the words in a string that are less than 4 letters'
# # words=string.split()
# # new_words=[word for word in words if len(word)<4]
# # print(new_words)

# # '''
# # Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# # '''
# # nested_list=[[num for num in range(1,100) if num%number==0]for number in range(2,10)]
# # print(nested_list)

# # '''Write a program to find the sum of following series
# #  1+8+27…………nterms
# # '''
# # start=1
# # series=''
# # end=int(input('Enter ending point :'))
# # while start<=end:
# #     series+=f'{start**3}'
# #     start+=1
# #     if start<end:
# #         series+=' + '
# # print(series)

# # ''' Write a program to find the sum of following series:
# #   2 + 6 + 12 + 20 + 3042. . . .nterms'''
# # start=1
# # series=''
# # end=int(input('Enter ending point :'))
# # while start<=end:
    
# #     series+=f'{start*(start+1)}'
   
# #     start+=1
# #     if start<end:
# #         series+=' + '
# # print(series)

# ###################################################################################################

# ''' Decorators '''

# ''' class implimentation of class decorators '''
# """ 1. """
# class ClsDeco:
#     def __call__(self,cls_address):
#         def outer(method_deco):
#             def inner(*args,**kwargs):
#                 print(f'Executing {method_deco.__name__}')
#                 method_deco(*args,**kwargs)
#                 print(f'Executed {method_deco.__name__}')
#             return inner
        
#         for name,address in cls_address.__dict__.items():
#             if callable(address):
#                 setattr(cls_address,name,outer(address))
#         return cls_address
# @ClsDeco()
# class Math:
#     def add(self):
#         print('This method performs addition..')
#     def product(self):
#         print('This method performs multiplication..')
# obj=Math()
# obj.add()
# obj.product()

# ''' 2. '''   
# class Decorator:
#     def __call__(self,method_deco):
    
#         def wrapper(*args,**kwargs):
#             print(f'Executing {method_deco.__name__}')
#             method_deco(*args,**kwargs)
#             print(f'Executed {method_deco.__name__}')
#         return wrapper
# class Deco:
#     def __call__(self,clss):
#         for name,address in clss.__dict__.values():
#             if callable(address):
#                 obj=Decorator()
#                 setattr(clss,name,obj(address))
#         return clss

# class Display:
#     def sample(self):
#         print("Inside sample method..")
#     def random(self):
#         print('Inside random method..')

# obj=Display()
# obj.random()
# obj.sample()

# '''class implimentation of function decorator'''
# class Deco:
#     def __call__(self,func_address):
#         def inner(*args,**kwargs):
#             print('*'*20)
#             func_address(*args,**kwargs)
#             print('*'*20)
#         return inner
# @Deco()
# def message():
#     print('Inside message function..')
# message()

# ''' function implimentation of a class decorator '''
# def outer(cls_address): 
#     def decorator(method_address):
#         def inner(*args,**kwargs):
#             print('#'*20)
#             method_address(*args,**kwargs)
#             print('#'*20)
#         return inner
#     for name,address in cls_address.__dict__.items():
#         if callable(address):
#             setattr(cls_address,name,decorator(address))
#     return cls_address

# @outer
# class General:
#     def metod1(self):
#         print('Inside method1')
#     def metod2(self):
#         print('Inside method2')
# obj=General()
# obj.metod1()
# obj.metod2()

# ''' Dictionary comprehension '''
# names=['asha','abhi','shashi','rishi']
# roll_call=[1,2,3,4]
# details={name:rollno for name,rollno in zip(names,roll_call)}
# print(details)

# ''' Set Dictionary '''
# numbers={num**2 for num in range(10) if num%2==0}
# print(numbers)


# '''
# 1 1 1 1
# 1 2 2 1
# 1 2 2 1
# 1 1 1 1 
# '''
# for row in range(5):
#     for col in range(5):
#         if row==0 or col==0 or col==4 or row==4:
#             print(1,end=' ')

#         else:
#             print(2,end=' ')
#     print()
    
# '''
# 1 5 2 5 3
# 1 5 2 5 3
# 1 5 2 5 3
# 1 5 2 5 3
# 1 5 2 5 3
# '''
# for row in range(5):
#     count=0
#     for col in range(5):
#         if col%2==0:
#             count+=1
#             print(count,end=' ')

#         else:
#             count1=5
#             print(count1,end=' ')
#             count1-=1
#     print()


# def human(function):
#     def soul(*args,**kwargs):
#         print('*'*10)
#         function(*args,**kwargs)
#         print('*'*10)
#     return soul

# @human
# def body():
#     print('body without soul is dead body')

# body()

# def outer(n1,n2):
#     def deco1(func):
#         def inner(*args,**kwargs):
#             if n1+n2>10:
#                 print(n1+n2)
#                 print('#'*20)
#                 func(*args,**kwargs)
#                 print('#'*20)
#         return inner
#     return deco1

# @outer(10,5)
# def random():
#     print('Inside random')
# random()

# def outer(cls_addr):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             print(f' Executing {func.__name__}')
#             print(func(*args,**kwargs))
#             print(f' Executed {func.__name__}')
#         return wrapper
    
#     for name,address in cls_addr.__dict__.items():
#         if callable(address):
#             setattr(cls_addr,name,deco(address))
#     return cls_addr

# @outer
# class Arithmetic:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return (self.num1+self.num2)
#     def sub(self):
#         return self.num1-self.num2

# obj=Arithmetic(20,10)
# obj.add()

def factorial(num1):
    fact=1
    num=1
    while num <= num1:
        fact*=num
        num+=1
    yield fact
var=factorial(5)
print(next(var))

var = factorial(6)
print(next(var))

var = factorial(7)
print(next(var))

# import csv
# file = open('sample.csv','a',newline='')
# writer_obj=csv.writer(file)
# # writer_obj.writerow(['name','age','branch'])
# # writer_obj.writerow(['asha','22','cse'])
# writer_obj.writerow(['arha','23','ise'])

# file.close()

import csv
file = open('sample.csv')
reader_obj = csv.reader(file)
# print(reader_obj)
next(reader_obj)
for data in reader_obj:
    print(data)
file.close()

# file = open('sample.csv')
# dir_obj=csv.DictReader(file)
# for item in dir_obj:
#     print(item)
# file.close()

# file = open('sample.csv','a',newline='')
# writer_obj = csv.writer(file)
# writer_obj.writerows([['anu','23','cbd'],['amala','21','bca']])
# file.close()

file = open('sample.csv')
rd=csv.DictReader(file)
next(rd)
for data in rd:
    if int(data['age']) > 20:
        print(data)
file.close()

file = open('sample.csv')
rd=csv.DictReader(file)
# next(rd)
for data in rd:
    if rd.line_num == 2:
        print(data)
file.close()

# class FileHandling:
#     def get_names(self,filename):
#         file = open(filename)
#         rd=csv.reader(file)
#         for data in rd:
#             if data['name']


#         file.close()

import json
with open('new.json','r') as file:
    # py_data={
    #     'name':'asha',
    #     'age':22,
    #     'hobbies':('singing','listening music')
    # }
    # var=json.dump(py_data,file)
    var=json.load(file)
print(var)

py_data={
        'name':'asha',
        'age':22,
        'hobbies':('singing','listening music')
    }
string = json.dumps(py_data)
print(string)

string = json.loads(string)
print(string)


class Home:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class House(Home):
    def __init__(self, name):
        # super().__init__(name)
        Home.__init__(self,name)
    def display(self):
        return Home.display(self)
a1=Home('Nilaya')
a1.display()
        
def armstrong():
    num=1
    while True:
        org=num
        arms=0
        while org!=0:
            last=org%10
            arms+=(last)**len(str(num))
            org//=10
        if arms==num:
            yield num
            # num+=1
        num+=1
var=armstrong()
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))

def prime():
    num=2
    while True:
        for number in range(2,num):
            if num % number==0:
                break
        else:
            yield num
        num+=1
var= prime()
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))

def perfect_square():
    num=1
    while True:
        for number in range(1,num+1):
            if num / number == number:
                yield num
        num+=1
var = perfect_square()
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))

        
def strong():
    num = 1
    while True:
        rev=0
        sum=0
        org=num
        while org != 0:
            last = org%10
            rev=rev*10+last
            org//=10
            fact=1
            for number in range(1,last+1):
                fact*=number
            sum+=fact
    
        if sum == num:
            yield num
        num+=1
var =strong()
print(next(var))
print(next(var))
print(next(var))
print(next(var))

class Deco:
    def __call__(self,cls_addr):
        def deco1(func_add):
            def wrap(*args,**kwargs):
                print(f'Execting {func_add.__name__}')
                print(func_add(*args,**kwargs))
                print(f'executed {func_add.__name__}')
            return wrap
        
        for name,address in cls_addr.__dict__.items():
            if callable(address):
                setattr(cls_addr,name,deco1(address))
        return cls_addr
@Deco()
class Display:
    def disp1(self):
        return 'display1'
    def disp2(self):
        return 'display2'
    def disp3(self):
        return 'display3'
    def disp4(self):
        return 'display4'                                                                                                                                                                
obj = Display()
obj.disp1()
obj.disp2()
obj.disp3()
obj.disp4()


import re

string='Hello asha how are u ashh'
pattern='asha?'
print(re.findall(pattern,string))

string = ' hello my adhar no is 3749 5237 0962'
pattern='[0-9]{4}\s[0-9]{4}\s[0-9]{4}'
print(re.findall(pattern,string))

string = ' hello my pan no is RMLPS5403K'
pattern='[A-Z]{5}[0-9]{4}[A-Z]'
print(re.findall(pattern,string))

string = ' dob is 14/01/2003, 31/12/9909'
pattern=r'(?:(?:[012][0-9]|3[01])/(?:0[0-9]|1[012])/(?:[0-9]{4}))'
print(re.findall(pattern,string))

string = ' ip addresses 1.89.87.9'
pattern=r'(:?(:?(:?0|1[0-9]{0,3}|2[0-5]{1,3}])\.){3}(:?0|1[0-9]{0,3}|2[0-5]{0,3}]))'
print(re.findall(pattern,string))

def sort_string(string):
    words=string.split()
    for inx in range(1,len(words)):
        for index in range(len(words)-inx):
            if words[index]>words[index+1]:
                words[index],words[index+1]=words[index+1],words[index]
                
            else:
                continue
    
    return words
string = 'python sql webtech selenium'
res=sort_string(string)
output=''
for word in res:
    output+=word+' '
print(output)
def main()->int:
    return 'hello'
print(main())

""" Programs on List """

# 1.

items = [10,23,30,45,89,90]
new_items = [item**2 for item in items]
print(new_items)

squares_of_even=[num**2 for num in items if num%2==0]
print(squares_of_even)

# Write a program to calculate the factorial of a number using a loop.
fact = 1
num = int(input('Enter a number :'))
factor=1
while factor<=num:
    fact*=factor
    factor+=1
print(f'Factorial of {num} is {fact}')

# Create a simple calculator that can perform addition, subtraction, multiplication, and division.
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
num1 = int(input('Enter num1 value :'))
num2 = int(input('Enter num2 value :'))

print(add(num1,num2))
print(mul(num1,num2))
print(div(num1,num2))
print(sub(num1,num2))

# Take a string input and count the number of vowels in it.
def count_vowels(string):
    count=0
    for char in string:
        if char in 'AEIOUaeiou':
            count+=1
    return count
string = input('Enter a word :')
print(f'Number of vowels in {string} is {count_vowels(string)}')

# Print all prime numbers between 1 and 100.

prime_num=[]
def is_prime(num):
    for n in range(2,num):
        if num%n==0:
            break
    else:
        prime_num.append(num)
for num in range(2,101):
    is_prime(num)
print(prime_num)

# Write a program to reverse a given number using a while loop.

num = 5687
rev=0
while num!=0:
    last=num%10
    rev=rev*10+last
    num//=10
print(rev)

# Find the largest number in a list using a for loop.

max_num=0
numbers = [23,17,89,23,90]

for num in numbers:
    max_num=max(max_num,num)
print(max_num)

# Generate the Fibonacci series up to n terms.
def fibonacci_nums():
    num1=0
    num2=1
    while True:
        yield num1
        num1,num2=num2,num1+num2
fib=fibonacci_nums()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# Check if a number is a palindrome.

num = int(input('Enter a number :'))
org=num
rev=0
while num!=0:
    last = num%10
    rev=rev*10+last
    num//=10
if rev==org:
    print('Palindrome...')
else:
    print('Not a Palindrome...')

# Write a function to remove duplicates from a list.

def remove_duplicates(collection,index=0,new=[]):
    if index==len(collection):
        return new
    if collection[index] not in new:
        new.append(collection[index])
    return remove_duplicates(collection,index+1,new)
items = [12,34,56,12,90,'hi','hi']
print(remove_duplicates(items))

# Sort a list of tuples by the second element.

items = [(1,20),('hello',90),(67,2)]
sorted_data=sorted(items,key=lambda x:x[1])
print(sorted_data)

# Create a dictionary from two lists: one of keys and one of values.

fruits = ['mango','grapes','pomogranate','banana','strawberry']
prices = [100,200,250,80,150]
fruits_prices = {fruit:price for fruit,price in zip(fruits,prices)}
print(fruits_prices)

# Count the frequency of each word in a sentence.

sentence = input('Enter a sentence :')
words=sentence.split()
frequency_of_words={word:words.count(word) for word in words}
print(frequency_of_words)

# Merge two dictionaries into one.

student_details = {'name':'asha','age':22}
asha_details = {'name':'Asha S','education':'B.Tech','stream':'CSE'}
student_details.update(asha_details)
print(student_details)

# Write a function to check if a string is a palindrome.

def is_palindrome(string):
    if string == string[::-1]:
        return 'Palindrome...'
    else:
        return 'Not a palindrome..'
string = input('Enter a string :')
print(is_palindrome(string))

# Create a function that accepts a list and returns the sum of its elements.

def sum_of_elements(numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum
numbers=[10,29,89,98,23]
print(sum_of_elements(numbers))

# Write a function that finds the second largest number in a list.

def second_largest(numbers):
    numbers.sort(reverse=True)
    return numbers[1]
numbers=[34,9,23,87,34,56]
print(second_largest(numbers))

# # Create a recursive function to compute the nth Fibonacci number.
def fibonacci(num):
    if num==1:
        return 0
    elif num==2 or num==3:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(5))

# Write a function that returns the number of uppercase and lowercase letters in a string.

def count_upper_lower(string):
    lower=0
    upper=0
    for char in string:
        if char>='A' and char<='Z':
            upper+=1
        elif char>='a' and char<='z':
            lower+=1
    return lower,upper
print(count_upper_lower('VyTbnbETRDjiu'))


# Write a program that reads a file and prints its content.
with open('read.txt','w') as file:
    file.writelines(['hey hi my name is asha...\n','welcome to old version\n','Octopuses have three hearts\n','Birds are dinosaurs'])

with open('read.txt','r') as file1:
    
    file1.seek(0)
    print(file1.read())
    

# Count the number of lines, words, and characters in a file.
with open('read.txt','r') as file1:
    
    file1.seek(0)
    lines=0
    words=0
    chars=0
    data=file1.readlines()
    for line in data:
        lines+=1
        list_of_words=line.split()
        words+=len(list_of_words)
        for char in line:
            chars+=1
    print('Words :',words)
    print('lines :',lines)
    print('Characters :',chars)

# Handle exceptions for division by zero and invalid inputs.
while True:
    try:
        dividend = int(input('Enter a number :'))
        divisor = int(input('Enter a number :'))
        res = dividend/divisor
    except ZeroDivisionError:
        print('Enter the number otherthan zero for divisor...')
    except ValueError:
        print('Enter only numerical data...')
    else:
        print("Quotient is :",res)
        break

# Write to a file and then read from it.

# Copy contents of one file into another.
