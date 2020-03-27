class Person(object):
    name = None
    _mediator = None

    def __init__(self, mediator):
        self._mediator = mediator
