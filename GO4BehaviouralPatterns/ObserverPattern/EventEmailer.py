from GO4BehaviouralPatterns.ObserverPattern.EventMonitor import EventMonitor


class EventEmailer(EventMonitor):
    _receiver = None

    def __init__(self, receiver):
        self._receiver = receiver

    def update(self):
        message = self._receiver.last_message
        print("Emailing: {0}".format(message))
