class computer():
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("the confige is ", self.cpu, self.ram)

com1 = computer("i3", 8)
com1.config()
