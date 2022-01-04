import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initui()

    def initui(self):
        self.setWindowTitle("scandat")
        self.setGeometry(200,500,400,300)
        self.setWindowIcon(QIcon(QPixmap("logo.png")))
        self.show()

    def contextMenuEvent(self, event):
        contextmenu = QMenu(self)
        new_action = contextmenu.addAction("Open Rect")
        open = contextmenu.addAction("Create Box")
        quit = contextmenu.addAction("quit")
        action = contextmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quit:
            self.close()

app = QApplication(sys.argv)
win = window()
sys.exit(app.exec_())