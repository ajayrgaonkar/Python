 #Looping using List  Comprehension
 #it is shortest syntax for looping


'''
thisList=["apple","banana","cherry","kiwi","mango"]
newList=[]
#[print(x) for x in thisList ]
for x in thisList:
    if "a" in x:
        newList.append(x)

print(newList)
'''
'''
# Syntax
newList=[expression for item in iterabl if condition==True]
'''
thisList=["apple","banana","cherry","kiwi","mango"]
#newList=
#[print(x) for x in thisList]
#newList=[x for x in thisList if "a" in x]
#print(newList)
#newList=[x for x in range(10)]
#print(newList)
#newList=[x for x in range(10) if x < 5]
#print(newList)
#newList=[x.upper() for x in thisList]
#newList=["hello" for x in thisList]
newList=[x if x!="banana" 
else "orange" for x in thisList]
print(newList)




 
