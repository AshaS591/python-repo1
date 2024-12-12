#########################################################################
def decorator(func_name):
    def wrapper(*args,**kwargs):
        print('Inside wrapper....')
        for _ in range(3):
            print('-'*40)
            func_name()
            print('-'*40)
    return wrapper

@decorator
def greet():
    print('Welcome to Decorators in python')

greet()
############################ PARAMETERIZED DECORATOR ##############################################
from time import sleep
def outer(n):
    def decorator(func_name):
        def inner(*args,**kwargs):
            print('inside inner...')
            for num in range(n):
                sleep(1)
                print(num)
                func_name(num)
        return inner
    return decorator

@outer(5)
def display(n):
    print(f"calling display function for {n+1} time")

display()
##################################################################################################

"""WAP to print factorial of a number using decorator"""

def number(num):
    def whole_number(func_name):
        def calculate(*args,**kwargs):
            try:
                print(f"Calculating factorial of number : {num}")
                Factorial=func_name(*args,**kwargs)
            except Exception as msg:
                print(msg)
            else:
                print(f"Factorial of number : {num} is {Factorial}")
        return calculate
    return whole_number

@number(6)
def factorial(num:int):
    fact=1
    for num in range(1,num+1):
        fact*=num
    return fact

factorial(6)

##################################################################################################

"""WAP to print reverse of a number using decorator"""

def number(func_name):
        def display_reverse(*args,**kwargs):
            try:
                rev=func_name(*args,**kwargs)
            except Exception as msg:
                print(msg)
            else:
                print(f"Reverse of number is {rev}")
        return display_reverse

@number
def reverse(num:int):
    rev_num=0
    while num!=0:
        last_digit=num%10
        rev_num=rev_num*10+last_digit
        num//=10
    return rev_num

reverse(456)