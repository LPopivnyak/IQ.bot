from PyQt6.QtWidgets import *
import QuizTime

app = QApplication([])
window = QWidget()

mainLine1 = QVBoxLayout()

Title = QLabel("IQtest.bot")
startButton = QPushButton("Почати")

mainLine1.addWidget(Title)
mainLine1.addWidget(startButton)


startButton.clicked.connect(QuizTime.openWindow)
window.setLayout(mainLine1)
window.show()
app.exec()