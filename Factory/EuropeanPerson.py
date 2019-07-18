from Person import Person

class EuropeanPerson(Person):

    def __init__(self):
        self.height = 1.80
        self.colorSkin = "white"

    def get_characteristics(self):
        return {"height": self.height, "colorSkin":self.colorSkin}
