class function():
    def add(self, a, b):
        print(float(a + b))

    def sub(self, a, b):
        print(float(a - b))

    def mul(self, a, b):
        print(float(a * b))

    def div(self, a, b):
        print(float(a / b))


fun = function()

fun.add(20.8, 20.6)
fun.sub(30.2, 20.8)
fun.mul(25.3, 6)
fun.div(20.9, 2)