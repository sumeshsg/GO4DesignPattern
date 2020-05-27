class SingleTon(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingleTon, cls).__new__(cls)
            cls.x = 10
        return cls._instance
