from Bulbasaur import BulbasaurFuerte
from Bulbasaur import BulbasaurDevil

class BulbasaurFactory:

    bulbasaurFuerte1 = None
    bulbasaurFuerte2 = None
    bulbasaurDevil1 = None
    bulbasaurDevil2 = None

    @staticmethod
    def initialize():
        BulbasaurFactory.bulbasaurFuerte1 = BulbasaurFuerte("Latigo cepa","Placaje","Rayo Solar","Rayo Solar")
        BulbasaurFactory.bulbasaurFuerte2 = BulbasaurFuerte("Somnifero","Placaje","Rayo Solar","Drenadoras")
        BulbasaurFactory.bulbasaurDevil1 = BulbasaurDevil("Latigo cepa","Estallido","Rayo Solar","Rayo Solar")
        BulbasaurFactory.bulbasaurDevil2 = BulbasaurDevil("cortacesped","Placaje","Rayo Solar","Rayo Solar")

    @staticmethod
    def getBulbaFuerte1():
        return BulbasaurFactory.bulbasaurFuerte1.clone()

    @staticmethod
    def getBulbaFuerte2():
        return BulbasaurFactory.bulbasaurFuerte2.clone()

    @staticmethod
    def getBulbaDevil1():
        return BulbasaurFactory.bulbasaurDevil1.clone()

    @staticmethod
    def getBulbaDevil2():
        return BulbasaurFactory.bulbasaurDevil2.clone()