from GO4CreationalPatterns.AbstractFactory.audi_model.q_five import QFive
from GO4CreationalPatterns.AbstractFactory.audi_model.q_three import QThree
from GO4CreationalPatterns.AbstractFactory.car_factory import CarFactory


class AudiCarFactory(CarFactory):
    models = {"Q5": QFive,
              "Q3": QThree}

    model = None

    def __init__(self, model):
        self.model = model

    @staticmethod
    def create_car(model):
        return AudiCarFactory.models.get(model).create_car()

    @staticmethod
    def deliver_car(model):
        return AudiCarFactory.models.get(model).deliver_car()
