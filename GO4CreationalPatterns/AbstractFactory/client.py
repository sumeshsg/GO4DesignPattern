class Client(object):
    factory = None
    model = None

    def __init__(self, factory):
        self.factory = factory
        self.model = factory.model

    def create_car(self):
        return self.factory.create_car(self.model)

    def deliver_car(self):
        return self.factory.deliver_car(self.model)
