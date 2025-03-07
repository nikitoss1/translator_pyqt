from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QMessageBox, QPushButton, QLabel, QTextBrowser, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt6.QtGui import QIcon
from config.config import SIZE_OF_WINDOW, LANGUAGES


class ViewTranslate(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.setWindowTitle('Translator')
        self.setGeometry(100, 100, *SIZE_OF_WINDOW)
        self.setFixedSize(*SIZE_OF_WINDOW)

        self.createWidgets()
        self.createLayouts()
        #self.connectSignals()

    
    def createWidgets(self):
        self.button_switch = QPushButton()
        self.button_switch.setFixedSize(25, 25)
        self.button_switch.setIcon(QIcon('./images/button_switch_languages.png'))
        self.button_switch.setStyleSheet('''
            QPushButton {
                background-color: #9788B6;
            }
        ''')
        self.button_translate = QPushButton('Перевести')

        self.text_field_source = QTextEdit()
        self.text_field_source.setPlaceholderText('Введите ваш текст')
        self.text_field_target = QTextBrowser()
        self.text_field_target.setPlaceholderText('Ваш перевод')

        # Добавить слушателей для этих виджетов
        # Как задать максимальный размер списка
        self.language_combo_source = QComboBox()
        self.language_combo_source.addItems([*LANGUAGES.values()])
        self.language_combo_target = QComboBox()
        self.language_combo_target.addItems([*LANGUAGES.values()])


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
        


    # Код ниже для примера
    # def connectSignals(self):
    #     """Подключение сигналов и слотов."""
    #     self.button.clicked.connect(self.onButtonClicked)

    # def onButtonClicked(self):
    #     """Обработчик нажатия кнопки."""
    #     self.label.setText("Кнопка нажата!")
    #     QMessageBox.information(self, "Сообщение", "Вы нажали кнопку!")


if __name__ == "__main__":
    app = QApplication([])
    window = ViewTranslate()
    window.show()
    app.exec()