'''
def my_functon(*kids):
    print(kids)
my_functon("Amit","Rudra","Ridesh")
'''
'''
def my_functon(*kids):
    print("The youngest child is "+kids[2])



my_functon("Amit","Rudra","Ridesh")
''' 
#**keyworldArgument(For dictionary of argument)
from fnmatch import fnmatch


def my_function(**kid):
    print("His last name is "+kid["lname"])

my_function(fname="Rura",lname="Patil")