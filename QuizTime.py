from PyQt6.QtWidgets import *

def openWindow():
    window = QDialog()

    mainLine = QVBoxLayout()

    question1 = QLabel("На літаку було 500 цеглинок, одна цеглинка випала з літака. Скільки цеглинок лишилось?")
    answer1 = QRadioButton("512")
    answer2 = QRadioButton("501")
    answer3 = QRadioButton("499")
    answer4 = QRadioButton("536")

    mainLine.addWidget(question1)
    mainLine.addWidget(answer1)
    mainLine.addWidget(answer2)
    mainLine.addWidget(answer3)
    mainLine.addWidget(answer4)


    window.setLayout(mainLine)
    window.show()
    window.exec()