from ChainOfResponsibility.CoinHandlerBase import CoinHandlerBase


class FiveCentHandler(CoinHandlerBase):
    def __init__(self):
        pass

    def handle_coin(self, coin):
        if coin.get_weight() == 5 and coin.get_diameter() == 5:
            print ("Captured 5 Cent")
        elif self._successor is not None:
            self._successor.handle_coin(coin)
