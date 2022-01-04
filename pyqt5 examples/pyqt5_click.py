import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QDialog()
    b1 = QPushButton(win)
    b1.setText("Button1")
    b1.move(50,20)
    b1.clicked.connect(b1_clicked)

    b2 = QPushButton(win)
    b2.setText("button2")
    b2.move(50,50)
    b2.clicked.connect(b2_clicked)

    win.setGeometry(100,100,300,300)
    win.setWindowTitle("Weeroda")
    win.show()
    sys.exit(app.exec())

def b1_clicked():
    print("button1 is clicked")

def b2_clicked():
    print("button2 is clicked")

if __name__=='__main__':
    window()
