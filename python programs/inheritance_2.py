#inhweitance of next level

class person():
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def print_fun(self):
        print(self.first, self.last)

class student(person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.year = graduation_year
    def call_by(self):
        print(self.first , self.last , " was finish his graduation on  " , self.year)

x = student("harish", "kumar", 2019)

x.call_by()