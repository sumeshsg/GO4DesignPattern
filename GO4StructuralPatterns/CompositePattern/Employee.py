class Employee(object):
    _name = None

    def __init__(self, name):
        self._name = name
        self._subordinates = []

    def get_name(self):
        return self._name

    def add_subordinate(self, subordinate):
        self._subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        self._subordinates.remove(subordinate)

    def get_subordinates(self):
        return self._subordinates
