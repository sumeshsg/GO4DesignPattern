import uuid


class Target(object):
    def __init__(self):
        self.id = uuid.uuid1()
        self.unit = None
