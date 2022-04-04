class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.gradYear=year
    def welcome(self):
        print("welcome",self.fname,self.lname," to the class of year ",self.gradYear)


x=Student("Rakesh","Patil",2022)
x.welcome()
x=Person("Rakesh","Patil")
x.printname()