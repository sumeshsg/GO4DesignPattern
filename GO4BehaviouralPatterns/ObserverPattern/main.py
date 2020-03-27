from ObserverPattern.EventEmailer import EventEmailer
from ObserverPattern.EventLogger import EventLogger
from ObserverPattern.EventReceiver import EventReceiver

if __name__ == '__main__':
    # event_receiver = EventReceiver()
    # event_receiver.log_message("Message with no observers")

    # event_receiver = EventReceiver()
    # emailer = EventEmailer(event_receiver)
    # event_receiver.attach(emailer)
    # event_receiver.log_message("Message with one observers")

    event_receiver = EventReceiver()
    emailer = EventEmailer(event_receiver)
    logger = EventLogger(event_receiver)
    event_receiver.attach(emailer)
    event_receiver.attach(logger)
    event_receiver.log_message("Message with two observers")
