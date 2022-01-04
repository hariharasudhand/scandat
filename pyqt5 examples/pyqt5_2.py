import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(300,300)
        self.setWindowTitle("Weeroda screen")
        self.label = QLabel(self)
        self.label.setText("welcome to weeroda")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,50)

def main():
        App = QApplication(sys.argv)
        ex = Window()
        ex.show()
        sys.exit(App.exec())
if __name__=='__main__':
        main()