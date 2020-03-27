class PersonnelSystem(object):

    def __init__(self):
        self._employee_details = []
        self._employee_details.append(["1210", "Ushas", "Team Leader"])
        self._employee_details.append(["3322", "SG", "Developer"])
        self._employee_details.append(["1211", "June", "Team Leader"])

    def get_employee(self):
        return self._employee_details
