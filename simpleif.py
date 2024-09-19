#1. wap to check if the first character of the user enter word is uppercase character
word=input('enter a word : ')
first_character=word[0]
if first_character.isupper():
    print(f"{word} is starting uppercase letter")

#2. wap to check if the user entered number is positive no
number=int(input("enter a number :"))
if number>0:
    print(f"{number} is +ve number")

#3. wap to check if the user entered number is two digit no
number=int(input("enter a number :"))
if (number>9 and number<100) or (number<-9 and number>-100):
    print(f"{number} is two digit number")

#4. wap to check if the user entered number is 3 digit no
number=int(input("enter a number :"))
if (number>99 and number<1000) or (number<-99 and number>-1000):
    print(f"{number} is three digit number")

#5. wap to check if the user entered number is multiple of 5
number=int(input("enter a number :"))
if number%5==0:
    print(f"{number} is multiple of 5 ")

#6. wap to check if the user entered number is multiple of 5 and divivible by 3
number=int(input("enter a number :"))
if number%5==0 and number%3==0:
    print(f"{number} is multiple of 5 and divivible by 3 ")

# 7. wap to check if the user entered set is subset of other set
set1=eval(input("enter set1 :"))
set2=eval(input("enter set2 :"))
if (set1<set2 or set2<set1):
    print("one of the set is subset of other set")

# 8.wap to check if the user entered word is palindrome
word=input("enter a word :")
reversed_word=word[::-1]
if reversed_word==word:
    print(f"{word} is palindrome.....")

# 9.wap to check if the weather is sunny
weather=input('Enter the weather condition : ')
if weather=='sunny':
    print('All of the childrens will play in the playground')
print("you have oppurtunity to play in sunny days")

# 10.wap to check if the character is vowel
character=input('Enter a character : ')
if character in "aeiouAEIOU":
    print(f"{character} is vowel")
print("try with some other character...")

# 11.wap to check if the character is consonant
character=input('Enter a character : ')
if character not in "aeiouAEIOU":
    print(f"{character} is consonant")
print("try with some other character...")

# 12.wap to check if the user entered number is even
number=int(input('enter a number :'))
if number%2==0:
    print(f"{number} is a even number...")

# 13.wap to check if the user entered value is single valued datatype
user_input=eval(input("enter a value :"))
type_of_value=type(user_input)
if type_of_value in [int,float,complex,bool]:
    print(f"{user_input} is single valued datatype of type {type_of_value}")