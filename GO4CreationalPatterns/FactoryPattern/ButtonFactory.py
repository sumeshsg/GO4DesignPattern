class Button(object):
    html = None

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img></img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory(object):
    @staticmethod
    def create_button(type):
        target_class = type.capitalize()
        return globals()[target_class]()
