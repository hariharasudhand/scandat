#Arbitrary Keyword Arguments, *kwargs
def myfunction(**kids):
    print("the youngest child is "+ kids["fname"])

myfunction(fname = "harish", sname = "karthi")



#Arbitrary Keyword Arguments, **kwargs
def function(*kid):
    print("the young child is ", kid[1])

function("harish", "karthi","naveen")