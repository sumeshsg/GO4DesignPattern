class SingleTon(object):
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(SingleTon, self).__new__(self)
            self.x = 10
        return self._instance
