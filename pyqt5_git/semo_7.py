# menubar

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initui()

    def initui(self):
        exit = QAction(QIcon("logo.png"), "&Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip("Exit Application")
        exit.triggered.connect(qApp.quit)

        self.statusBar()

        menu = self.menuBar()
        file = menu.addMenu("&File")
        file.addAction(exit)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("scandat")
        self.show()

def main():
    app = QApplication([])
    ex = Example()
    app.exec_()

if __name__=="__main__":
    main()