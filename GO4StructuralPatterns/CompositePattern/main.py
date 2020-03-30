from GO4StructuralPatterns.CompositePattern.Employee import Employee


def print_subordinate(group_manager):
    print('--', group_manager.get_name())
    for employee in group_manager.get_subordinates():
        print(' ', employee.get_name())
        for employee_1 in employee.get_subordinates():
            print_subordinate(employee_1)


if __name__ == '__main__':
    group_manager = Employee('Group Manager')
    manager_1 = Employee('Manager 1')
    manager_2 = Employee('Manager 2')
    group_manager.add_subordinate(manager_1)
    group_manager.add_subordinate(manager_2)

    team_lead_1 = Employee('TeamLead 1')
    manager_1.add_subordinate(team_lead_1)
    team_lead_2 = Employee('TeamLead 2')
    manager_2.add_subordinate(team_lead_2)

    developer_1 = Employee('Developer 1')
    developer_2 = Employee('Developer 2')
    team_lead_1.add_subordinate(developer_1)
    team_lead_1.add_subordinate(developer_2)

    developer_3 = Employee('Developer 3')
    developer_4 = Employee('Developer 4')
    team_lead_2.add_subordinate(developer_3)
    team_lead_2.add_subordinate(developer_4)
    print_subordinate(group_manager)
