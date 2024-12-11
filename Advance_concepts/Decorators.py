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
