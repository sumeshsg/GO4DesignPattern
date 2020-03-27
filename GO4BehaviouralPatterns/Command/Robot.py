class Robot:
    def __init__(self):
        pass

    @staticmethod
    def move(distance):
        if distance > 0:
            print ("Robot move forwards {0}mm".format(distance))
        else:
            print ("Robot move backwards {0}mm".format(-distance))

    @staticmethod
    def rotate(distance):
        if distance > 0:
            print ("Robot move right {0}mm".format(distance))
        else:
            print ("Robot move left {0}mm".format(-distance))

    @staticmethod
    def scoop(action):
        if action:
            print ("Robot gathered soil in scoop")
        else:
            print ("Robot release soil from scoop")
