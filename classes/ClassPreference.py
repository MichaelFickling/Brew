class Preferences:
    def __init__(self, name, temperature, colour, alcohol, carbonated, flavours):
        self.name = name #personname?
        self.temperature = temperature
        self.colour = colour
        self.alcohol = alcohol
        self.carbonated = carbonated
        self.flavours = flavours #list? OR
        # be able to take any number of attributes?


    def __repr__(self):
        return self.name