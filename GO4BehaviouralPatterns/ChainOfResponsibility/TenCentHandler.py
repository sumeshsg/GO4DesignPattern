from GO4BehaviouralPatterns.ChainOfResponsibility.CoinHandlerBase import CoinHandlerBase


class TenCentHandler(CoinHandlerBase):
    def __init__(self):
        pass

    def handle_coin(self, coin):
        if coin.get_weight() == 10 and coin.get_diameter() == 10:
            print ("Captured 10 Cent")
        elif self._successor is not None:
            self._successor.handle_coin(coin)
