from StrategyPattern.MenScoringAlgorithm import MenScoringAlgorithm
from StrategyPattern.Scoreboard import Scoreboard
from StrategyPattern.WomenScoringAlgorithm import WomenScoringAlgorithm

if __name__ == '__main__':
    scoreboard = Scoreboard()
    men_scoring_algorithm = MenScoringAlgorithm()
    scoreboard.scoring = men_scoring_algorithm
    scoreboard.show_score()

    women_scoring_algorithm=WomenScoringAlgorithm()
    scoreboard.scoring=women_scoring_algorithm
    scoreboard.show_score()
