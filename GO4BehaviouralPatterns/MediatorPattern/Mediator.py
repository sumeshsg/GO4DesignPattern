class Mediator:
    attendees = []
    presenter = None

    def __init__(self):
        pass

    def send_slide(self, url):
        for attendee in self.attendees:
            attendee.receive_slide(url)

    @staticmethod
    def send_answer(answer, attendee):
        attendee.receive_answer(answer, attendee)

    def send_question(self, question, attendee):
        self.presenter.receive_question(question, attendee)
