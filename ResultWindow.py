from PyQt6.QtWidgets import *
import QuestCode
import pygame

def openWindow():
    window = QDialog()

    mainLine = QVBoxLayout()

    pygame.mixer.music.stop()
    victory_sound = pygame.mixer.Sound("Tada.wav")
    victory_sound.play()

    result = QLabel("Результат:" + str(QuestCode.score))

    mainLine.addWidget(result)

    window.setLayout(mainLine)
    window.show()
    window.exec()