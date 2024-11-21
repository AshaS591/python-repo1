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


