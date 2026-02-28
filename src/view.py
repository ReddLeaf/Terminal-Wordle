from .utils import LetterStatus, is_valid_word


class WordleView:
    def ask_for_guess(self) -> str:
        guess = ""

        while len(guess) != 5 or not guess.isalpha() or not is_valid_word(guess):
            guess = input("Make your guess [5-letters]: ").upper().strip()

            if len(guess) != 5:
                print("Your word has to be 5 letters long!")
            
            elif not guess.isalpha() or not is_valid_word(guess):
                print("That's not a valid word!")

        print()
        return guess   
            
    def show_guess_status(self, guess: str, status: list[None | LetterStatus]) -> None:
        print(" " + "   ".join(list(guess)))
        print("  ".join(str(stat) for stat in status))
        print()

    def show_end_message(self, win: bool, answer: str, attempts: int) -> None:
        if win:
            match attempts:
                case 6:
                    print("Genius!")
                case 5:
                    print("Magnificent!")
                case 4:
                    print("Impressive!")
                case 3:
                    print("Splendid!")
                case 2:
                    print("Great!")
                case 1:
                    print("Phew...")
                case _: # > 6
                    print("Genius!")
            print("You got it!")
        else:
            print(f"Better luck next time, the word was {answer}.")
