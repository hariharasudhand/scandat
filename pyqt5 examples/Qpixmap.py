import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def mainwindow():
    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel()
    l1.setPixmap(QPixmap("logo.png"))

    box = QVBoxLayout()
    box.addWidget(l1)
    win.setLayout(box)
    win.setWindowTitle("Weeroda")
    win.show()
    sys.exit(app.exec())

if __name__=="__main__":
    mainwindow()