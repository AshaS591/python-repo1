#1.wap to print second maximum number among 3 numbers
num1 = int(input('Enter num1 :'))
num2 = int(input('Enter num2 :'))
num3 = int(input('Enter num3 :'))
if num1>num2:
    if num1>num3:
        if num2>num3:
            print(f"{num2} is second greatest number")
        else:
            print(f"{num3} is second greatest number")
    else:
        print(f"{num3} is second greatest number")
else:
    if num2>num3:
        if num1>num3:
            print(f"{num1} is second greatest number")
        else:
            print(f"{num3} is second greatest number")
    else:
        print(f"{num2} is second greatest number")

#2.wap to print second maximum number among 4 numbers
num1 = int(input('Enter num1 :'))
num2 = int(input('Enter num2 :'))
num3 = int(input('Enter num3 :'))
num4 = int(input('Enter num3 :'))
