


'''
class Myclass:
    x=5

#print(Myclass)
#Create object of calss
p1=Myclass()
print(p1.x)
'''

#_init_()
'''
class Myclass:
    def __init__():
        print("Hello MyClass from")

p1=Myclass()
'''
'''
class Person:
    def __init__(self):
        print("Hello MyClass INIT()")
p1=Person()
'''
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("Rudra",15)

print(p1.name)
print(p1.age)
'''
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfuc(self):
        print("Hello my name is "+self.name)


p1=Person("Rudra",11)
p1.myfuc()
'''
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfuc(self):
        print("Hello my name is "+self.name)


p1=Person("Rudra",11)
p1.myfuc()
p1.age=12
print(p1.age)
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfuc(self):
        print("Hello my name is "+self.name)

p1=Person("Rudra",11)
p1.myfuc()
p1.age=12
print(p1.age)

#del p1.age
#print(p1.age)
del p1
print(p1)
