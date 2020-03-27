class Car(object):
    def __init__(self):
        self._wheels = []
        self._engine = None
        self._body = None

    def set_body(self, value):
        self._body = value

    def set_engine(self, value):
        self._engine = value

    def attach_wheel(self, value):
        self._wheels.append(value)
