class Original(object):
    @staticmethod
    def test_original():
        return "Result From Original.test_original() function"


class MonkeyPatching(object):
    @staticmethod
    def test_monkey_patching():
        return "Result From MonkeyPatching.test_monkey_patching() function"


if __name__ == '__main__':
    original = Original()
    print(original.test_original())
    # Monkey patching
    original.test_original = MonkeyPatching.test_monkey_patching
    print(original.test_original())
