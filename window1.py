import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QApplication, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self, x):                                         # x <-- 3
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.lay = QVBoxLayout(self.centralwidget)

        img_folder_path = 'G:/Scandat/sacndat_studio/Templates'
        dirListing = os.listdir(img_folder_path)

        for i in dirListing:                                          # <---
            self.btn = QPushButton('Button ', self)
            text = self.btn.text()
            self.btn.clicked.connect(lambda ch, text=text : print("\nclicked--> {}".format(text)))
            self.lay.addWidget(self.btn)
            self.btn.clicked.connect(self.clickMethod)

        self.numButton = 4

        pybutton = QPushButton('Create a button', self)
        pybutton.clicked.connect(self.clickMethod)

        self.lay.addWidget(pybutton)
        self.lay.addStretch(1)

    def clickMethod(self):
        newBtn = QPushButton('New Button{}'.format(self.numButton), self)
        self.numButton += 1
        newBtn.clicked.connect(lambda : print("\nclicked===>> {}".format(newBtn.text())))
        self.lay.addWidget(newBtn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(3)                                            # 3 --> x
    mainWin.show()
    sys.exit( app.exec_() )
