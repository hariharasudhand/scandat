import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class spinbox(QWidget):
    def __init__(self, parent= None):
        super(spinbox, self).__init__(parent)

        layout = QVBoxLayout()
        self.b1 = QLabel("the connection is ")
        self.b1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.b1)
        self.sp = QSpinBox()

        layout.addWidget(self.sp)
        self.setLayout(layout)

        self.sp.valueChanged.connect(self.spk)
        self.setWindowTitle("scandat")

    def spk(self):
        self.b1.setText("is connected "+ str(self.sp.value()))

def main():
    app = QApplication(sys.argv)
    ex = spinbox()
    ex.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()