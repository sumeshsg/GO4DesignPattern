from GO4CreationalPatterns.SingletonPattern.Singleton import SingleTon

if __name__ == '__main__':
    obj1 = SingleTon()
    obj2 = SingleTon()
    print(obj1)
    print(obj2)
    print(obj1.x == obj1.x)
