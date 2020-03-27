from GO4BehaviouralPatterns.StrategyPattern.ScoringAlgorithmBase import ScoringAlgorithmBase


class WomenScoringAlgorithm(ScoringAlgorithmBase):
    def calculate_score(self):
        return "Score of Women"
