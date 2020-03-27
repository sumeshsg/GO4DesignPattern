from RobotCommand import RobotCommand
from Robot import Robot


class MoveCommand(RobotCommand):
    _robot = Robot()
    distance = 0

    def __init__(self, robot):
        self._robot = robot

    def execute(self):
        self._robot.move(self.distance)

    def undo(self):
        self._robot.move(-self.distance)
