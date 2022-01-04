global str
from time import  sleep
try:
 lift_rules = int(input("Enter the number (1 or 2)"))

 class lift_operator():

    def __init__(self,capacity, current_pos, targetpos, status):
        self.cap = capacity
        self.current = current_pos
        self.target = targetpos
        self.status = status

    def print_fun(self):
        print(self.cap, self.current, self.target, self.status)


 class service_lift(lift_operator):

    def __init__(self, capacity, current_pos, targetpos, status):
        super().__init__(capacity, current_pos, targetpos, status)

    def call_by(self):
        print(self.cap, "person is the capactiy of service_lift ", self.current, "is the current and target capacity will be  ", self.target)

    def stat(self):
        if self.current == True:
             print(str(self.status))
        else:
            print("the lift was not moving")

    def calculate(self):
        if self.current <= 1000:
            print("your current capacity is ", self.current,"you got to go")
            sleep(1)
            print("have a safe journey")
        else:
            print("the weight was over load")
            sleep(1)
            print("the lift was not moving")


 class passenger_lift(lift_operator):

    def __init__(self, capacity, current_pos, targetpos, status):
        super().__init__(capacity, current_pos, targetpos, status)

    def call_by(self):
        print(self.cap, "person is the capactiy of passenger_lift", self.current, "is the current capacity and target capacity will be ", self.target)

    def stat(self):
        if self.stat == self.current:
             print(str(self.status))
        else:
            print("the lift is not moving")

    def calculate(self):
        if self.current <= 400:
            print("your current capacity is ", self.current, "you got to go")
            sleep(1)
            print("have a safe journey")
        else:
            print("the weight was over load")
            sleep(1)
            print("the lift was not moving")


 r1 = service_lift(4, 1010, 1000, "max allowed capacity is 1000 and it is ready to move")

 r2 = passenger_lift(8, 399, 400, "max allowed capacity is 400 and it is ready to move")

 if lift_rules == 1:
    r1.calculate()
    sleep(1)
    #r1.stat()
    #sleep(1)
    r1.call_by()

 elif lift_rules == 2:
    r2.calculate()
    sleep(1)
    #r2.stat()
    #sleep(1)
    r2.call_by()

 else:
    print("you enter the wrong number")
except ValueError as e :
    print("the value error is have", e)
except Exception as E :
    print("the Exception error is have", E)
