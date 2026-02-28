from classes import LetterStatus


class WordleModel:
    def __init__(self, max_attempts: int) -> None:
        self._attempts = max_attempts

        self._is_game_over = False
        self._answer = ...

    @property
    def is_game_over(self):
        return self._is_game_over
