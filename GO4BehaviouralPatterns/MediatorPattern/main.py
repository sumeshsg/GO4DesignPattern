from MediatorPattern.Mediator import Mediator
from MediatorPattern.Attendee import Attendee
from MediatorPattern.Presenter import Presenter

if __name__ == '__main__':
    mediator = Mediator()

    presenter = Presenter(mediator)
    presenter.name = "SG"

    attendee1 = Attendee(mediator)
    attendee1.name = "June"

    attendee2 = Attendee(mediator)
    attendee2.name = "Ushas"

    mediator.presenter = presenter
    mediator.attendees=[attendee1,attendee2]

    presenter.send_new_slide("Slide 1")
    attendee1.ask_question("Question 1?")
    presenter.answer_question("Answer 1", attendee1)
    presenter.send_new_slide("Slide 2")
