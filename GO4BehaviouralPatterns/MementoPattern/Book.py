class Book(object):
    _name = None
    _title = None
    _author = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_author(self, author):
        self._author = author

    def get_author(self):
        return self._author
