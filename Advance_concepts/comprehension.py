# ############ comprehension ##########

#************************** list comprehension *****************************

# # 1. wap to create numbers list by taking input from user using comprehension
# end=int(input("Enter an endpoint :"))
# numbers=[num for num in range(end+1)]
# print(numbers)

# # 2.wap to create even list by taking input from user using comprehension
# end=int(input('Enter an endingpoint :'))
# even_list=[ num  for num in range(0,end+1,2)]
# print(even_list)

# # 3. wap to create list ,if item last second character is vowel by taking another collection from the user using comprehension
# try:
#     items=eval(input('Enter a collection :'))
#     new_list=[item  for item in items if item[-2] in 'aeiouAEIOU']
# except Exception as err_msg:
#     print(err_msg)
# else:
#     print(new_list)

# # 4. wap to create a list by taking another number collection from user if num is even append its square ,if num is odd append cube of that number

# try:
#     numbers=eval(input('Enter a number collection :'))
#     new_numbers=[num**2 if num%2==0 else num**3 for num in numbers ]
# except Exception as err_msg:
#     print(err_msg)
# else:
#     print(new_numbers)

# # 5. wap to create list with all integers 

# try:
#     numbers=eval(input('Enter a collection :')) 
#     new_list=[num for num in numbers if type(num)==int]
# except Exception as err_msg:
#     print(err_msg)
# else:
#     print(new_list)

# 6. wap to create a list ,if item is string datatye and item contains only alphabets and length is greaterthan 5

# try:
#     items=eval(input('Enter a collection which supports indexing :'))
#     new_list=[item for item in items if type(item)==str if item.isalpha() if len(item)>5]
# except Exception as err_msg:
#     print(err_msg)
# else:
#     print(new_list)

# 7. wap to create a list where each item is word in sequence and convert to uppercase only if it contains only alphabet then append to the list

# sequence=input("Enter a sequence :")
# words=sequence.split()
# try:
#     new_list=[word.upper() for word in words if word.isalpha()]
# except Exception as err_msg:
#     print(err_msg)
# else:
#     print(new_list)

# 8. wap to create a list if item is string then reverse it and append to the list

# try:
#     items=eval(input("Enter a collection :"))
#     new_list=[item[::-1] for item in items if type(item)==str]
# except Exception as err_msg:
#     print(err_msg)
# else:
#     print(new_list)

# 9.
nested=[[num for num in range(4) ] for num in range(5)]
print(nested)

#10.
even_index_collection=[[num for num in range(3)] for num in range(10) if num%2==0]
print(even_index_collection)

#11.
even_numbers_collection=[[num1 for num2 in range(3)] for num1 in range(10) if num1%2==0]
print(even_numbers_collection)
# ***************************** Set Comprehension ***************************** 

# 1.
numbers={num  for num in range(10)}
print(numbers)

# 2.
even_set={num for num in range(10) if num%2==0}
print(even_set)

# 3.
odd_set={num for num in range(10) if num%2==1}
print(odd_set)

# 4
number=int(input('Enter number :'))
squares_set={num**2 for num in range(number)}
print(squares_set)

# 5.
cube_set={num**3 for num in range(15)}
print(cube_set)

# 6. 
squares_and_cubes={num**2 if num%2==0 else num**3 for num in range(10)}
print(squares_and_cubes)

# 7.
string='collection'
vowels={char for char in string if char in 'aeiouAEIOU'}
print(vowels)

# 8.
collection=['artist',True,90,'actor','drama',0,9.23,'role','director']
strings={item for item in collection if type(item)==str}
print(strings)