# polymorphism with two different classes

class india():
    def capital(self):
        print("the delhi is the CAPITAL of india")
    def sports(self):
        print("hockey is the national game of india")
    def population(self):
        print("india is the 2nd population in the world")

class america():
    def capital(self):
        print("the Washington DC is the CAPITAL of USA")
    def sports(self):
        print("rucby is the national game of USA")
    def population(self):
        print("USA is the 3rd population in the world")

obj_ind = india()
obj_USA = america()

for country in (obj_ind, obj_USA):
    country.capital()
    country.sports()
    country.population()
