import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QCursor
import sys
import constants


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scandat Studio")
        self.setGeometry(20, 30, 1300, 800)
        self.setStyleSheet("background:#2c3644")

        self.label_4 = QLabel(' FILE EXECUTION ', self)
        # self.label_4.move(360, 665)
        self.label_4.setFont(QFont('Arial', 20))
        self.label_4.setGeometry(550, 120, 400, 20)
        self.label_4.setStyleSheet("color:#10bc83")

        self.label = QLabel(self)

        # loading image
        self.pixmap = QPixmap("logo.png")

        # adding image to label
        self.label.setPixmap(self.pixmap)

        # Optional, resize label to image size
        self.label.resize(200, 100)
        self.label.move(620, 10)


        Go_Back = QPushButton('GO BACK', self)
        Go_Back.setGeometry(650, 660, 100, 30)
        Go_Back.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        Go_Back.setStyleSheet("QPushButton {background-color: #bcae10;}"
                              "QPushButton:hover { background-color: #64ccef;}")
        Go_Back.clicked.connect(self.onClicked)


        self.scale = 1

    def Image_text_loading(self, Image_Name):
        df = pd.read_csv(constants.CSV_dir+'/'+Image_Name+'.csv',header=None, encoding="utf-8", on_bad_lines='skip')
        print(df)
        self.listview2 = QLabel(self)
        self.listview2.move(850, 190)
        self.listview2.setStyleSheet("border :3px solid black;")
        self.listview2.setStyleSheet('background:#ffffff')
        self.listview2.resize(400, 450)
        self.listview2.setText(str(df))
        self.im = QPixmap(constants.plot_image_dir+'/'+Image_Name)
        self.listview = QLabel(self)
        self.listview.setScaledContents(True)
        self.listview.setMinimumSize(800, 500)
        self.fileModel = QFileSystemModel()
        self.listview.move(30, 150)
        self.listview.setStyleSheet("border :3px solid black;")
        # self.listview.resize(370, 400)
        self.listview.setPixmap(self.im)

        return Image_Name

    def onClicked(self):
        self.close()


def ShowWindow():
    app = QApplication(sys.argv)
    win = Window3()
    win.show()
    sys.exit(app.exec_())

# ShowWindow()