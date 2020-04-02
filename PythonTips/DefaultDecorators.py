# A class method is a method that is bound to a class rather than its object.
# It doesn't require creation of a class instance, much like staticmethod
# Static method knows nothing about the class and just deals with the parameters
# Class method works with the class since its parameter is always the class itself.

class DefaultDecorators(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"

    def normal_method(*args, **kwargs):
        print("calling normal_method({0},{1})".format(args, kwargs))

    @classmethod
    def class_method(*args, **kwargs):
        print("calling class_method({0},{1})".format(args, kwargs))

    @staticmethod
    def static_method(*args, **kwargs):
        print("calling static_method({0},{1})".format(args, kwargs))

    @property
    def some_property(self, *args, **kwargs):
        print("calling some_property getter({0},{1},{2})".format(self, args, kwargs))
        return self._some_property

    @some_property.setter
    def some_property(self, *args, **kwargs):
        print("calling some_property setter({0},{1},{2})".format(self, args, kwargs))
        self._some_property = args[0]

    @property
    def some_other_property(self, *args, **kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self, args, kwargs))
        return self._some_other_property


if __name__ == '__main__':
    o = DefaultDecorators()
    # o.normal_method
    # o.normal_method()
    # o.normal_method(1, 2, x=3, y=4)

    # o.class_method
    # o.class_method()
    # o.class_method(1, 2, x=3, y=4)
    #
    # o.static_method
    # o.static_method()
    # o.static_method(1, 2, x=3, y=4)

    # o.some_property
    # o.some_other_property
    #
    # o.some_other_property()
    # o.some_property = "groovy"
    # o.some_property

    # o.some_other_property = "very groovy"

    DefaultDecorators.normal_method(1, 2, x=3, y=4)
    o.normal_method(1, 2, x=3, y=4)
    DefaultDecorators.static_method(1, 2, x=3, y=4)
    DefaultDecorators.class_method(1, 2, x=3, y=4)
