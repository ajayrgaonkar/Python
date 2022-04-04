'''
thisList=["orange","mango","kiwi","apple","banana","cherry"]
thisList.sort()
#print(thisList)


thisList=[100,50,65,85,23]
thisList.sort()
print(thisList)
'''
'''
#Sort Descnding
thisList=["orange","mango","kiwi","apple","banana","cherry"]
thisList.sort(reverse = True)
print(thisList)
'''
'''
def myFunc(n):
    return abs(n-50) #50,0,15,35,25 sorting[50,65,23,82,100]

thisList=[100,50,65,85,23]
thisList.sort(key=myFunc)
print(thisList)
#thisList	100	50	65	85	23
#MyFunc	50	0	15	35	27
#sort	50	65	23	85	100
#	0	15	27	35	50
'''

#thisList=["Orange","mango","kiwi","apple","Apple","banana","cherry"]
#thisList.sort()
#print(thisList)
thisList=["Orange","mango","kiwi","apple","banana","cherry"]
thisList.reverse()
print(thisList)
