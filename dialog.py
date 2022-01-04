import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class dialogapp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
        self.setWindowIcon(QIcon(QPixmap("logo.png")))

        self.button1 = QPushButton("upload Image")
        self.button1.clicked.connect(self.get_image_file)
        self.button2 = QPushButton("Run")


        self.labelimage = QLabel()

        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.labelimage)
        layout.addStretch()
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def get_image_file(self):
        # fileName = QFileDialog.getOpenFileName(self, 'OpenFile', )
        # self.labelimage.setText(fileName)
        # print(fileName)
        # path = QFileDialog.getOpenFileName(self, 'Open a file', '',
        #                                    'All Files (*.xml)')
        # if path != ('', ''):
        #     print("File path : " + path[0])
        #     self.label = QLabel()
        #     self.label.setText(path[0])
        #     self.label.show()
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select project folder:', 'F:\\', QtWidgets.QFileDialog.ShowDirsOnly)
        print(dir_)
        self.label = QListWidget()
        self.label.addItem(dir_)
        self.label.show()
        self.labelimage.setPixmap(QPixmap(dir_))





if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = dialogapp()
    ex.show()
    sys.exit(app.exec())