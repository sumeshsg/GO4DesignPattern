from ChainOfResponsibility.CoinHandlerBase import CoinHandlerBase


class TwentyCentHandler(CoinHandlerBase):
    def __init__(self):
        pass

    def handle_coin(self, coin):
        if coin.get_weight() == 20 and coin.get_diameter() == 20:
            print ("Captured 20 Cent")
        elif self._successor is not None:
            self._successor.handle_coin(coin)
