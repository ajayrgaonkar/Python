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

#x=Student("Rakesh","Patil")
#x.printname()
#print(x.gradYear)
x=Student("Rakesh","Patil",2022)
x.printname()
print(x.gradYear)