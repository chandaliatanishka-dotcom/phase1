class InvalidScoreError(Exception):
    """Raised when score is outside 0-100"""
    pass


class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        if not 0 <= score <= 100:
            raise InvalidScoreError(f"{score} is invalid. Must be 0-100.")
        self._score = score

    @property
    def score(self):
        return self._score

    @property
    def grade(self):
        if self._score >= 90: return "A"
        elif self._score >= 80: return "B"
        elif self._score >= 70: return "C"
        elif self._score >= 60: return "D"
        else: return "F"

    def __str__(self):
        return f"{self.name}: {self.score} ({self.grade})"