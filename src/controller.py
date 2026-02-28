class WordleController:
    def __init__(self, model: ..., view: ...) -> None:
        self._model = model
        self._view = view

    def start(self):
        model = self._model
        view = self._view

        while not model.is_game_over:
            guess = view.ask_for_guess()
            status = model.make_guess(guess)
            view.show_guess_status(guess, status) # SATCH
                                                  # BGGGG
        
        view.show_end_message()