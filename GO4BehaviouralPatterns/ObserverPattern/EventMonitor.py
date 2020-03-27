from abc import abstractmethod


class EventMonitor(object):

    @abstractmethod
    def update(self):
        raise NotImplementedError
