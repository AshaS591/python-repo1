class mamal:
    def __init__(self,name):
        self.name=name
    def blood_type(self):
        print(f"{self.name} is worm blooded")
    def heart_chambers(self):
        print(f"{self.name} has four chambers in heart")
        
class tiger(mamal):
    ...
animal=tiger('tiger')
print(animal.name)
animal.blood_type()
animal.heart_chambers()

################################################################################

class Shapes:
    def area(self):
        print('This is Area method...')
    def perimeter(self):
        print('This is perimeter method...')
class Circle(Shapes):
    def area(self,radius):
        self.area=3.14 * radius**2
        print('Area of circle is :',self.area)
    def perimeter(self,radius):
       self.perimeter=2 * 3.14 *radius
       print('Perimeter of circle is :',self.perimeter)
class Square(Shapes):
    def area(self,side):
        self.area=side ** 2
        print('Area of circle is :',self.area)
    def perimeter(self,side):
       self.perimeter= 4 *side
       print('Perimeter of circle is :',self.perimeter)
shape=Shapes()
shape.area()
shape.perimeter()
circle1=Circle()
circle1.perimeter(10)
circle1.area(10)
square=Square()
square.area(10)
square.perimeter(4)
