import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)

        layout = QHBoxLayout()
        self.b1 = QCheckBox("button1")
        self.b1.setChecked(True)
        self.b1.clicked.connect(lambda : self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QCheckBox("button2")
        self.b2.clicked.connect(lambda: self.btnstate(self.b2))
        layout.addWidget(self.b2)

        self.setWindowTitle("weeroda")
        self.setLayout(layout)

    def btnstate(self, b):
        if b.text()=="button1":
            if b.isChecked()==True:
                print(b.text()+ "is selected")
            else:
                print(b.text()+ " is deselected")

        if b.text()=="button2":
            if b.isChecked()==True:
                print(b.text()+ "is selected")
            else:
                print(b.text()+ " is deselected")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec())