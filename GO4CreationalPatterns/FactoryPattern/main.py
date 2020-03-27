from GO4CreationalPatterns.FactoryPattern.ButtonFactory import ButtonFactory

if __name__ == '__main__':
    button_factory = ButtonFactory()
    button_types = ['image', 'input', 'flash']
    for button_type in button_types:
        button_obj = button_factory.create_button(button_type)
        print(button_obj.get_html())
