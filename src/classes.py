from enum import Enum, auto

class LetterStatus(Enum):
    CORRECT = auto()
    INCORRECT = auto()
    PARTIAL = auto()


class Player:
    def __init__(self) -> None:
        self._correct: set[str] = set()
        self._incorrect: set[str] = set()
        self._partial: set[str] = set()
