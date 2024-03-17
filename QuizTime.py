from PyQt6.QtWidgets import *
import random
import QuestCode

def openWindow():
    window = QDialog()

    mainLine = QVBoxLayout()

    question1 = QLabel("На літаку було 500 цеглинок, одна цеглинка випала з літака. Скільки цеглинок лишилось?")
    answersGroup1 = QGroupBox("Варіанти відповідей:")
    answersLine1 = QVBoxLayout()
    answer1 = QRadioButton("512")
    answer2 = QRadioButton("501")
    answer3 = QRadioButton("499")
    answer4 = QRadioButton("536")
    answers = [answer1, answer2, answer3, answer4]

    result = QLabel("Результат:")
    answerButton = QPushButton("Відповісти")
    nextQuestButton = QPushButton("Наступне питання")

    mainLine.addWidget(question1)
    mainLine.addWidget(answer1)
    mainLine.addWidget(answer2)
    mainLine.addWidget(answer3)
    mainLine.addWidget(answer4)

    answersLine1.addWidget(result)
    result.hide()
    answersGroup1.setLayout(answersLine1)
    mainLine.addWidget(answersGroup1)

    def showQuest():
        random.shuffle(answers)
        question1.setText(QuestCode.quest[QuestCode.currentQuest]["Питання"])
        answers[0].setText(QuestCode.quest[QuestCode.currentQuest]["Неправильна відповідь1"])
        answers[1].setText(QuestCode.quest[QuestCode.currentQuest]["Неправильна відповідь2"])
        answers[2].setText(QuestCode.quest[QuestCode.currentQuest]["Правильна відповідь"])
        answers[3].setText(QuestCode.quest[QuestCode.currentQuest]["Неправильна відповідь3"])

    showQuest()

    def showResult():
        answers[0].hide()
        answers[1].hide()
        answers[2].hide()
        answers[3].hide()
        answerButton.hide()
        result.show()
        nextQuestButton.show()

        if answers[2].isChecked():
            result.setText("Правильно")
        else:
            result.setText("Неправильно")

    def nextQuestionFunc():
        answers[0].show()
        answers[1].show()
        answers[2].show()
        answers[3].show()
        answerButton.show()
        result.hide()
        nextQuestButton.hide()
        showQuest()
        QuestCode.currentQuest += 1

    nextQuestionFunc()

    answerButton.clicked.connect(showResult)
    nextQuestButton.clicked.connect(nextQuestionFunc)

    window.setLayout(mainLine)
    window.show()
    window.exec()