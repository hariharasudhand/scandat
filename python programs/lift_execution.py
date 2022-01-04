from Service_lift import service_lift
from Passenger_lift import passenger_lift
from time import sleep

try:
    lift_rules = int(input("Enter the lift (1 - service or 2- passenger )"))

    if lift_rules == 1:
        r1 = service_lift(int(input("how many passenger are in lift")), 10, 1000,
                          "max allowed capacity is 1000 and it is ready to move")
        r1.calculate()
        sleep(1)
        # r1.stat()
        # sleep(1)
        r1.call_by()

    elif lift_rules == 2:
        r2 = passenger_lift(int(input("how many passenger are in lift")), 10, 400,
                            "max allowed capacity is 400 and it is ready to move")
        r2.calculate()
        sleep(1)
        # r2.stat()
        # sleep(1)
        r2.call_by()
    else:
        print("you enter the wrong number")

except Exception as e:
    print("The exception error", e)