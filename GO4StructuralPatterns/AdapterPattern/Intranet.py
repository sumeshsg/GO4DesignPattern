class Intranet(object):
    _phone_dictionary = None

    def __init__(self, phone_dictionary):
        self._phone_dictionary = phone_dictionary

    def get_employee(self):
        phone_dictionary = self._phone_dictionary.get_phone_list()
        for key, value in phone_dictionary.items():
            yield value
