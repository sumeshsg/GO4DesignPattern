class Action(object):
    _book_queue = []
    _current_book = None
    _book_stack = []

    def add(self, book):
        self._book_queue.append(book)
        self._current_book = book

    def undo(self):
        if self._book_queue and len(self._book_queue) >= 1:
            self._current_book = self._book_queue[len(self._book_queue) - 1]
            self._book_queue.remove(self._current_book)
            self._book_stack.append(self._current_book)
        else:
            self._book_queue = None

    def redo(self, redo_cnt=0):
        if self._book_stack and len(self._book_stack) >= 1:
            if self._book_stack[redo_cnt] in self._book_queue:
                redo_cnt += 1
                self.redo(redo_cnt)
            else:
                self._book_queue.append(self._book_stack[redo_cnt])


        else:
            self._book_stack = None

    def show_book(self):
        if self._book_queue:
            for book in self._book_queue:
                if book:
                    print(book.get_name(), ':', book.get_author(), ':',
                          book.get_title())
        else:
            print('No Book Present')
