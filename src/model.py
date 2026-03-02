from .utils import LetterStatus


class WordleModel:
    def __init__(self, max_attempts: int, answer: str) -> None:
        self._max_attempts = self._attempts = max_attempts
        self._answer = answer
        self._guesses: list[list[None | LetterStatus]] = []

        self._is_game_over = False

    @property
    def is_game_over(self):
        return self._is_game_over
    
    @property
    def answer(self):
        return self._answer
    
    @property
    def attempts(self):
        return self._attempts
    
    @property
    def max_attempts(self):
        return self._max_attempts
    
    @property
    def results(self):
        return self._guesses
    
    def did_player_win(self) -> bool:
        if self._attempts > 0 and self._is_game_over:
            return True
        return False
    
    def make_guess(self, guess: str) -> list[None | LetterStatus]:
        remaining = list(self._answer)
        status: list[None | LetterStatus] = [None] * len(self._answer)

        for i in range(len(self._answer)):
            if guess[i] == remaining[i]:
                status[i] = LetterStatus.CORRECT
                remaining[i] = ""
        
        for i in range(len(self._answer)):
            if status[i] is None:
                if guess[i] in remaining:
                    status[i] = LetterStatus.PARTIAL
                    remaining[remaining.index(guess[i])] = ""
                else:
                    status[i] = LetterStatus.INCORRECT
        self._guesses.append(status)
        return status
    
    def next_attempt(self):
        assert self._attempts
        if all(status == LetterStatus.CORRECT for status in self._guesses[-1]):
            self._is_game_over = True
        else:
            self._attempts -= 1
            if self._attempts == 0:
                self._is_game_over = True
