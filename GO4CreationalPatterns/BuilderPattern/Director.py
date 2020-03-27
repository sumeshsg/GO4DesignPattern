from BuilderPattern.Car import Car


class Director(object):
    _builder = None

    def set_builder(self, value):
        self._builder = value

    def get_car(self):
        car = Car()
        car._wheels
        engine = self._builder.get_engine()
        car.set_engine(engine)
        body = self._builder.get_body()
        car.set_body(body)
        for i in range(4):
            wheel = self._builder.get_wheel()
            car.attach_wheel(wheel)
        print(">>>>>>>>> Body:", self._builder.shape)
        print(">>>>>>>>> Engine:", self._builder.horsepower)
        print(">>>>>>>>> Wheel Size:", self._builder.size)
