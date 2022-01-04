from lift import lift_operator
from time import sleep
try:
    class passenger_lift(lift_operator):

        def __init__(self, capacity, current_pos, targetpos, status):
            super().__init__(capacity, current_pos, targetpos, status)

        def call_by(self):
            print(self.cap, "person is the capactiy of passenger_lift", self.current,
                  "is the minimum capacity and maxminum capacity will be ", self.target)

        def stat(self):
            if self.stat == self.current:
                print(str(self.status))
            else:
                print("the lift is not moving")

        def calculate(self):
            self.weigh = 90 * self.cap
            if self.weigh <= 500:
                print("your current capacity is ", self.weigh, "you got to go")
                sleep(1)
                print("have a safe journey")
            else:
                print("the capacity was", self.weigh, " so the weight was over load")
                sleep(1)
                print("the lift was not moving")

except Exception as e:
    print("The exception error", e)