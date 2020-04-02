from datetime import date


# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_fathers_age(name, father_age, father_person_age_diff):
        return Man(name, date.today().year - father_age + father_person_age_diff)

    @classmethod
    def from_birth_year(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


class Man(Person):
    sex = 'Male'


if __name__ == '__main__':
    man = Man.from_birth_year('John', 1985)
    print(isinstance(man, Man))

    man1 = Man.from_fathers_age('John', 1965, 20)
    print(isinstance(man1, Man))
