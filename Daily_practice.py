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
def add(num1,num2):
    return num1+num2
def diff(num1,num2):
    return num1-num2
def product(num1,num2):
    return num1*num2
def arithmetic(sum,product,diff,num1,num2):
    return f"sum of {num1} and {num2} is {sum(num1,num2)}",f"Difference of {num1} and {num2} is {diff(num1,num2)}",f"product of {num1} and {num2} is {product(num1,num2)}"
print(arithmetic(add,product,diff,10,40))

#2 wap which is based on miscelleneous function
def login(username,password):
    name=input('Enter a name :')
    if name==username:
        print('valid username...')
        pass_key=input('Enter a password :')
        if pass_key==password:
            print("Login succesfull...")
        else:
            count=0
            while count<3:
                pass_key=input('Enter a password :')
                if pass_key==password:
                     print("Login succesfull...")
                     break
                else:
                    if count<2:
                        print('Enter correct password...')
                    else:
                        print('Currently your account is blocked,Try after 24 hours')
                count+=1     
    else:
        print('Invalid username')
sign_in=login
sign_in(username='Asha',password='asha@1405s')

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
char=input('enter a char')
if char.isalpha():
    if char in 'aeiouAEIOU':
        list1=[]
        list1.append(char)
        print(list1)
    else:
        print(ord(char))

#2 greatest among 3 numbers
num1=int(input('enter num1 :'))
num2=int(input('enter num2 :'))
num3=int(input('enter num3 :'))
if num1>num2:
    if num1>num3:
        print(f"{num1} is greatest")
    else:
        print(f"{num3} is greatest")
else:
    if num2>num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

#3. wap to check for leap year 
year=304
if year%4==0 and year%100!=0 or year%400==0:
    print('leap year')
else:
    print("not")