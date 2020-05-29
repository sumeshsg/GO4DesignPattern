from GO4CreationalPatterns.AbstractFactory.bmw_model.x_one import XOne
from GO4CreationalPatterns.AbstractFactory.bmw_model.x_three import XThree
from GO4CreationalPatterns.AbstractFactory.car_factory import CarFactory


class BmwCarFactory(CarFactory):
    models = {"X1": XOne,
              "X3": XThree}
    model = None

    def __init__(self, model):
        self.model = model

    @staticmethod
    def create_car(model):
        return BmwCarFactory.models.get(model).create_car()

    @staticmethod
    def deliver_car(model):
        return BmwCarFactory.models.get(model).deliver_car()
