from PyQt6.QtWidgets import QMessageBox
from config.condition import Condition

def send_info(condition, text=''):
    msg = QMessageBox()
    msg.setGeometry(2500, 300, 300, 150)
    if condition == Condition.NOTIFICATION:
        msg.setWindowTitle('Уведомление')
        msg.setIcon(QMessageBox.Icon.Information)
    else:
        msg.setWindowTitle('Ошибка')
        msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()