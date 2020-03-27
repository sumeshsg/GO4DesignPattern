from abc import abstractmethod


class IntranetBase(object):
    @abstractmethod
    def get_phone_list(self):
        pass
