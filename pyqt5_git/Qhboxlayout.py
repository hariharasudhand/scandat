import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    b1 = QPushButton("Button1")
    b2 = QPushButton("Button2")

    box = QHBoxLayout()
    box.addWidget(b1)
    box.addStretch()
    box.addWidget(b2)
    win.setLayout(box)
    win.setWindowTitle("weeroda")
    win.setGeometry(200,100, 300,200)
    win.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    window()