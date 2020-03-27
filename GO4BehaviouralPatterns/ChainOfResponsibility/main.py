from ChainOfResponsibility.FiveCentHandler import FiveCentHandler
from ChainOfResponsibility.FiftyCentHandler import FiftyCentHandler
from ChainOfResponsibility.TenCentHandler import TenCentHandler
from ChainOfResponsibility.TwentyCentHandler import TwentyCentHandler
from ChainOfResponsibility.Coin import Coin

if __name__ == '__main__':
    h5 = FiveCentHandler()
    h10 = TenCentHandler()
    h20 = TwentyCentHandler()
    h50 = FiftyCentHandler()
    h5.set_successor(h10)
    h10.set_successor(h20)
    h20.set_successor(h50)

    coin_5 = Coin(5, 5)
    coin_10 = Coin(10, 10)
    coin_20 = Coin(20, 20)

    h5.handle_coin(coin_20)
