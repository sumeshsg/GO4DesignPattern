from GO4StructuralPatterns.DecoratorPattern.VehicleBase import VehicleBase


class VehicleDecoratorBase(VehicleBase):
    _vehicle = None

    def __init__(self, vehicle):
        self._vehicle = vehicle

    def get_make(self):
        return self._vehicle.get_make()

    def get_model(self):
        return self._vehicle.get_model()

    def get_hire_price(self):
        return self._vehicle.get_hire_price()

    def get_hire_lap(self):
        return self._vehicle.get_hire_lap()
