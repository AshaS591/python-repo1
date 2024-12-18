############ comprehension ##########

# 1. wap to create numbers list by taking input from user using comprehension
end=int(input("Enter an endpoint :"))
numbers=[num for num in range(end+1)]
print(numbers)

# 2.wap to create even list by taking input from user using comprehension
end=int(input('Enter an endingpoint :'))
even_list=[ num  for num in range(0,end+1,2)]
print(even_list)

# 3. wap to create list ,if item last second character is vowel by taking another collection from the user using comprehension
try:
    items=eval(input('Enter a collection :'))
    new_list=[item  for item in items if item[-2] in 'aeiouAEIOU']
except Exception as err_msg:
    print(err_msg)
else:
    print(new_list)

# 4. wap to create a list by taking another number collection from user if num is even append its square ,if num is odd append cube of that number

try:
    numbers=eval(input('Enter a number collection :'))
    new_numbers=[num**2 if num%2==0 else num**3 for num in numbers ]
except Exception as err_msg:
    print(err_msg)
else:
    print(new_numbers)


