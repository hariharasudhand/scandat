#polymorphism inheritance 
class bird():
    def intro(self):
        print("some birds can fly and some cant fly")
    def fly(self):
        print("ostrich can fly")

class eagle(bird):
    def fly(self):
        print("eagle can fly")

class pegion(bird):
    def fly(self):
        print("pegion can fly")

obj_bird = bird()
obj_eagle = eagle()
obj_pegion = pegion()

obj_bird.intro()
obj_bird.fly()

obj_eagle.intro()
obj_eagle.fly()

obj_pegion.intro()
obj_pegion.fly()