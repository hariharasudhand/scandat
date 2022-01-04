import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def window():

    app = QApplication(sys.argv)
    w = QWidget()
    l = QPushButton(w)
    l.setText("open")
    l.move(50,50)
    l.clicked.connect(Dialog)
    w.setWindowTitle("Weeroda")
    w.show()
    sys.exit(app.exec())

def Dialog():

    v = QDialog()
    layout = QHBoxLayout()
    s = QPushButton("ok", v)
    s.move(50,50)
    v.setWindowTitle("Qdailog")
    v.setWindowModality(Qt.ApplicationModal)
    v.exec()

if __name__=="__main__":
    window()