from PyQt6.QtWidgets import QTextEdit

class PlainTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def insertFromMimeData(self, source):
        if source.hasText():
            plain_text = source.text()
            cursor = self.textCursor()
            cursor.insertText(plain_text)