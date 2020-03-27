from GO4BehaviouralPatterns.MementoPattern.Book import Book
from GO4BehaviouralPatterns.MementoPattern.Action import Action

if __name__ == '__main__':
    book1 = Book()
    book1.set_name('Name 1')
    book1.set_author('Author 1')
    book1.set_title('Title 1')

    book2 = Book()
    book2.set_name('Name 2')
    book2.set_author('Author 2')
    book2.set_title('Title 2')

    print('>>>>>>>>>Add book')
    action = Action()
    action.add(book1)
    action.add(book2)
    print('>>>>>>>>>Show book')
    action.show_book()


    print('>>>>>>>>>Undo')
    action.undo()
    print('>>>>>>>>>Show book')
    action.show_book()

    print('>>>>>>>>>Redo')
    action.redo()
    print('>>>>>>>>>Show book')
    action.show_book()
    print('>>>>>>>>>Undo 2 time')
    action.undo()
    action.undo()
    print('>>>>>>>>>Show book')
    action.show_book()
    print('>>>>>>>>>Redo 2 time')
    action.redo()
    action.redo()
    print('>>>>>>>>>Show book')
    action.show_book()
