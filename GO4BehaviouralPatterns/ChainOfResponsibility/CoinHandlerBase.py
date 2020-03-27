from abc import abstractmethod


class CoinHandlerBase:
    def __init__(self):
        _successor = CoinHandlerBase()
        self._successor = _successor

    @abstractmethod
    def handle_coin(self, coin):
        pass

    def set_successor(self, successor):
        self._successor = successor
