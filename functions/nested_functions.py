def outer():
    def inner():
        print('This is inner function...')
    return inner
var=outer()
var()

def number(num):
    def factorial():
        fact=1
        for number in range(1,num+1):
            fact*=number
        print(f'Factorial of {num} is {fact}')
    return factorial
factorial_no=number(7)
factorial_no()
       
   