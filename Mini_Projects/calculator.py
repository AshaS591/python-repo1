import os
def add(num1,num2):
    print(f'Sum of {num1} and {num2} is {num1+num2}')
    return num1+num2
def diff(num1,num2):
    print(f'Difference of {num1} and {num2} is {num1-num2}')
    return num1-num2
def product(num1,num2):
    print(f'Product of {num1} and {num2} is {num1*num2}')
    return num1*num2
def true_division(num1,num2):
    print(f'True division of {num1} and {num2} is {num1/num2}')
    return num1/num2
def remainder(num1,num2):
    print(f'Modulus of {num1} and {num2} is {num1%num2}')
    return num1%num2
def floor_division(num1,num2):
    print(f'Floor division of {num1} and {num2} is {num1//num2}')
    return num1//num2

operations={'+':add,'-':diff,'*':product,'/':true_division,'%':remainder,'//':floor_division}

# choice=input("...Here you can perform arithmetic operations ...\nDo you like to perform any operation,\nif yes type 'y' otherwise type 'n' to exit :\n")
# if choice=='y':
def one_more_check():
    num1=int(input('Enter first number :\n')) 
    for symbol in operations:
            print(symbol)
    flag=True
    while flag: 
        operator=input('Pick an operation :\n')
        num2=int(input('Enter second number :\n'))
        calcy=operations[operator]
        output=calcy(num1,num2)
        print(f"{num1} {operator} {num2} = {output}")
        one_more_time=input(f"Enter '1' for continue operation with {output} or '2' for start new operation or '3' for exit")
        if one_more_time=='1':
            output
        elif one_more_time=='2':
            flag=False
            os.system('cls')
            one_more_check()
        else:
            flag=False
            print('-----end-----')
one_more_check()


        



            
            
    
            

    