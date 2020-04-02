# Python decorators add functionality to functions and methods at definition time.
# The decorator pattern is an object orientated design pattern that allows behaviour to be added to an existing object dynamically.

def smart_divide(param):
    def decorator(func):
        def decorated(a, b):
            print(param)
            print("I am going to divide", a, "and", b)
            if b == 0:
                print("Whoops! cannot divide")
                return
            return func(a, b)
        return decorated
    return decorator


class DecoratorTest(object):
    @staticmethod
    @smart_divide(param="Test Parameter From Decorator")
    def divide(a, b):
        return a / b


if __name__ == '__main__':
    obj = DecoratorTest()
    obj.divide(1, 0)
