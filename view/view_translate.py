from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QComboBox,
    QMessageBox,
    QPushButton,
    QLabel,
    QTextBrowser,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor
from config.constants import SIZE_OF_WINDOW, LANGUAGES_SOURCE, LANGUAGES_TARGET
from view.styles.styles import (
    BUTTON_STYLE,
    TEXT_BROWSER_STYLE,
    COMBO_BOX_STYLE,
    TEXT_EDIT_STYLE,
    BACKGROUND_COLOR,
)
from config.condition import Condition


class ViewTranslate(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Translator")
        self.setGeometry(100, 100, *SIZE_OF_WINDOW)
        self.setFixedSize(*SIZE_OF_WINDOW)

        self.createWidgets()
        self.createLayouts()
        self.setStyles()
        # self.connectSignals()

    def createWidgets(self):
        self.button_switch = QPushButton()
        self.button_switch.setFixedSize(25, 25)
        self.button_switch.setIcon(QIcon("./images/button_switch_languages.png"))
        self.button_switch.setCursor(Qt.CursorShape.PointingHandCursor)

        self.button_translate = QPushButton("Перевести")
        self.button_translate.setCursor(Qt.CursorShape.PointingHandCursor)

        self.text_field_source = PlainTextEdit()
        self.text_field_source.setPlaceholderText("Введите ваш текст")
        self.text_field_target = QTextBrowser()
        self.text_field_target.setPlaceholderText("Ваш перевод")

        self.language_combo_source = QComboBox()
        self.language_combo_source.addItems([*LANGUAGES_SOURCE.keys()])
        self.language_combo_source.setCursor(Qt.CursorShape.PointingHandCursor)

        self.language_combo_target = QComboBox()
        self.language_combo_target.addItems([*LANGUAGES_TARGET.keys()])
        self.language_combo_target.setCursor(Qt.CursorShape.PointingHandCursor)

    def createLayouts(self):
        layout_top = QHBoxLayout()
        layout_top.addWidget(self.language_combo_source)
        layout_top.addWidget(self.button_switch)
        layout_top.addWidget(self.language_combo_target)

        layout_fields = QHBoxLayout()
        layout_fields.addWidget(self.text_field_source)
        layout_fields.addWidget(self.text_field_target)

        layout_bottom = QHBoxLayout()
        layout_bottom.addWidget(self.button_translate)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout_top)
        main_layout.addLayout(layout_fields)
        main_layout.addLayout(layout_bottom)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def connectSignals(self, presenter):
        """Подключение сигналов и слотов."""
        self.presenter = presenter
        self.button_switch.clicked.connect(self.switch_languages)
        self.button_translate.clicked.connect(self.translate_text)

    def translate_text(self):
        if not self.text_field_source.toPlainText().strip():
            self.message(Condition.NOTIFICATION, "Напишите какой-нибудь текст")
        else:
            self.presenter.translate_text()

    def switch_languages(self):
        current_source = self.language_combo_source.currentText()
        current_target = self.language_combo_target.currentText()

        self.language_combo_source.setCurrentText(current_target)
        self.language_combo_target.setCurrentText(current_source)

        temp = self.text_field_source.toPlainText()
        self.text_field_source.setText(self.text_field_target.toPlainText())
        self.text_field_target.setText(temp)

    def setStyles(self):
        self.button_switch.setStyleSheet(
            """
            QPushButton {
                background-color: #9788B6;
            }
        """
        )
        self.text_field_source.setStyleSheet(TEXT_EDIT_STYLE)
        self.text_field_target.setStyleSheet(TEXT_BROWSER_STYLE)
        self.language_combo_source.setStyleSheet(COMBO_BOX_STYLE)
        self.language_combo_target.setStyleSheet(COMBO_BOX_STYLE)
        self.button_translate.setStyleSheet(BUTTON_STYLE)
        self.setStyleSheet(BACKGROUND_COLOR)

    def current_source_lang(self):
        return self.language_combo_source.currentText()

    def current_target_lang(self):
        return self.language_combo_target.currentText()

    def current_text(self):
        return self.text_field_source.toPlainText()

    def write_translate_in_browser(self, text):
        self.text_field_target.setText(text)

    def message(self, condition, text=""):
        msg = QMessageBox(self)
        if condition == Condition.NOTIFICATION:
            msg.setWindowTitle("Уведомление")
            msg.setIcon(QMessageBox.Icon.Information)
        else:
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setWindowFlags(Qt.WindowType.Dialog)
        msg.exec()

class PlainTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def insertFromMimeData(self, source):
        if source.hasText():
            plain_text = source.text() 
            cursor = self.textCursor()
            cursor.insertText(plain_text)


if __name__ == "__main__":
    app = QApplication([])
    window = ViewTranslate()
    window.show()
    app.exec()
