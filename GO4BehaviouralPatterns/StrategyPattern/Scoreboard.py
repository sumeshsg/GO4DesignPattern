class Scoreboard(object):
    scoring = None

    def show_score(self):
        print(self.scoring.calculate_score())
