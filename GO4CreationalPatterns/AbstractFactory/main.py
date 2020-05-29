from GO4CreationalPatterns.AbstractFactory.audi_car_factory import AudiCarFactory
from GO4CreationalPatterns.AbstractFactory.bmw_car_Factory import BmwCarFactory
from GO4CreationalPatterns.AbstractFactory.client import Client

if __name__ == '__main__':
    audi_car_factory = AudiCarFactory(model="Q5")
    bmw_car_factory = BmwCarFactory(model="X1")
    print (">>>>>>>>>>>>>>>>>>>>>AUDI")
    client = Client(audi_car_factory)
    print(client.create_car())
    print(client.deliver_car())
    print(">>>>>>>>>>>>>>>>>>>>>BMW")
    bmw_car_factory = BmwCarFactory(model="X3")
    client = Client(bmw_car_factory)
    print(client.create_car())
    print(client.deliver_car())
