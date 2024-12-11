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