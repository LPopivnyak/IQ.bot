from PyQt6.QtWidgets import *
import QuestCode

def openWindow():
    window = QDialog()

    mainLine = QVBoxLayout()

    result = QLabel("Результат:" + str(QuestCode.score))

    mainLine.addWidget(result)

    window.setLayout(mainLine)
    window.show()
    window.exec()