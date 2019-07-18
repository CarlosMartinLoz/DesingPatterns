from Builder import Car


class Director:
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