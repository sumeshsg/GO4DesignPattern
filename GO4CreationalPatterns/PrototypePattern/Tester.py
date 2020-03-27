from PrototypePattern.Employee import Employee
import copy


class Tester(Employee):

    def clone(self):
        return copy.copy(self)
