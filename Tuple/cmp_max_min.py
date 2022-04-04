from filecmp import cmp


tuple1=('python','java')
tuple2=('coder',1)
if(cmp(tuple1,tuple2)!=0):
    print("No the same")
else: 
    print("same")
