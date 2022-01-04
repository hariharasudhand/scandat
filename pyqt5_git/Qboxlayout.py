import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    b1 = QPushButton("button1")
    b2 = QPushButton("button2")
    b3 = QPushButton("button3")
    b4 = QPushButton("button4")

    vbox = QVBoxLayout()
    hbox = QHBoxLayout()

    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(b2)

    hbox.addWidget(b3)
    hbox.addStretch()
    hbox.addWidget(b4)

    vbox.addStretch()
    vbox.addLayout(hbox)
    win.setLayout(vbox)

    win.setWindowTitle("scandat studio")
    win.setGeometry(200,300,200,200)
    win.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    window()
