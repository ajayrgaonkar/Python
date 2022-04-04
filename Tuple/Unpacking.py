'''
frutes=("apple","banana","cherry" )# Packing
print(frutes)
(green,yellow,red)=frutes
print(green)
print(yellow)
print(red)
'''
'''
frutes=("apple","banana","cherry","strawerry","raspberry" )# Packing
(green,yellow,*red)=frutes
print(green)
print(yellow)
print(red)
'''
frutes=("apple","mmango","papaya","pineapple","cherry" )# Packing
(green,*tropical,red)=frutes
print(green)
print(tropical)
print(red)

