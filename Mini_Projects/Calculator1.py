import os
def add(num1,num2):  
    return num1+num2
def diff(num1,num2): 
    return num1-num2
def product(num1,num2):
    return num1*num2
def true_division(num1,num2):   
    return num1/num2
def remainder(num1,num2):
    return num1%num2
def floor_division(num1,num2):
    return num1//num2

operations={'+':add,'-':diff,'*':product,'/':true_division,'%':remainder,'//':floor_division}
def calculator():
    num1=int(input('Enter first number :\n'))
    for operator in operations:
        print(operator)
    continue_flag=True
    while continue_flag:
        symbol=input('Pick an operation :\n')
        num2=int(input('Enter second number :\n'))
        calculation=operations[symbol]
        output=calculation(num1,num2)
        print(f'{num1} {symbol} {num2} = {output}')
        should_continue=input(f"Enter 'y' to continue with {output} or 'n' to start a new calculation or 'x' to exit" ).lower()
        if should_continue=='y':
            num1=output
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print('....End....')
calculator()
        

