from GO4CreationalPatterns.SingletonPattern.Singleton import Singleton

if __name__ == '__main__':
    s = Singleton()
    print(s)

    s = Singleton.get_instance()
    print(s)

    s = Singleton.get_instance()
    print(s)
