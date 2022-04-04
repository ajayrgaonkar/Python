#Note: Both union() and update() will exclude any duplicate items'''
'''
mySet={"apple","banana","cherry"}
mySet2={1,2,3}
set3=mySet.union(mySet2)
print(set3)
'''
'''
mySet={"apple","banana","cherry"}
mySet2={1,2,3}
mySet.update(mySet2)
print(mySet)
'''

mySet={"apple","banana","cherry"}
mySet2={1,2,3,"banana"}
#mySet.intersection_update(mySet2)#Keep ONLY the Duplicate
#mySet.intersection(mySet2)
#mySet.symmetric_difference_update(mySet2)# Keep All,But NOT the Dupicates
#print(mySet)
z=mySet.symmetric_difference(mySet2)
print(z)
