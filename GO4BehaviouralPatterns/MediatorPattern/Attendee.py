from MediatorPattern.Person import Person


class Attendee(Person):
    def __init__(self, mediator):
        super().__init__(mediator)

    def ask_question(self, question):
        print("{0} asked by {1}".format(question, self.name))

    def receive_slide(self, url):
        print("{0} received by {1}".format(self.name, url))

    def receive_answer(self, answer, attendee):
        print("{0} received by {1}".format(answer, self.name))
