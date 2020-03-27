from Command.RobotCommand import RobotCommand
from Command.Robot import Robot


class RotateCommand(RobotCommand):
    _robot = Robot()
    distance = 0

    def __init__(self, robot):
        self._robot = robot

    def execute(self):
        self._robot.rotate(self.distance)

    def undo(self):
        self._robot.rotate(-self.distance)
