from enum import StrEnum
from random import Random

class LetterStatus(StrEnum):
    CORRECT = "🟩"
    INCORRECT = "⬜"
    PARTIAL = "🟨"

    def __str__(self) -> str:
        return self.value


def _load_words(filename: str) -> set[str]:
    with open(filename, "r") as f:
        return {line.strip().upper() for line in f}

_answers = _load_words("src\\answers_list.txt.")
_allowed_guesses = _answers | _load_words("src\\other_allowed_guesses.txt")
    
def is_valid_word(word: str) -> bool:
    return word in _allowed_guesses

def get_random_answer() -> str:
    return Random().choice(tuple(_answers))
