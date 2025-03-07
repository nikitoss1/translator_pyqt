from PyQt6.QtWidgets import QApplication
from model.model_translate import ModelTranslate
from view.view_translate import ViewTranslate
from presenter.presenter import PresenterTranslate

if __name__ == '__main__':
    app = QApplication([])

    model = ModelTranslate()
    view = ViewTranslate()
    presenter = PresenterTranslate(model, view)


    view.show()
    app.exec()