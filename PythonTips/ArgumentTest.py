def test(*args, **kwargs):
    for argument in args:
        print(argument)
    for key, value in kwargs.items():
        print(key, ':', value)


test(1, 2, a=10, b=10)
