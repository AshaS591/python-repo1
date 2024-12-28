'''
Types of arguments
1.variable arguments
2.keyword arguments
'''

def add(num1,num2):
    return num1+num2
res=add(20,30)
print(res)

def details(name,age):
    print(f"Name :{name},Age :{age}")
details(20,'asha')

def login(user_name,password):
    return f"User name is : {user_name},password is {password}"
res=login(1234,'ashas')
print(res)