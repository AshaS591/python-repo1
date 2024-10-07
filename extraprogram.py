sentence=input("Enter a word :")
words=sentence.split()
piglatin=''
count=0
vowels='AEIOUaeiou'
for word in words:
    for index in range(1,len(word)):
        if word[0] in vowels:
            piglatin+=word+'way'
        elif word[0] not in vowels and word[index] in vowels:
            count+=1
            if count==1:
                piglatin+=word[index+1:len(word)]+word[:index]+'ay'
        else:
            for char in word:
                if char not in vowels:
                    piglatin+=word+'ay' 
print(piglatin)







# if word[0] in 'AEIOUaeiou':
#     piglatin=word+'way'
# elif word[0] not in 'AEIOUaeiou':
#     for index in range(1,len(word)):
#         if word[index] in 'AEIOUaeiou':
#             count+=1
#             if count==1:
#                 piglatin=word[index+1:len(word)]+word[0:index]+'ay'
# else:
#     for index1 in range(len(word)):
#         if word[index1] not in 'AEIOUaeiou':
#             piglatin=word+'ay'
# print(piglatin)

