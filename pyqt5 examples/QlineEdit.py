import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def Window():
    app = QApplication(sys.argv)
    w = QWidget()

    a1 = QLineEdit()
    a1.setValidator(QIntValidator())
    a1.setMaxLength(4)
    a1.setAlignment(Qt.AlignRight)
    a1.setFont(QFont("arial", 20))

    a2 = QLineEdit()
    a2.setValidator(QDoubleValidator(0.99, 99.99, 2))

    flo = QFormLayout()
    flo.addRow("Int Vlaidator", a1)
    flo.addRow("Double Validator", a2)

    a3 = QLineEdit()
    a3.setInputMask('+99_9999_999999')
    flo.addRow("set inputmask", a3)

    a4 = QLineEdit()
    a4.textChanged.connect(textchanged)
    flo.addRow("Text changed ", a4)

    a5 = QLineEdit()
    a5.setEchoMode(QLineEdit.Password)
    flo.addRow("password", a5)

    a6 = QLineEdit()
    a6.setReadOnly(True)
    flo.addRow("Read only", a6)

    a5.editingFinished.connect(editingfinish)
    w.setLayout(flo)
    w.setWindowTitle("weeroda form")
    w.show()
    sys.exit(app.exec())

def textchanged(text):
    print("the text is changed" + text)

def editingfinish():
    print("the editing is finish")

if __name__=="__main__":
    Window()



