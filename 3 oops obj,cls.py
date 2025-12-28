'''
oops is a programming appoach that uses classes and objects to represent real world entities
'''
#class: class is a blueprint used to create objects,it define the properties(data) and methods(functions) that the object will have

class student(): # in this code there is not oop ex bcoz there is no functions and methods 
    print("hello student is studying")
s1=student()

#using functions : it is local variable which is temporary
class greet():           # class is greet
    def demo(self):       # method is demo
        name="sowmya"
        roll_no=23
        print(name) 
        print(roll_no)
g1=greet()               # g1 is object of class greet
g1.demo()                

#using function: priinintg inside the method,,,it permanently stored in the object bcoz we used self
class greet():                
    def demo(self):
        self.name="bunny"
        self.roll=21
        print(self.name)
        print(self.roll)
        g1=greet()
g1.demo()


class Greet:
    def demo(self):
        self.name = "bunny"
        self.roll = 21
g1 = Greet()
g1.demo()
print(g1.name)   # works printing using object name becose self works only instde the method
print(g1.roll)   # works
