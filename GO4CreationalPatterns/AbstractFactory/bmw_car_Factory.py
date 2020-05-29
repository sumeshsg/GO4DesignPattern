from GO4CreationalPatterns.FactoryMethos.bmw_model.x_one import XOne
from GO4CreationalPatterns.FactoryMethos.bmw_model.x_three import XThree
from GO4CreationalPatterns.FactoryMethos.car_factory import CarFactory


class BmwCarFactory(CarFactory):
    models = {"X1": XOne,
              "X3": XThree}

    @staticmethod
    def create_car(model):
        return BmwCarFactory.models.get(model)
