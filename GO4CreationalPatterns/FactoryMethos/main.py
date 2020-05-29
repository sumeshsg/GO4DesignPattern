from GO4CreationalPatterns.FactoryMethos.audi_car_factory import AudiCarFactory
from GO4CreationalPatterns.FactoryMethos.bmw_car_Factory import BmwCarFactory

if __name__ == '__main__':
    audi_car_factory = AudiCarFactory()
    print(audi_car_factory.create_car('Q5').get_car())
    print(audi_car_factory.create_car('Q3').get_car())
    bmw_car_factory=BmwCarFactory()
    print(bmw_car_factory.create_car('X1').get_car())
    print(bmw_car_factory.create_car('X3').get_car())
