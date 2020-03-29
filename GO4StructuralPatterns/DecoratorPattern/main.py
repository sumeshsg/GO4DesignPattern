from GO4StructuralPatterns.DecoratorPattern.Ferrari import Ferrari
from GO4StructuralPatterns.DecoratorPattern.SpecialOffer import SpecialOffer

if __name__ == '__main__':
    car = Ferrari()
    print(">>>>>>>>>>>>>>>> Normal Lap Details For Ferrari")
    print("Price For Laps:", car.get_hire_price(), "\nLaps:",
          car.get_hire_lap())
    offer = SpecialOffer(car)
    offer.set_discount_price(20)
    offer.set_extra_lap(2)
    print(">>>>>>>>>>>>>>>> Offer Lap Details For Ferrari")
    print("Price For Laps:", offer.get_hire_price(), "\nLaps:",
          offer.get_hire_lap())
