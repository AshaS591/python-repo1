# #1. wap to add two numbers using functions
# # a)without using return type and arguments
# # b)with using return type and without arguments
# # c)without using return type and with arguments
# # d)with return type and with arguments

# # a)without using return type and arguments
# def sum():
#     num1=int(input('Enter number1 :'))
#     num2=int(input('Enter number2 :'))
#     print("sum",num1+num2)
# sum()

# # b)with using return type and without arguments
# def sum():
#     num1=int(input('Enter number1 :'))
#     num2=int(input('Enter number2 :'))
#     return num1+num2
# print(sum())

# # c)without using return type and with arguments
# def sum(num1,num2):
#     print(num1+num2)
# sum(10,20)

# # d)with return type and with arguments
# def sum(num1,num2):
#     return num1+num2
# res=sum(25,35)
# print(res)

# #2.wap to print series of even numbers using functions
# def check_even(num):
#     even_list=[]
#     for even in range(0,num,2):
#         even_list.append(even)
#     return even_list
# number=int(input('Enter a number :'))
# res=check_even(number)
# print(f"Even list :{res}")

# #3. wap to check for number palindrome using functions
# def reverse(num):
#     rev=0
#     while num!=0:
#         last_digit=num%10
#         rev=rev*10+last_digit
#         num//=10
#     return rev
# number=int(input('Enter a number :'))
# res=reverse(number)
# if res==number:
#     print('Palindrome.....')
# else:
#     print('Not a palindrome....')

# #4. wap to check for a string palindrome using functions
# def check_palindrome(string):
#     rev=''
#     for char in string:
#         rev=char+rev
#     if rev==string:
#         return 'Pallindrome...'
#     else:
#         return 'Not a palindrome...'

# #5.wap tp find area of rectangle using functions
# def area(length,breadth):
#     return length*breadth
# length=int(input('Enter length :'))
# breadth=int(input('Enter breadth :'))
# res=area(length,breadth)
# print(f'Area is {res} meter square')

# #6. wap to calculate factorial of a number using functions
# def factorial(num):
#     fact=1
#     if num==1 or num==0:
#         return fact
#     else:
#         for factor in range(1,num+1):
#             fact*=factor
#         return fact
# number=int(input('Enter a number :'))
# res=factorial(number)
# print(f"Factorial of {number} is {res}")

#7.wap to sum all the numbers in a list using functions
def sum_of(list):
    return sum(list)
res=sum([10,20,33.56,90,45.99])
print(res)

#8. wap that accepts a string and counts the number of upper and lower case letters using functions.
def count_letters(string):
    lower=0
    upper=0
    other=0
    for char in string:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
        else:
            other+=1
    return upper,lower,other
upper,lower,other=count_letters('The quick Brow Fox')
print(upper,lower,other)
    
#9.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct_list(list):
    new_list=[]
    for item in  list:
        if item not in new_list:
            new_list.append(item)
    return new_list
res=distinct_list([10,10,35,9.9,9.99,12,'25','string'])
print(res)

#10. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def check_prime(num):
    if num==1:
        return 'Not a prime'
    elif num==2:
        return 'Prime'
    else:
        number=2
        prime=True
        while number<num//2:
            if num%number==0:
                prime=False
            number+=1
        if prime==True:
            return 'Prime'
       
res=check_prime(11)
print(res)

