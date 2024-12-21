'''1 wap to find factorial of a number using recursive functions'''
def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)
num=int(input('Enter a number :'))
print(f"Factorial of {num} is {factorial(num)}")

'''2 wap to find fibonocci series of a number using recursive functions'''
def fibonacci(num):
    if num<=0:
        return 'Try with positive number'
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)
num=int(input('Enter a number :'))
print(fibonacci(num))

num=13
prime=False
for number in range(2,num+1):
    if num%2!=0:
        prime=True
        break
print(prime)

'''3 wap to check for prime number using recursive functions'''

def isprime(num,temp=2,prime=True):
    if num==1:
        return False
    elif temp==num:
        return prime
    else:
        if num%temp==0:
            prime=False
        return isprime(num,temp+1,prime)
print(isprime(10))
    
# 4. wap to print sum of natural numbers from 1 to 100 using recursive functions
def natural_sum(num): 
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return num+natural_sum(num-1)
number=int(input('Enter a number :'))
print(natural_sum(number))

'''5.wap to display a dictionary where the keys are the characters in a string and its values are its number of occurances'''
def get_dict(string,count=0,output={}):
    
    if len(string)==1:
        output[string]=1
    elif count==len(string):
        return None
    else:
        if string[count] not in output:
            output[string[count]]=1
            get_dict(string,count+1,output)
        else:
            output[string[count]]+=1
            get_dict(string,count+1,output)
        return output
print(get_dict('kalamandir'))

'''6.wap to display a dictionary where the keys are the characters ina string and its values are its ascii values'''
def get_dict(string,output={},index=0):
    if index==len(string):
        return None
    else:
        output[string[index]]=ord(string[index])
        get_dict(string,output,index+1)
    return output
string=input('Enter a string :')
print(get_dict(string))

'''7.wap to check for a number pallindrome using recursive function'''
def num_pallindrome(num,rev=0):
    if num==0:
        return rev
    else:
        last_digit=num%10
        rev=rev*10+last_digit
        return num_pallindrome(num//10,rev)     
num2=int(input('Enter a number : '))
res=num_pallindrome(num2)
if num2==res:
    print('Palindrome')
else:
    print("not palindrome...")

# 8.wap to extract all the numeric values in a given items
def extract_numeric(items,index=0,output=[]):
    if index==len(items):
        return None
    else:
        if type(items[index]) in [int,float,complex]:
            output.append(items[index])
            extract_numeric(items,index+1,output)
        else:
            return  extract_numeric(items,index+1,output)
    return output
items=eval(input('Enter a items :'))
print(extract_numeric(items))

'''9.wap to extract all lowercase characters in a given string using recursive functions'''
def extract_lowercase_char(string,index=0,lower=''):
    if index==len(string):
        return None
    else:
        if string[index].islower():
            lower+=string[index]
            extract_lowercase_char(string,index+1,lower)
        else:
            return extract_lowercase_char(string,index+1,lower)
    return lower
print(extract_lowercase_char('MadHYapRaDeSH'))

'''
10. wap to find gcd of two numbers

'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(2,6) ) 

# 10.wap to display a dictionary whose keys are words of a sentence  and the values are the length of each word 





