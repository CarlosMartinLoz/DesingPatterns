import copy
from BulbasaurFactory import BulbasaurFactory

if __name__ == '__main__':
    BulbasaurFactory.initialize()

    instance = BulbasaurFactory.getBulbaFuerte1()
    print(instance.getIVS())

    instance = BulbasaurFactory.getBulbaFuerte2()
    print(instance.getIVS())

    instance = BulbasaurFactory.getBulbaDevil1()
    print(instance.getIVS())

    instance = BulbasaurFactory.getBulbaDevil2()
    print(instance.getIVS())






