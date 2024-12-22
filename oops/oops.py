class house:
    window=4
    doors=0
    def colors(self,doors):
        self.doors=doors
        print(self.doors)
   
house1=house()
house2=house()
print(house1)
house1.doors=7
print(house1.doors)
house1.colors(10)

###########################################################

class Colors:
    color1='black'
    color2='white'
    color3='pink'
    def dis_colors(self):
        print(Colors.__dict__)
color=Colors()
color.dis_colors()  

##############################################################

class Person:
    name='Asha S'
    country='India'
    dob="14/01/2003"
    def __init__(self,age):
        self.age=age
    def display_details(self):
        print(f'Name : {Person.name}\nCountry : {Person.country}\nDOB : {Person.dob}\nAge : {self.age}')
asha=Person(21)
print(asha.__dict__)
print(Person.__dict__)
asha.display_details()

#############################################################################
        
class Circle:
    def area(self,radius):
        self.pi=3.14
        self.radius=radius
        self.area= self.pi * (self.radius**2)
        print(f'Area of circle with radius {self.radius} is {self.area}')
    def peimeter(self,radius):
        self.rad=radius
        self.peimeter=2 * self.pi * self.rad
        print(f'Perimeter of circle with radius {self.rad} is {self.peimeter}')
c1=Circle()
c1.area(10)
c1.peimeter(20)

######################################################################
print()

class ArithmeticOperations:
    print('Performing Arithmetic Operations:')
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(f'{self.num1} + {self.num2} = {self.num1+self.num2}')
    def diff(self):
        print(f'{self.num1} - {self.num2} = {self.num1-self.num2}')
    def product(self):
        print(f'{self.num1} * {self.num2} = {self.num1*self.num2}')
    def div(self):
        print(f'{self.num1} / {self.num2} = {self.num1/self.num2}')
    def mod(self):
        print(f'{self.num1} % {self.num2} = {self.num1%self.num2}')
math=ArithmeticOperations(20,10)
math.add()
math.diff()
math.div()
math.product()
math.mod()
        