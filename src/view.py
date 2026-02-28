from classes import LetterStatus

class WordleView:
    def ask_for_guess(self) -> str:
        guess = ""

        while len(guess) != 5 or not guess.isalpha():
            guess = input("Make your guess [5-letters]: ").upper().strip()

            if len(guess) != 5:
                print("Your word has to be 5 letters long!")
            
            if not guess.isalpha():
                print("That's not a valid word!")

        return guess   
            
    def show_guess_status(self, guess: str, status: LetterStatus) -> None:
        ...