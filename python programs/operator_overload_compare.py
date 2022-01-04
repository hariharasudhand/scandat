# comparing

class student():

    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if (self.a > other.a ):
            return True
        else:
            return False

s1 = student(40)
s2 = student(30)

if s1 > s2 :
    print("it is good")
else:
    print("it is better")
