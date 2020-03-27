from GO4StructuralPatterns.AdapterPattern.IntranetBase import IntranetBase


class PhoneListAdapter(IntranetBase):
    _personnel = None

    def __init__(self, personnel):
        self._personnel = personnel

    def get_phone_list(self):
        phone_dictionary = {}
        key = 1
        for item in self._personnel.get_employee():
            phone_dictionary[key] = item
            key += 1
        return phone_dictionary
