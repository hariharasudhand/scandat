import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Radiobutton(QWidget):
    def __init__(self, parent= None):
        super(Radiobutton, self).__init__(parent)

        layout = QHBoxLayout()
        self.l1 = QRadioButton("button1")
        self.l1.setChecked(True)
        self.l1.toggled.connect(lambda : self.btnstate(self.l1))
        layout.addWidget(self.l1)

        self.l2 = QRadioButton("button2")
        self.l2.toggled.connect(lambda : self.btnstate(self.l2))


        layout.addWidget(self.l2)
        self.setLayout(layout)
        self.setWindowTitle("weeroda ")

    def btnstate(self, b):
            if b.text() == "button1":
                if b.isChecked() == True:
                    print(b.text() + " is selected")
                else:
                    print(b.text()+"is not selected")

            if b.text() == "button2":
                if b.isChecked() == True:
                    print(b.text() + " is selected")
                else:
                    print(b.text() +"is not selected")
def main():
    app = QApplication(sys.argv)
    w = Radiobutton()
    w.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()







