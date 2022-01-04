#duck type in polymorphism

class pycharm():

    def execute(self):
        print("compiling")
        print("running")
class myeditor():

    def execute(self):
        print("spelling")
        print("correcting")
        print("compiling")
        print("running")

class code():

    def coding(self, ide):
        ide.execute()

ide = pycharm()

x = code()
x.coding(ide)