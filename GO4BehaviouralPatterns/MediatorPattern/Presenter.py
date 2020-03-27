from MediatorPattern.Person import Person


class Presenter(Person):
    def __init__(self, mediator):
        super().__init__(mediator)

    def send_new_slide(self, url):
        print("Presenter change slide: {0}".format(url))
        self._mediator.send_slide(url)

    @staticmethod
    def receive_question(question, attendee):
        print('Presenter receive question from {0} from {1}'.format(attendee.name, question))
        pass

    def answer_question(self, answer, attendee):
        print("Presenter answered the question for {0}: {1}".format(attendee.name, answer))
        self._mediator.send_answer(answer, attendee)
