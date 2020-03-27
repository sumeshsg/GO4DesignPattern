from RobotCommand import RobotCommand
from Robot import Robot


class ScoopCommand(RobotCommand):
    _robot = Robot()
    action = None

    def __init__(self, robot):
        self._robot = robot

    def execute(self):
        self._robot.scoop(self.action)

    def undo(self):
        self._robot.scoop(not self.action)
