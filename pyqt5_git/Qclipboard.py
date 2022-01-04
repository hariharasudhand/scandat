import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.Initui()

    def Initui(self):
        box = QVBoxLayout()
        self.Text1 = QTextEdit()
        self.btn1 = QPushButton("copy")
        box.addWidget(self.Text1)
        box.addWidget(self.btn1)
        self.Text2 = QTextEdit()
        self.btn2 = QPushButton("paste")
        box.addWidget(self.Text2)
        box.addWidget(self.btn2)
        self.btn1.clicked.connect(self.copy)
        self.btn2.clicked.connect(self.paste)
        self.setLayout(box)

        self.setGeometry(100,100, 300,200)
        self.setWindowTitle("weeroda")
        self.show()

    def copy(self):
        self.Text1.copy()
        print(clipboard.text())

        msg = QMessageBox()
        msg.setText(clipboard.text()+"copied on clipboard")
        msg.exec_()

    def paste(self):
        self.Text2.setText(clipboard.text())


app = QApplication(sys.argv)
clipboard = app.clipboard()
ex = Example()
ex.show()
sys.exit(app.exec())