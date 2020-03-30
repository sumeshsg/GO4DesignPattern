from GO4CreationalPatterns.PrototypePattern.Developer import Developer

if __name__ == '__main__':
    developer_sg = Developer('SG', 'Python')
    developer_ushas = developer_sg.clone()
    developer_ushas.set_name('Ushas')

    print("Developer SG Details")
    print(developer_sg.get_name(), developer_sg.get_skill())

    print("Developer Ushas Details")
    print(developer_ushas.get_name(), developer_ushas.get_skill())
