#1.to check if the user entered no is even 
# if even print square of a number
# else print cube of a number
num=int(input("enter the number :"))
if num%2==0:
    print(f"{num} is a even number and its square is:{num**2}")
else :
    print(f"{num} is not a even number and its cube is:{num**3}")

############################################################################

#2.wap to check if the user entered character is special character or not
char=input('enter a character :')
if char.isalnum():
    print(f"{char} is not special character")
else :
    print(f"{char} is  special character")
char=input('enter a character :')
if 'a'<=char<='z' or 'A'<=char<='Z' or "0"<=char<="9":
    print(f"{char} is not special character")
else :
    print(f"{char} is  special character")
#3.wap to check if user entered no is +ve or -ve
num=int(input("enter a number :"))
if num>=0:
    print(f"{num} is positive number")
else :
    print(f"{num} is negative number")
    
############################################################################

#4.wap to check if user entered character is upper case or lower case
char=input("enter a chararter :")
if "A"<=char<="Z" :
    print(f"{char} is upper case")
else :
    print(f"{char} is lower case")

############################################################################

#5.wap to check if user entered value is mutable datatype or immutable datatype
data=eval(input('Enter the value :'))
if type(data) in (list,set,dict):
    print(f"{data} is mutable datatype")
else :
    print(f"{data} is immutable datatype")

############################################################################

#6.wap to check if the weather is sunny or rainy
weather=input('Enter the weather condition : ')
if weather=='sunny' or weather=='SUNNY':
    print(f"It's a {weather} day ")
else:
    print(f"It's a {weather} day ")

############################################################################

#7.wap to check if the working shift is day or night
shift_of_day=input('enter the working shift :')
if shift_of_day=='day' or shift_of_day=='DAY':
    print(f"you have work in {shift_of_day} shift")
else:
    print(f"you have work in {shift_of_day} shift")
    
############################################################################
 
#8.wap to check if the user entered data is single valued data type or a collection
data=eval(input("enter the vlaue or collection :"))
if type(data) in [int,float,bool,complex]:
    print(f"{data} is single valued datatype")
else:
    print(f"{data} is collection or multi valued datatype")

############################################################################

#9.wap to check if the user entered character is vowel or consonant
char=input('enter the character :')
if char in 'aeiouAEIOU':
    print(f"{char} is vowel")
else:
    print(f"{char} is consonant")

############################################################################

#10.wap to check if the user entered collection contains 5 or lessthan 5 elements
collection=eval(input("enter a collection :"))
if len(collection)<=5:
    print(f"{collection} has 5 or lessthan 5 elements")
else:
    print(f"{collection} has morethan 5 elements")

############################################################################

#11.wap to check if the user entered word is keyword or not
import keyword
keywords=keyword.kwlist
word=input("enter a word :")
if word in keywords:
    print(f"{word} is a keyword")
else:
    print(f"{word} is not a keyword")
    print(keywords)