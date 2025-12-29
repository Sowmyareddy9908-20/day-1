'''methods=(actions/functions)
1.instance method
should contail 1st parameter as self
defined inside a class
works on object
'''
class greet():
    def demo(self):
        self.name="somwya"
        self.age=20
g1=greet()
g1.demo()
print(g1.name)
print(g1.age)
#same code by passing arguments
class greet():
    def demo(self,name,age):
        self.name=name
        self.age=age
g1=greet()
g1.demo("sowmya",21)
print(g1.name)
print(g1.age)

'''2.class method:a class method works whith clas data
rules: first parameter should be cls
uses @classmethod'''
class student():
    college="vbjc"
    @classmethod
    def show(cls):
        print(cls.college)
s1=student()
student.show()

'''3.static method: it dont uses obj,cls and self'''
class math():
    @staticmethod
    def add(a,b):
        print(a+b)
m=math()
m.add(2,4)

#constructors: constructors is aa special instance method that create aan object data automatially when an object is created
#constructor is initialized using def__init__()
# constructors are 2 types : 1-default constructor,2-parameterized constructor
class student():
    def __init__(self):      #it is default:no values , only self
        self.name="bunny"
        self.age=10
s=student()
print(s.name)
print(s.age)
#same code using parameters
class student():
    def __init__(self,name,age):  #it is parameterized :self+values
        self.name=name
        self.age=age
s1=student("mani",17)
print(s1.name)
print(s1.age)        
