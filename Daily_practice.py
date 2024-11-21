# 21/11/2024 (every day five programs)
#1 wap to check whether a number is armstrong no or not using while loop
number=int(input('enter a number :'))
num=number
armstrong_num=0
while num!=0:
    last_digit=num%10
    armstrong_num+=last_digit**len(str(number))
    num//=10
if number==armstrong_num:
    print(f"{number} is armstrong number...")
else:
    print(f"{number} is not armstrong number...")

#2 wap to find factorial of a number using recursive functions
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1) 
number=int(input('Enter a number :'))
print(f"factorial of {number} is {factorial(number)}")

#3 wap to  create dictionary where keys are each characters in a sentance and values are numbers of occurances of characters using for loop
sentence=input('Enter a sentance :')
collection={}
for each_char in sentence:
    if each_char in collection:
        collection[each_char]+=1
    else:
        collection[each_char]=1
print(collection)

#4 wap to reverse a string without using builtin method
string=input('Enter a string :')
index=0
reverse=''
while index<len(string):
    char=string[index]
    reverse=char+reverse
    index+=1
print(f'Reverse of {string} : {reverse}')

#5 wap to get the following output
# input ='hai hello good morning'
# output={'hai':'a','hello':'l','good':'gd','morning':'n'}

line=input('Enter a sequence of words :')
words=line.split()
output={}
for word in words:
    if len(word)%2==0:
        output[word]=word[0]+word[-1]
    else:
        output[word]=word[len(word)//2]
print(output)