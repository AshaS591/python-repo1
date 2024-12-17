# #########################################################################
# def decorator(func_name):
#     def wrapper(*args,**kwargs):
#         print('Executing wrapper....')
#         for _ in range(3):
#             print('-'*40)
#             func_name()
#             print('-'*40)
#     return wrapper

# @decorator
# def greet():
#     print('Welcome to Decorators in python')

# greet()
# ############################ PARAMETERIZED DECORATOR ##############################################
# from time import sleep
# def outer(n):
#     def decorator(func_name):
#         def inner(*args,**kwargs):
#             print('inside inner...')
#             for num in range(n):
#                 sleep(1)
#                 print(num)
#                 func_name(num)
#         return inner
#     return decorator

# @outer(5)
# def display(n):
#     print(f"calling display function for {n+1} time")

# display()
# ##################################################################################################

# """WAP to print factorial of a number using decorator"""

# def number(num):
#     def whole_number(func_name):
#         def calculate(*args,**kwargs):
#             try:
#                 print(f"Calculating factorial of number : {num}")
#                 Factorial=func_name(*args,**kwargs)
#             except Exception as msg:
#                 print(msg)
#             else:
#                 print(f"Factorial of number : {num} is {Factorial}")
#         return calculate
#     return whole_number

# @number(6)
# def factorial(num:int):
#     fact=1
#     for num in range(1,num+1):
#         fact*=num
#     return fact

# factorial(6)

# ##################################################################################################

# """WAP to print reverse of a number using decorator"""

# def number(func_name):
#         def display_reverse(*args,**kwargs):
#             try:
#                 rev=func_name(*args,**kwargs)
#             except Exception as msg:
#                 print(msg)
#             else:
#                 print(f"Reverse of number is {rev}")
#         return display_reverse

# @number
# def reverse(num:int):
#     rev_num=0
#     while num!=0:
#         last_digit=num%10
#         rev_num=rev_num*10+last_digit
#         num//=10
#     return rev_num

# reverse(456)

# ##################################################################################################

# """WAP to check for a number palindrome  using decorator"""
# def outer(num):
#     def number(func_name):
#         def check_palindrome(*args,**kwargs):
            
#             try:
#                 rev=func_name(num)
#             except Exception as msg:
#                 print(msg)
#             else:
#                 if num==rev:
#                     print("Palindrome......")
#                 else:
#                     print(" Not a palindrome......")
#         return check_palindrome
#     return number

# @outer(998)
# def palindrome(num:int):
#     rev_num=0
#     while num!=0:
#         last_digit=num%10
#         rev_num=rev_num*10+last_digit
#         num//=10
#     return rev_num               

# palindrome()

######################## Function implimentation of class Decorator ###########################

def method_decorator(func_name):
    def wrapper(*args,**kwargs):
        print(f"Executing {func_name.__name__}")
        print(func_name(*args,**kwargs))
        print(f"Executed {func_name.__name__}")
    return wrapper
def class_deco(cls_name):

    for name,address in cls_name.__dict__.items():
        if callable(address):
            setattr(cls_name,name,method_decorator(address))
    return cls_name

@class_deco
class MathOperations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
       
    def add(self):
        return f"Sum of {self.num1} + {self.num2} = {self.num1+self.num2}"
    def difference(self):
        return f"Difference of {self.num1} - {self.num2} = {self.num1-self.num2}"
    def product(self):
        return f"product of {self.num1} X {self.num2} = {self.num1*self.num2}"
    def division(self):
        return f"Division of {self.num1} / {self.num2} = {self.num1/self.num2}"
        
math=MathOperations(20,10)
math.add()
math.product()
math.division()
math.difference()

############################ Decorating a function with multiple Decorators ########################

def deco1(func1):
    def wrap1(*args,**kwargs):
        print('*'*20)
        print("Executing Wrap1")
        func1(*args,**kwargs)
        print("Executed wrap1")
        print('*'*20)
        
    return wrap1

def deco2(func2):
    def wrap2(*args,**kwargs):
        print('*'*20)
        print("Executing Wrap2")
        func2(*args,**kwargs)
        print("Executed wrap2")
        print('*'*20)

    return wrap2

def deco3(func3):
    def wrap3(*args,**kwargs):
        print('*'*20)
        print("Executing Wrap3")
        func3(*args,**kwargs)
        print("Executed wrap3")
        print('*'*20)
    return wrap3

@deco1
@deco2
@deco3
def random():
    print('#'*30)
    print('Inside Random function')
    print('#'*30)


random()