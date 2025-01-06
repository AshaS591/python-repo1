''' Creating text file'''
# file=open('movies.txt','x')
# file.close()

''' writing into the text file'''

file=open('movies.txt','w')
file.writelines(['1.kantara\n','2.bahubali\n','3.kirik party'])

# file.close()

''' appending new data into the text file at end'''

# file=open('movies.txt','a')
# file.writelines(['3.lakki bhaskar\n','4.max\n'])

# file.close()

''' reading from the file '''
# file=open('movies.txt','r')
# print(file.read())

# file.close()

# file=open('movies.txt','r')
# print(file.read(20))

# file.close()

# file=open('movies.txt','r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())


# file.close()

# file=open('movies.txt','r')
# print(file.readlines())
# file.close()

''' wap to print a movie name in a file which has k as 3rd character'''
file=open('movies.txt','r')
for line in file.readlines():
    if line[2]=='k':
        print(line)
file.close()

''' wap to find no of characters, no of words or number of lines in Python text file'''

file=open('movies.txt')
count_characters=len(file.read())
print(count_characters)
file.seek(0)
count_words=len(file.read().split())
print(count_words)
file.seek(0)

count_lines=len(file.readlines())
print(count_lines)
file.close()

'''Write a statement to write the string 'Welcome! Please have a seat' in the file wel.txt, that has not yet been created.'''
file=open('wel.txt','w')
file.write('Welcome! Please have a seat\n')
file.close()
