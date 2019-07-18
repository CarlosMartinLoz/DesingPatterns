from Builder import JeepBuilder
from driver import Director

def main():
    jeepBuilder = JeepBuilder()
    director = Director()
    director.setBuilder(jeepBuilder)
    car = director.getCart()
    print(car.toString())


if __name__=="__main__":

    main()