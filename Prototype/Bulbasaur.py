from Pokemon import Prototype
import copy

class BulbasaurFuerte(Prototype):

    def __init__(self, attack1,attack2,attack3,attack4):
        self.IVS = "450 IVS"
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
    def clone(self):
        return copy.copy(self)

class BulbasaurDevil(Prototype):

    def __init__(self, attack1,attack2,attack3,attack4):
        self.IVS = "360IVS"
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
    def clone(self):
        return copy.copy(self)