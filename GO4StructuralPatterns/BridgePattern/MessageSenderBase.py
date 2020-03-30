from abc import abstractmethod


class MessageSenderBase(object):
    @abstractmethod
    def send_message(self, title, details, importance):
        pass
