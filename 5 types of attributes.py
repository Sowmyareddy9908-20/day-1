'''2 types of attributes : an attribute is just a variable inside a class/obj : 
self.name="bunny" self is attr

1:instance att: each object has it's own data
attribute that belongs to only 1 object
'''
class student():
    def __init__(self,name): 
        self.name=name     #instance attribute
s1=student("sowmya")   #each objhas its own name
s2=student("bunny")
print(s1.name)
print(s2.name)

#2: class attribute: created for the all oobject- it is return instde class and above method
class stud():
    car="bmw" #class attribute
    def __init__(self,name):
        self.name=name
s1=stud("bunny")
print(s1.name,s1.car)
        
