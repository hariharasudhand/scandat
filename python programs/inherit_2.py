class base1():

    def __init__(self):
        self.name1 = "harish"
        print(self.name1)

class base2():

    def __init__(self):
        self.name2 = "karthi"
        print(self.name2)

class derived(base1, base2):

    def __init__(self):

        base1.__init__(self)
        base2.__init__(self)
        print("derived")

    def printstrs(self):
        print(self.name1, self.name2)

x = derived()

x.printstrs()

