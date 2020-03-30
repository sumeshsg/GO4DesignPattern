from GO4StructuralPatterns.BridgePattern.MessageSenderBase import MessageSenderBase


class EmailSender(MessageSenderBase):
    def send_message(self, title, details, importance):
        print("Message sending using Email: \n{0}\n{1}\n{2}\n".format(title, details, importance))
