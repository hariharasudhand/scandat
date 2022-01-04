# inheritance class
class person():
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def print_function(self):
        print(self.first, self.last)

class student(person):
    def __init__(self, first_name, last_name):
        super().__init__( first_name, last_name)

x = student('harish', 'kumar')
x.print_function()