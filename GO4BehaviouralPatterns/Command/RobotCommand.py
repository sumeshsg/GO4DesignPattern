from abc import abstractmethod


class RobotCommand:
    def __init__(self, robot):
        _robot = robot

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
