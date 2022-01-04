class addition():
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def adding(self):
        self.answer = self.first + self.second

    def print(self):
        print("the value of first num = " + str(self.first))
        print("the value of second num = " + str(self.second))
        print("the addition of two number is = " + str(self.answer))



cal1 = addition(2500, 2000)

cal1.adding()

cal1.print()