from enum import StrEnum


class LetterStatus(StrEnum):
    CORRECT = "🟩"
    INCORRECT = "⬜"
    PARTIAL = "🟨"

    def __str__(self) -> str:
        return self.value
