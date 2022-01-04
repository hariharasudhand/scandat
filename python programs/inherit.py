class person():

    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name

    def is_employee(self):
        return False

class employee(person):

    def is_employee(self):
        return True

x = employee()



