#Camryn and Britney

class Person:
    def __init__(self, countryofOrigin, color):
        self.countryofOrigin = countryofOrigin
        self.color = color

    def __str__(self):
        return self.countryofOrigin + "(" + str(self.color) + ")"

p1 = Person("John", "pink" )

print(p1)
