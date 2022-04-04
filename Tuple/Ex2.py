'''
thisTuple=("banana","apple","cherry","orange","kiwi","melon","mango")
y=list(thisTuple)




y[1]="axy"
thisTuple=tuple(y)
print(thisTuple)
'''
'''
thisTuple=("banana","apple","cherry","orange","kiwi","melon","mango")
y=list(thisTuple)
y.append("abc")
thisTuple=tuple(y)
print(thisTuple)
'''
thisTuple=("banana","apple","cherry","orange","kiwi","melon")
y=("mango",)
thisTuple += y
print(thisTuple)
