num=7453
denominations = [2000,500,200,100,50,20,10,1]
output={}
for denomination in denominations:
    count=num//denomination
    num%=denomination
    output[denomination]=count
print(output)


def reverse(num,temp=0):
    if num==0:
        return temp
    last = num%10
    temp=temp*10+last
    num//=10
    return reverse(num,temp)
print(reverse(89))

def factorial(num,start=1,fact=1):
    if start>num:
        return fact
    fact*=start
    return factorial(num,start+1,fact)
print(factorial(5))

def fib(num):
    if num==1:
       return 0
    elif num==2 or num==3:
       return 1
    return fib(num-1)+fib(num-2)

for num in range(1,6):
    print(fib(num))

def prime(num,start=2,is_prime=True):
    if start==num:
        return is_prime
    else:
        if num%start==0:
            is_prime=False

            return prime(num,start+1,is_prime)
        return prime(num,start+1,is_prime)
   
num=100
output=[]
for n in range(2,101):
    if prime(n):
        output.append(n)
print(output)
        
    
# 1. Print numbers from 1 to 50 using a while loop.
num=1
while num<=50:
    print(num)
    num+=1
# 2. Print all odd numbers from 1 to 30.
for num in range(1,31,2):
    print(num)
# 3. Print all even numbers from 2 to 40.
for num in range(2,41,2):
    print(num)
# 4. Print numbers from 10 to 1 in reverse order.
for num in range(10,0,-1):
    print(num)
# 5. Print the first n multiples of a given number.
n=int(input('Enter a number :'))
end=int(input('enter a end num: '))
for num in range(1,end):
    print(f'{n} X {num} = {num*n}')
# 6. Print the square of each number from 1 to 15.
for num in range(1,16):
    print(num**2)
# 7. Print the cube of each number from 1 to 10.
for num in range(1,11):
    print(num**3)
# 8. Print the first n terms of the Fibonacci series.
fib=[0,1]
num=int(input('enter n value :'))
if num==1:
    print(fib[0]) 
elif num==2:
    print(fib)
else:
    for n in range(3,num+1):
        fib.append(fib[-1]+fib[-2])
    print(fib)
# 9. Print all numbers divisible by 5 from 1 to 100.
for num in range(1,101):
    if num%5==0:
        print(num)
# 10. Print numbers from n to 1 (reverse counting).
num=10
for num in range(num,0,-1):
    print(num)
# 11. Print all two-digit numbers using a while loop.
num=0
while num>0 and num<100:
    if num<=9:
        num+=1
        
    else:
        print(num)
        num+=1
    
# 12. Print numbers that are divisible by both 3 and 7 between 1 and 100.
# 13. Print the ASCII values of characters A to Z.
# 14. Print the factorial of numbers from 1 to 5 using a while loop.
# 15. Print the sum of numbers from 1 to 100.
# 16. Print numbers from -10 to 10.
# 17. Print every third number starting from 1, up to 30.
# 18. Print the multiplication table of 7 using a while loop.
# 19. Print all numbers from 1 to n that are divisible by a user-input number.
# 20. Print the sum of squares of the first n natural numbers.



    
