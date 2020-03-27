from StrategyPattern.ScoringAlgorithmBase import ScoringAlgorithmBase


class ChildrenScoringAlgorithm(ScoringAlgorithmBase):
    def calculate_score(self):
        return "Score of Children"
