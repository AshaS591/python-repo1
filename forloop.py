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

