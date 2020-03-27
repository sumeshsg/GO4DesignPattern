from abc import abstractmethod


class ScoringAlgorithmBase(object):
    @abstractmethod
    def calculate_score(self):
        pass
