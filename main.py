from src.model import WordleModel
from src.view import WordleView
from src.controller import WordleController
from src.utils import get_random_answer


if __name__ == "__main__":
    max_attempts = 6
    answer = get_random_answer()
    model = WordleModel(max_attempts, "LINEN")
    view = WordleView()
    controller = WordleController(model, view)

    controller.start()
