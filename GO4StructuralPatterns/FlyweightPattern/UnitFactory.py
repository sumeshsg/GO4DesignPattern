from FlyweightPattern.Tank import Tank
from FlyweightPattern.Soldier import Soldier


class UnitFactory(object):
    unit_dictionary = {}

    def get_unit(self, unit_type):
        if unit_type in self.unit_dictionary:
            return self.unit_dictionary.get(unit_type)
        else:
            unit_object = globals()[unit_type.capitalize()]()
            self.unit_dictionary[unit_type] = unit_object
            return unit_object
