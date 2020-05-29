from GO4CreationalPatterns.FactoryMethos.audi_car_factory import AudiCarFactory
from GO4CreationalPatterns.FactoryMethos.bmw_car_Factory import BmwCarFactory

if __name__ == '__main__':
    audi_car_factory = AudiCarFactory()
    car = audi_car_factory.create_car('Q5')
    print(car.get_car())
    bmw_car_factory = BmwCarFactory()
    car = bmw_car_factory.create_car('X1')
    print(car.get_car())
