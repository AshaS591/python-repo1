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
        print(line,end='')
file.close()
