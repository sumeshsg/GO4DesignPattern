from abc import abstractmethod


class VehicleBase(object):
    @abstractmethod
    def get_make(self):
        pass

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_hire_price(self):
        pass

    @abstractmethod
    def get_hire_lap(self):
        pass
