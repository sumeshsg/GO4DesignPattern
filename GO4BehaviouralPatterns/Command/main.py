from GO4BehaviouralPatterns.Command.Robot import Robot
from GO4BehaviouralPatterns.Command.RobotController import RobotController
from GO4BehaviouralPatterns.Command.MoveCommand import MoveCommand
from GO4BehaviouralPatterns.Command.RotateCommand import RotateCommand
from GO4BehaviouralPatterns.Command.ScoopCommand import ScoopCommand

if __name__ == '__main__':
    robot = Robot()
    robot_controller = RobotController()

    move_command = MoveCommand(robot)
    move_command.distance = 10
    robot_controller.command_list.append(move_command)
    rotate_command = RotateCommand(robot)
    rotate_command.distance = 10
    robot_controller.command_list.append(rotate_command)
    scoop_command = ScoopCommand(robot)
    scoop_command.action = True
    robot_controller.command_list.append(scoop_command)

    robot_controller.execute_command()
    robot_controller.undo_command()
