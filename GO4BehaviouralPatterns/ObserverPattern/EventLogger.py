from ObserverPattern.EventMonitor import EventMonitor


class EventLogger(EventMonitor):
    _receiver = None

    def __init__(self, receiver):
        self._receiver = receiver

    def update(self):
        message = self._receiver.last_message
        print("Logging: {0}".format(message))
