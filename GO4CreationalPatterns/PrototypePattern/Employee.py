from abc import abstractmethod


class Employee(object):
    def __init__(self, name, skill):
        self._name = name
        self._skill = skill

    @abstractmethod
    def clone(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_skill(self):
        return self._skill

    def set_skill(self, value):
        self._skill = value
