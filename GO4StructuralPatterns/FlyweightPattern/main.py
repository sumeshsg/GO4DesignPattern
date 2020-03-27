from GO4StructuralPatterns.FlyweightPattern.UnitFactory import UnitFactory
from GO4StructuralPatterns.FlyweightPattern.Target import Target

if __name__ == '__main__':
    unit_factory = UnitFactory()

    unit_tank_1 = Target()
    unit_tank_1.unit = unit_factory.get_unit('tank')

    unit_tank_2 = Target()
    unit_tank_2.unit = unit_factory.get_unit('tank')

    print(">>>>>>>>>>>> ID of Tanks")
    print(unit_tank_1.id)
    print(unit_tank_2.id)

    print(">>>>>>>>>>>> Unit Details Of Tank")
    print(unit_tank_1.unit)
    print(unit_tank_2.unit)
