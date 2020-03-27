from ChainOfResponsibility.CoinHandlerBase import CoinHandlerBase


class FiftyCentHandler(CoinHandlerBase):
    def __init__(self):
        pass

    def handle_coin(self, coin):
        if coin.get_weight() == 50 and coin.get_diameter() == 50:
            print ("Captured 50 Cent")
        elif self._successor is not None:
            self._successor.handle_coin(coin)
