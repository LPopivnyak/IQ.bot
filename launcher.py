import PyQt6
from PyQt6.QtWidgets import *
import QuizTime

app = QApplication([])
window = QWidget()
window.resize(350, 250)

mainLine = QVBoxLayout()

Title = QLabel("IQtest.bot")
startButton = QPushButton("Почати")

mainLine.addWidget(Title)
mainLine.addWidget(startButton)


app.setStyleSheet("""
        QWidget {
            background: #FFFFFF;
        }
        
        QPushButton {
            background: #FFFFFF;
            border: 5px solid #FFFFFF;
            border-radius: 1px;
            border: 5px solid #000000;
            padding: 1px 5px;
            min-width: 120px;
            min-height: 35px;
        }
        
        """)



startButton.clicked.connect(QuizTime.openWindow)
window.setLayout(mainLine)
window.show()
app.exec()