import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class combo(QComboBox):

    def __init__(self, title, parent):
        super(combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)

        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class example(QWidget):
    def __init__(self):
        super(example, self).__init__()

        self.Initui()

    def Initui(self):
        lo = QFormLayout()
        lo.addRow(QLabel("enter the text and drag it into combobox"))


        edit = QLineEdit()
        edit.setDragEnabled(True)
        com = combo("Button", self)
        lo.addRow(edit, com)
        self.setLayout(lo)
        self.setWindowTitle("deag&drop")

def main():
    app = QApplication(sys.argv)
    ex = example()
    ex.show()
    app.exec_()

if __name__=="__main__":
    main()

