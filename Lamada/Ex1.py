#A lamada function is small anonymous function


#A lamda fruntion can take any number of arguments, but can have only one expression
#Syntax: lambda arguments : expression

'''
a=5
x=a+10

print(x)
'''
'''
def my_function(a):
    x=a+10
    return x

print(my_function(100))
'''
#x=lambda a : a+10
#print(x(10))
#x=lambda b: b*b
#print(x(10))
#x=lambda a,b : a+b
#print(x(10,20))
'''
z=lambda x,y,z :  x+y+z
m=z(10,20,30)
print(m)
'''
'''
def myFunc(n):
    return lambda a:a*a

myFunction=myFunc(10)
print(myFunction(10))

'''
#x=lambda a,b : a+b
'''
def myFunc(n):
    return lambda a:a*n

myFunction=myFunc(2)
print(myFunction(12))
'''
def myFunc(n):
    return lambda a:a*n

myDouble=myFunc(2)
mytriper=myFunc(3)
print(myDouble(11))
print(mytriper(11))
