#1.wap to extract all the numeric values in a given collection
collection=eval(input('Enter a collection :'))
numbers=[]
for item in collection:
    if type(item) in [int,float,complex]:
        numbers.append(item)
print(f"All numbers in a collection are :{numbers}")

#2.wap to extract all lowercase characters in a given string using for loop
string=input('Enter a string :')
lower=''
for char in string:
    if char.islower():
        lower+=char
print(f"Lowercase characters are {lower}")

#3.wap to display a dictionary whose keys are words of a sentence  and the values are the length of each word using for loop
sentence=input("Enter a sentence :")
output={}
words=sentence.split()
for word in words:
    if word not in output:
        output[word]=len(word)
print("Dictionary :",output)

#4.wap to mimic len function
string=input('Enter a string :')
count=0
for char in string:
    count+=1
print(f"Length of string {string} is {count}")

#5.wap to display a largest number in a given collection
collection=eval(input('Enter a collection of numbers :'))
max=0
for num in collection:
    if num>max:
        max=num
print(f"Largest number of a collection is {max}")

#6.wap to print range of natural numbers entered by the user using for loop
num=int(input('Enter the ending number :'))
for nums in range(num):
    print(nums)

#7.wap to print even numbers by using range entered by the user
last_num=int(input('Enter a number :'))
for even in range(last_num):
    if even%2==0:
        print(even)

#8.wap to print square of a numbers by using range entered by the user
last_num=int(input('Enter a last number :'))
for num in range(last_num):
    print(f"Square of {num} is {num**2}")

#9.wap to print multiples of 5 and 10 by using range entered by the user
last_num=int(input('Enter a last number :'))
for num in range(last_num):
    if num%5==0 and num%10==0:
        print(f"{num} is multiple of both 5 and 10")

#10.wap to print countdown of a game using for loop
start=int(input("Eneter a countdown starting number :"))
for count in range(start,-1,-1):
    print(count)

