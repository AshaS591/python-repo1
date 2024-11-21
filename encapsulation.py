class student:
    degree='btech'
    __yop=2024
    def __init__(self,name,age,cgpa,stream):
        self.name=name
        self.age=age
        self.cgpa=cgpa
        self.stream=stream
    def __displayAge(self,age):
        print(f"Your age is {self.age}")
    def getAge(self):
        return self.age
    def setAge(self,age):
        self.age=age
s1=student('asha',21,9.16,'cse')
print(s1.getAge())
s1.setAge(22)
print(s1.getAge())
# print()
 


class student:
    college='presidency'
    _yop=2024
    __rollno='20201cse0787'
    def __init__(self,name,age,stream):
        self.name=name
        self.__age=age
        self.stream=stream
    def get_Age(self):
        print( self.__age)
    def set_Age(self,newage):
        self.__age=newage
object=student('asha',21,'cse')
object.get_Age()
object.set_Age(20)
object.get_Age()
print(student._student__rollno)
print(object._student__rollno)


class student:
    college='presidency'
    _yop=2024
    __rollno='20201cse0787'
    def __init__(self,name,age,stream):
        self.name=name
        self.__age=age
        self.stream=stream

    @property
    def Age(self):
        print( self.__age,student._student__rollno)
        # return student._student__rollno
        print(student._student__rollno)
    @Age.setter
    def Age(self,newage):
        self.__age=newage
object=student('asha',21,'cse')
object.Age
print(student.__dict__)
print(object.__dict__)