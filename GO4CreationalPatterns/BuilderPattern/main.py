from GO4CreationalPatterns.BuilderPattern.Audi import Audi
from GO4CreationalPatterns.BuilderPattern.Director import Director

if __name__ == '__main__':
    director = Director()
    car_builder = Audi(size=25, horsepower=1000, shape="SUV")
    director.set_builder(car_builder)
    director.get_car()
