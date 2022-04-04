thisDict={  "brand":"Ford",
    "electrical":False,    
    "Year":1964,
    "colors":("red","white","blue")
}
#x=thisDict["brand"]
#x=thisDict.get("Year")
#print(x)
'''
x=thisDict.keys()
print(x)
thisDict["model"]="Mustang"

print(x)
'''
'''
x=thisDict.values()
print(x)
'''
'''
x=thisDict.values()
print(x)
thisDict["year"]=2022
print(x)
'''
'''
x=thisDict.values()
print(x)
thisDict["model"]="Mustang"
print(x)
'''
'''
x=thisDict.items()# returns each item in a dictionary as tuple in a list

print(x)
'''
if "model" in thisDict:
    print(thisDict["brand"])
else :
    print("key is not avalable")

