''' Lambda functions are simple and single line functions
    * used for simple if else conditions'''

even_or_odd=lambda num:'even' if num%2==0 else "odd"
print(even_or_odd(20))

positive_or_negative=lambda num :'Positive' if num>0 else 'Negative'
print(positive_or_negative(99))

last_element=lambda collection:collection[-1]
print(last_element([1,'word','90',99,91,9]))

square_or_cube=lambda num:num**3 if num%2==0 else num**2
print(square_or_cube(6))

message=lambda :"my name is asha"
print(message())

length=lambda collection:len(collection) 
print(length([10,'word',10+0j,90.12,'100']))

greatest_among_two=lambda num1,num2:num1 if num1>num2  else num2
print(greatest_among_two(10,20))

# wap to return one more even number if the user entered number is even number otherwise return one more odd number
other_even_or_odd=lambda num:(num,num+2) if num%2==0 else (num,num+2)
print(other_even_or_odd(11))