from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon('logo.png'))


        self.acceptDrops()
        # set the title
        self.setWindowTitle("Weeroda")

        # setting the geometry of window
        self.setGeometry(0, 0, 800, 600)
        #self.pixmap4 = pixmap.scaled(64, 64)

        # creating label
        self.label = QLabel(self)

        # loading image
        self.pixmap = QPixmap('logo.png')


        # adding image to label
        self.label.setPixmap(self.pixmap)
        self.label.move(0, 0)

        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        #self.label.smaller_pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

