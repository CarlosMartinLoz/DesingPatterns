class Driver:
    builder = None

    def setBuilder(self,builder):
        self.builder=builder

    def getCart(self):
        car= Car()
        body = self.builder.getBody()
        car.setBody(body)
        engine = self.builder.getEngine()
        car.setEngine(engine)

        i=0
        while i<4:
            wheel = self.builder.getWheel()
            car.attachWheel(wheel)
            i+=1
        return car

class Builder:
    def getWheel(self):
        pass
    def getEngine(self):
        pass
    def getBody(self):
        pass

class JeepBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.setSize(112)
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.setSize(50)
        return engine

    def getBody(self):
        body = Body()
        body.setWight(100)
        return body


class Car:
    def __init__(self):
        self.wheels = list()
        self.engine = None
        self.body = None

    def setBody(self,body):
        self.body=body

    def attachWheel(self,wheel):
        self.wheels.append(wheel)

    def setEngine(self,engine):
        self.engine=engine

    def toString(self):

        return len(self.wheels)




class Body:
    weight=None

    def setWight(self,weight):
        self.weight=weight


class Engine:
    cv = None

    def setSize(self, cv):
        self.cv = cv


class Wheel:
    size=None

    def setSize(self,size):
        self.size=size







