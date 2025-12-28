'''fun is a block of code
use for reuability 
'''
#simple fun prog
def greet(a,b): #here a,b are parameters
    print(a+b)
greet(2,3) #2,3 r arguments

#using return keyword
def add(a,b):
    return a+b
x=5+3
print(x) #or
print(add(5,6))

#even or odd
def cal(i):
    if i%2==0:
        return "even"
    else:
        return "odd"
x=5
print(cal(x))

#nested function => fun within the fun
def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()