try:
    class lift_operator():

        def __init__(self, capacity, current_pos, targetpos, status):
            self.cap = capacity
            self.current = current_pos
            self.target = targetpos
            self.status = status

        def print_fun(self):
            print(self.cap, self.current, self.target, self.status)

except Exception as e:
    print("The exception error", e)