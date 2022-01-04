import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def winsdow():
    app = QApplication(sys.argv)
    win = QWidget()

    l1 = QLabel("Name")
    nm = QLineEdit()
    fbox = QFormLayout()
    fbox.addRow(l1, nm)

    vbox = QVBoxLayout()
    l2 = QLabel("address")
    nm2 = QLineEdit()
    nm3 = QLineEdit()
    vbox.addWidget(nm2)
    vbox.addWidget(nm3)
    fbox.addRow(l2, vbox)

    hbox = QHBoxLayout()
    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    fbox.addRow(QLabel("sex"), hbox)
    fbox.addRow(QPushButton("submit"), QPushButton("cancel"))

    win.setLayout(fbox)
    win.setWindowTitle("scandat studio")
    win.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    winsdow()