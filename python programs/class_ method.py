# class method
class student():

    school = ' weeroda'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.school


cal1 = student(20, 30, 50)
cAL2 = student(0, 30, 80)

print(cAL2.calculate())

print(student.info())