from GO4StructuralPatterns.DecoratorPattern.VehicleBase import VehicleBase


class Ferrari(VehicleBase):
    def get_make(self):
        return "Ferrari"

    def get_model(self):
        return "360"

    def get_hire_price(self):
        return 100

    def get_hire_lap(self):
        return 10
