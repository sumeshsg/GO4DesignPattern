from GO4StructuralPatterns.DecoratorPattern.VehicleDecoratorBase import VehicleDecoratorBase


class SpecialOffer(VehicleDecoratorBase):
    _vehicle = None
    _discount_price = None
    _extra_lap = None

    def __init__(self, vehicle):
        self._vehicle = vehicle

    def set_discount_price(self, value):
        self._discount_price = value

    def set_extra_lap(self, value):
        self._extra_lap = value

    def get_hire_price(self):
        return self._vehicle.get_hire_price() - self._discount_price

    def get_hire_lap(self):
        return self._vehicle.get_hire_lap() + self._extra_lap
