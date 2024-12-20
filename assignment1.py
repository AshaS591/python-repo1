
###################################################################################################################################################

# 1 . Write a program to print the following using while loop
#  a. First 10 Even numbers
#  b. First 10 Odd numbers
#  c. First 10 Natural numbers
#  d. First 10 Whole numbers

even=[]
odd=[]
natural=[]
whole=[]
num=0
while num<20:
    if num%2==0:
        even.append(num)
    if num%2!=0:
        odd.append(num)
    if num>=1 and num<11:
        natural.append(num)
    if num>-1 and num<10:
        whole.append(num)
    num+=1
print(f"Even numbers are :{even}")
print(f"Odd numbers are :{odd}")
print(f"Natural numbers are :{natural}")
print(f"Whole numbers are :{whole}")

###################################################################################################################################################

# 2. Write a program to print first 10 integers and their squares using while loop

num=0
integer=[]
squares=[]
while num<=10 and num>=0:
    integer.append(num)
    squares.append(num*num)
    num+=1
print(f"Integers :{integer} and their squares :{squares}")

###################################################################################################################################################

# 3. Write while loop statement to print the following series: 10, 20, 30 … … 300

num=0
series=[]
while num<300:
    num+=10
    series.append(num)
print(f"series :{series}")

###################################################################################################################################################

#  4. Write a while loop statement to print the following series 105, 98, 91 ………7.

num=105
series=[]
while num>6:
    series.append(num)
    num-=7
print(f"series :{series}")

###################################################################################################################################################

#  5.Write a program to print first 10 natural number in reverse order using while loop.

num=10
natural=[]
while num>0:
    natural.append(num)
    num-=1
print(f"Natural number are :{natural}")

###################################################################################################################################################

#  6. Write a program to print sum of first 10 Natural numbers.

num=0
sum=0
while num<=10:
    sum+=num
    num+=1
print(f"Sum of first 10 natural numbers is :{sum}")

###################################################################################################################################################

# 7. Write a program to print sum of first 10 Even numbers.

num=0
evensum=0
while num<=20:
    if num%2==0:
        evensum+=num
    num+=1
print(f"Sum of first 10 even numbers is :{evensum}")

###################################################################################################################################################

#  8. Write a program to print table of a number entered from the user.
number=int(input('Enter a number :'))
num=1
while num<=10:
    print(f"{number} X {num} = {number*num}")
    num+=1

###################################################################################################################################################

#  9. Write a program to print all even numbers that falls between two numbers (exclusive both
#  numbers) entered from the user using while loop.
start=int(input('Enter starting number :'))
end=int(input('Enter ending number :'))
num=start+1
even=[]
while num<end:
    if num%2==0:
        even.append(num)
    num+=1
print('Even numbers :',even)

###################################################################################################################################################

#  10. Write a program to check whether a number is prime or not using while loop.
# num=int(input('Enter a number :'))
prime=True
factor=2
while factor<=num/2:
    if num%factor==0:
        prime=False
    factor+=1
if prime==True:
    print('prime')
else:
    print('not a prime')

###################################################################################################################################################

# 11.Write a program to find the sum of the digits of a number accepted from the user.

number=int(input('Enter a number :'))
sum=0
while number!=0:
    last_digit=number%10
    sum+=last_digit
    number//=10
print(sum)

###################################################################################################################################################


# 12. Write a program to find the product of the digits of a number accepted from the user

number=int(input('Enter a number :'))
product=1
while number!=0:
    last_digit=number%10
    product*=last_digit
    number//=10
print(product)

###################################################################################################################################################

#  13. Write a program to reverse the number accepted from user using while loop.
rev=0
num=int(input('Enter a number :'))
while num!=0:
    last_digit=num%10
    rev=rev*10+last_digit
    num//=10
print(rev)

# Write a program to display the number names of the digits of a number entered by user,
#  for example if the number is 231 then output should be Two Three One
