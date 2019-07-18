from Person import Person

class AfricaPerson(Person):

    def __init__(self):
        self.height = 1.80
        self.colorSkin = "black"

    def get_characteristics(self):
        return {"height": self.height, "colorSkin":self.colorSkin}