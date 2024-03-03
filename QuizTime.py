from PyQt6.QtWidgets import *

def openWindow():
    window = QDialog()

    mainLine = QVBoxLayout()

    extraLine1 = QHBoxLayout()
    question1 = QLabel("На літаку було 500 цеглинок, одна цеглинка випала з літака. Скільки цеглинок лишилось?")
    answer1 = QRadioButton("512")
    answer2 = QRadioButton("501")
    answer3 = QRadioButton("499")
    answer4 = QRadioButton("536")

    extraLine1.addWidget(question1)
    extraLine1.addWidget(answer1)
    extraLine1.addWidget(answer2)
    extraLine1.addWidget(answer3)
    extraLine1.addWidget(answer4)
    mainLine.addWidget(extraLine1)


    window.setLayout(mainLine)
    window.show()
    window.exec()