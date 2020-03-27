import copy

from PrototypePattern.Employee import Employee


class Developer(Employee):
    def clone(self):
        return copy.copy(self)
