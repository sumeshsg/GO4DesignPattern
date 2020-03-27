class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is single ton")
        else:
            Singleton._instance = self

    @staticmethod
    def get_instance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
