class base(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class child(base):

    def __init__(self, name, age):
        base.__init__(self,name)
        self.age = age

    def get_age(self):
        return self.age

class grandchild(child):

    def __init__(self, name, age, place):
        child.__init__(self,name, age)
        self.place = place

    def get_place(self):
        return self.place

result = grandchild("harish", 23, "salem")

print(result.get_name(), result.get_age(), result.get_place())

