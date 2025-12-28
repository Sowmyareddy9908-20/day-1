# a function call itself 
#to print factorial using recurison
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

#for fibinocci series-sum of privious number : 0 1 1 2 3 5 8 13
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(7))

#power of 2 numbers
def pow(x,n):
    if n==1:
        return x
    else:
        return x*pow(x,n-1)
print(pow(3,3))