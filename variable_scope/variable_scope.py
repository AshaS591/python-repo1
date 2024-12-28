''' Variable Scope '''

num=20
def display(num):
    print(num)
display(num)

num=10
def display():
    num=30
    print(num)
    def get_num():
        #print(num)#---->throws error i.e cannot access local variable 'num' where it is not associated with a value
        num=20
        num+=20
        print(num)
    print(num)
    get_num()
print(num)
display()

name='asha'
def display():
    # print(name)---->throws error i.e cannot access local variable 'num' where it is not associated with a value
    # name+=" s" ---->throws error i.e cannot access local variable 'num' where it is not associated with a value
    name='Asha'
    print(name)
    def display_name():
        global name
        name='Asha S'
        print(name)
    print(name)
    display_name()
display()
print(name)

items=[10,20]
def display():
    global items
    items.append(40)
    print(items)
    def display_items():
        # print(items)
        items=[10,46,60]
        print(items)
    display_items()   
display()
print(items)

num=30
def display():
    print(num)
display()

num1=20
num2=30
def outer():
    print(num1)
    num1=90
    def inner():
        print(num1)
    inner()
outer()

num=10
def outer():
    num=30
    print(num)
    def inner():
        global num
        num+=10
        print(num)
    inner()
print(num+10)
outer()
print(num)

name='Name'
def display():
    global name
    name='Asha'
    def inner():
        global name
        name+=" s"
    print(name)
    inner()
print(name)
display()
print(name)

num1=20
def outer():
    global num1
    num1+=90
    print(num1)
    def inner():
        # num1=50
        print(num1)
    inner()
print(num1)
outer()

num1=20
def outer():
    num1=10
    num1+=90
    print(num1)
    def inner():
        # num1=50
        print(num1)
    inner()
print(num1)
outer()