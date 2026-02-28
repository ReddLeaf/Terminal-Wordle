from .model import WordleModel
from .view import WordleView

class WordleController:
    def __init__(self, model: WordleModel, view: WordleView) -> None:
        self._model = model
        self._view = view

    def start(self):
        model = self._model
        view = self._view

        while not model.is_game_over:
            guess = view.ask_for_guess()
            status = model.make_guess(guess)
            view.show_guess_status(guess, status)
            model.next_attempt()
        
        view.show_end_message(model.did_player_win(), model.answer, model.attempts)
