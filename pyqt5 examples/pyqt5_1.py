import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class window():

    app = QApplication(sys.argv)

    w = QWidget()
    l = QLabel(w)
    l.setText("Welcome to Weeroda")
    w.setGeometry(100,100,300,400)
    l.move(100,100)
    w.setWindowTitle("Weeroda")
    w.show()
    sys.exit(app.exec())

if __name__=="__main__":
    window()
