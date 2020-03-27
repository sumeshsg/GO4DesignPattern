class Coin:
    def __init__(self, weight, diameter):
        self._weight = weight
        self._diameter = diameter

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_diameter(self):
        return self._diameter

    def set_diameter(self, diameter):
        self._diameter = diameter
