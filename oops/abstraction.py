from abc import ABC,abstractmethod
class Car(ABC):
    def wiper(self):
        print('wipe the windShield...')
    @abstractmethod
    def accelerator(self):
        ...

    @abstractmethod
    def brake(self):
        ...
class Lamorghini(Car):
    def go_home(self):
        print('gaya tata goodbye...')
    def accelerator(self):
        print('High speed accelerator...')
    def brake(self):
        print('Using brimbo brakes for best quality... ')

car=Lamorghini()
car.accelerator()
# car=Car() Can't instantiate abstract class Car without an implementation for abstract methods 'accelerator', 'brake'