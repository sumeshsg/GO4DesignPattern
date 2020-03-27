class RobotController:

    def __init__(self):
        self.command_list = []

    def execute_command(self):
        print ('Execute Command')
        for command in self.command_list:
            command.execute()

    def undo_command(self):
        print ('Undo Command')
        for command in reversed(self.command_list):
            command.undo()
