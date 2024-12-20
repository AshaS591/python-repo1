###########################################################

def display():
    print("This is miscelleneous function....")
function=display
function()

############################################################
number=10
numbers=[]
def display_list():
    for num in range(number):
        numbers.append(num)
    print(numbers)
func=display_list
func()

#############################################################

def factorial(number):
    fact=1
    for num in range(1,number+1):
        fact*=num
    print(f'Factorial of {number} is {fact}')
factorial_num=factorial
factorial_num(5)

################################################################