import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("@Hichem")
        self.setGeometry(100, 100, 600, 600)
        self.UiComponents()
        self.show()


    def UiComponents(self):
        calendrier = QCalendarWidget(self)
        calendrier.setGeometry(10, 10, 400, 250)
        push = QPushButton("Année Suivante", self)

        push.setGeometry(120, 280, 100, 40)

        push.clicked.connect(lambda: do_action())

        def do_action():
            calendrier.showNextYear()


App = QApplication(sys.argv)
window = Fenetre()
sys.exit(App.exec())
