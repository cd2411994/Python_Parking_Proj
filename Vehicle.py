class Vehicle:
    def __init__(self, regno, colour):
        self.colour = colour
        self.regno = regno


class Car(Vehicle):

    def __init__(self, regno, colour):
        Vehicle.__init__(self, regno, colour)

    def getType(self):
        return "Car"
