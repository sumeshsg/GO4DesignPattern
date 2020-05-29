from GO4CreationalPatterns.FactoryMethos.audi_model.q_five import QFive
from GO4CreationalPatterns.FactoryMethos.audi_model.q_three import QThree
from GO4CreationalPatterns.FactoryMethos.car_factory import CarFactory


class AudiCarFactory(CarFactory):
    models = {"Q5": QFive,
              "Q3": QThree}

    @staticmethod
    def create_car(model):
        return AudiCarFactory.models.get(model)
