import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    b1 = QPushButton("button1")
    b2 = QPushButton("button2")

    box = QVBoxLayout()
    box.addWidget(b1)
    box.addStretch()
    box.addWidget(b2)

    win.setLayout(box)
    win.setWindowTitle("scandat studio")
    win.setGeometry(100,200,200,300)
    win.show()

    sys.exit(app.exec())

if __name__=="__main__":
    window()