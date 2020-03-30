class Message(object):
    _message_sender = None
    _title = None
    _details = None
    _importance = None

    def __init__(self, title, details, importance):
        self._title = title
        self._details = details
        self._importance = importance

    def set_message_sender(self, value):
        self._message_sender = value

    def send(self):
        self._message_sender.send_message(self._title, self._details, self._importance)
