
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

choice=input("...Here you can perform arithmetic operations ...\nDo you like to perform any operation,\nif yes type 'y' otherwise type 'n' to exit :\n")
if choice=='y':
        num1=int(input('Enter first number :\n'))  

        def one_more_check():
            
            global num1
            print('+\n-\n*\n/\n%\n//')
            operator=input('Pick an operation :\n')
            num2=int(input('Enter second number :\n'))
            for operator in operations:
                result=operations[operator](num1,num2)
                print(f'Do you want to perform operation on {result}\n')
                while True:
                    one_more_time=input("Type '1' for yes, '2' for exit :\n")
                    if one_more_time=='1':
                        num1=result
                        one_more_check()
                    elif one_more_time=='2':
                        break

        one_more_check()




            
            
    
            

    