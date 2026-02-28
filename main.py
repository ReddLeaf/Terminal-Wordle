from src.model import WordleModel
from src.view import WordleView
from src.controller import WordleController


if __name__ == "__main__":
    model = WordleModel(6, "APPLE")
    view = WordleView()
    controller = WordleController(model, view)

    controller.start()
