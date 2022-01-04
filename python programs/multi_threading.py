from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


s1 = hello()
s2 = hi()

s1.start()
sleep(0.2)
s2.start()

s1.join()
s2.join()

print("bye")