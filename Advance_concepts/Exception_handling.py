
# Default Exception Handling
"""1. wap to checks a person eligible to vote or not using exception handling"""
try:
    age=int(input('Enter your age :'))
except:
    print("Enter valid age...")
else:
    if age>=18:
        print('You are eligible to vote.....')
    else:
        print('You are not eligible to vote.....')

####################################################################################################

"""2. wap to handle a ZeroDevisionError exception when dividing a number by zero"""
try:
    num1=int(input('Enter num1 :'))
    num2=int(input('Enter num2 :'))
    res=num1/num2
except:
    print('Enter valid number....')
else:
    print(f"Result :{res}")

####################################################################################################

"""3. wap that executes an operation on a list and handles an IndexError exception if index out of range"""
collection=[10.20,30,24,89,10]
try:
    index=int(input('Enter index value :'))
    Element_at_index=collection[index]
except:
    print('Enter a valid index')
else:
    print(f"Element present at index {index} is {Element_at_index}")

####################################################################################################

"""4. wap to print factorial of a number by taking input from user using exception handling"""
try:
    num=int(input('Enter a number :'))
except:
    print('Enter a valid number....')
else:
    if num>0:
        factorial=1
        for factor in range(1,num+1):
            factorial*=factor
        print(f"Factorial of {num} is {factorial}")
    else:
        print('Enter a +ve number.....')
        
####################################################################################################

# Generic Exception Handling   

""" 1. """
try:
    collection=eval(input('Enter a dictionary :'))
    key=input("Enter a key :")
    value=collection[key]
except Exception as error_msg:
    print(error_msg)
else:
    print(f"value asssociated with {key} is {value}")
finally:
    print('Execution ends here...')

""" 2. """
# try:
