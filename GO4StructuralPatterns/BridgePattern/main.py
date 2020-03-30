from GO4StructuralPatterns.BridgePattern.EmailSender import EmailSender
from GO4StructuralPatterns.BridgePattern.Message import Message
from GO4StructuralPatterns.BridgePattern.MsmqSender import MsmqSender
from GO4StructuralPatterns.BridgePattern.WebServiceSender import WebServiceSender

if __name__ == '__main__':
    message = Message("Message Title", "Message Deatils", "High")
    email = EmailSender()
    queue = MsmqSender()
    web = WebServiceSender()
    print(">>>>>>>>> Message Via Email")
    message.set_message_sender(email)
    message.send()
    print(">>>>>>>>> Message Via Queue")
    message.set_message_sender(queue)
    message.send()
    print(">>>>>>>>> Message Via WebService")
    message.set_message_sender(web)
    message.send()
