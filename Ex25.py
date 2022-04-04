#Slicing
#You can return a range of characters by uing slicing Syntax

b="Hello World"
#Slicing
#print(b[2:7])
#Slicing From Start
#print(b[:5])
#Slicing From End
#print(b[2:])
#print(b[-5:-2])
#Upper
#print(b.upper())
#Upper
#print(b.lower())
#b=" Hello World  "
#print(b)
#print(b.strip())# returns "Hello World"
#b="Hello World"
#print(b.replace("H","J"))
#b="Hello , World"
#print(b.split(","))
#a="Hello"
#b="World"
#c=a+" "+b
#print(c)
#age=36
#txt="My NAme is Amit, I am "+age
#print(txt)#  format error
#age=36
#txt="My NAme is Amit, I am {}"
#print(txt.format(age)) 
#Nultipal
qty=3
itemno=567
price=49.9566
#myorder="I Want {} prices of item {} for {} dollars "
#print(myorder.format(qty,itemno,price))
myorder="I Want to pay {2:.2f} dollars for {0} piceses of item {1}"
#print(myorder.format(price,qty,itemno))
price=49.55555
txt="the price {:.2f} rs"
#print(txt.format(price))
myorder="I Have a {carname},it is a {model}"
print(myorder.format(carname="Foard",model="Sport"))


