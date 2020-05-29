from abc import abstractmethod


class CarFactory(object):
    @abstractmethod
    def create_car(model):
        pass

    @abstractmethod
    def deliver_car(model):
        pass
