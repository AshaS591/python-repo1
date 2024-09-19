#1.wap a program to print 'while loop' for 10 times
count=0
while count<10:
    print('while loop')
    count+=1

#2.wap a program to print first n natural numbers in one line
first=1
last=int(input('enter n value :'))
while first<=last:
    print(first,end=' ')
    first+=1

#3.wap a program to print first n whole numbers in one line
first=0
last=int(input('\nenter n value :'))
while first<last:
    print(first,end='   ')
    first+=1

#4.wap a program to print even numbers between 1 to 50
even=1
print("\nEven numbers")
while even<=50:
    if even%2==0:
        print(even)
    even+=1

#5.wap a program to print odd numbers between 1 to 50
odd=1
print("Odd numbers")
while odd<=50:
    if odd%2!=0:
        print(odd)
    odd+=1
#6.wap a program to print countdown of a game
count=10
print("\nstart countdowning")
while count>=0:
    print(count)
    count-=1

#7.wap to print items in a tuple using while loop
tuple1=eval(input('enter tuple of periodic elements'))
items=0
while items<len(tuple1):
    print(tuple1[items])
    items+=1

#8.wap to print items in a list using while loop
list1=eval(input('enter list of grocery items'))
items=0
while items<len(list1):
    print(list1[items])
    items+=1

#9.wap to print square of a  n numbers using while loop
square=0
last_square=int(input('enter last square number '))
while square<=last_square:
    print(square**2)
    square+=1

#10.wap to print cube of a  n numbers using while loop
cube=0
last_cube=int(input('enter last cube number '))
while cube<=last_cube:
    print(cube**3)
    cube+=1
#11.wap to print first 10 integers and their squares using while loop
first=1
last=10
while first<=last:
    print(first,first*first,sep=' ')
    first+=1
#12.write a while loop statement to print the following series 105,98,91,....,7
end=7
start=105
while start>=end:
    print(start)
    start-=7
#13.wap to print sum of first 10 natural numbers
sum=0
start=1
end=10
while start<=end:
    sum+=start
    start+=1
print(sum)

#14. wap to print sum of first 10 even numbers
sum=0
even=2
while even<=20:
    if even%2==0:
        sum+=even
    even+=2
print(sum)

#15.wap to print all even numbes that falls b/w two numbers (exclusive both numbers) entered by the user using while loop
start=int(input('enter starting number :'))
end=int(input('enter ending number :'))
while start<end:
    if start%2==0:
        print(start)
    start+=1
#16.wap to find sum of the digits of a number accepted from the user
sum=0
index=0
num=input('enter the number')
while index<len(num):
    sum+=int(num[index])
    index+=1
print(sum)
   # or
sum=0
remainder=0
num=int(input('enter the number'))
while num!=0:
    remainder=num%10
    sum=sum+remainder
    num//=10
print(sum)

#17.wap to find reverse of a number accepted from the user
reverse=0
remainder=0
num=int(input('enter number :'))
while num!=0:
    remainder=num%10
    reverse=reverse*10+remainder
    num//=10
print(reverse)

#18.wap to print the product of the digits of a number accepted from the user
num1=int(input('enter a number'))
product=1
remainder=0
while num1!=0:
    remainder=num1%10
    product=product*remainder
    num1//=10
print(product)

#19.wap to print the factorial of a number till n terms (accept input from user) using while loop
num=int(input('enter number'))
fact=1
start=1
if num>0:
    if num==0 or num==1:
        print(fact)
    else:
        while start<=num:
            fact=fact*start
            start+=1
print(fact)



