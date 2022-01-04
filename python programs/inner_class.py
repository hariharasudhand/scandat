# inner class
class student():
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop():
        def __init__(self):
            self.company = "hp"
            self.process = "i3"
            self.ram = 8

        def show(self):
            print(self.company, self.process, self.ram)

s1 = student('harish', 28)

s1.show()



