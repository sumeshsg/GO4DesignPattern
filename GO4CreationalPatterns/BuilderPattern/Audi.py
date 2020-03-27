from BuilderPattern.BulderBase import BuilderBase
from BuilderPattern.Wheel import Wheel
from BuilderPattern.Engine import Engine
from BuilderPattern.Body import Body


class Audi(BuilderBase):
    def __init__(self, size, horsepower, shape):
        self.size = size
        self.horsepower = horsepower
        self.shape = shape

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = self.size
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = self.horsepower
        return engine

    def get_body(self):
        body = Body()
        body.shape = self.shape
        return body
