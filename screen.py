import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox,QHBoxLayout, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import pyqtSlot
import webbrowser
import os


class App(QWidget ):

    def __init__(self):
        super().__init__()
        self.title = 'ScanDat-Run Automation'
        self.left = 20
        self.top = 30
        self.width = 1300
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('logo5.png'))

        button = QPushButton('Run', self)
        button.setToolTip('This is an example button')
        button.setGeometry(500, 600, 100, 30)
        button.clicked.connect(self.on_click)

        button2 = QPushButton('Open Dir', self)
        button2.setToolTip('this is for open directory')
        button2.setGeometry(150,100,170,30)
        button2.clicked.connect(self.dialog)

        button3 = QPushButton('Select Bounding Template', self)
        button3.setToolTip('this is for open directory')
        button3.setGeometry(800, 100, 170, 30)
        button3.clicked.connect(self.on_click)

        button4 = QPushButton('View Results', self)
        button4.setToolTip('this is for open directory')
        button4.setGeometry(1000, 660, 100, 30)
        button4.clicked.connect(self.on_click)



        combobox = QComboBox(self)
        combobox.setToolTip('this is for selection')
        combobox.setGeometry(800,150,170,30)
        pro_list =['temp1', 'temp2', 'temp3', 'temp4', 'temp5']
        combobox.setEditable(False)
        combobox.addItems(pro_list)
        combobox.activated.connect(self.pro_click)
        """
        self.layout = QHBoxLayout()
        self.right = QPushButton()
        self.lefts = QPushButton()
        self.layout.addWidget(self.right)
        self.layout.addWidget(self.lefts)
        self.setLayout(self.layout)
        self.layout.setGeometry(QRect(100,400, 300, 300))
        """

        self.label_1 = QLabel("", self)
        self.label_1.move(80,190)
        self.label_1.setStyleSheet("border :1px solid black;")
        self.label_1.resize(370, 400)

        self.label_2 = QLabel("", self)
        self.label_2.move(700, 190)
        self.label_2.setStyleSheet("border :1px solid black;")
        self.label_2.resize(370, 400)

        self.label_3 = QLabel('Run Status :', self)
        self.label_3.move(100,665)
        self.label_3.setFont(QFont('Arial', 10))

        self.label_4 = QLabel('Run Status :', self)
        self.label_4.move(360, 665)
        self.label_4.setFont(QFont('Arial', 10))

        self.label_5 = QLabel('Run Status :', self)
        self.label_5.move(660, 665)
        self.label_5.setFont(QFont('Arial', 10))

        self.label_6 = QLabel('Not Started ', self)
        self.label_6.move(180, 665)
        self.label_6.setStyleSheet('background: 2px solid red')
        self.label_6.setFont(QFont('Arial', 10))

        self.label_7 = QLabel('In Progress ', self)
        self.label_7.move(440, 665)
        self.label_7.setStyleSheet('background: 2px solid brown')
        self.label_7.setFont(QFont('Arial', 10))

        self.label_8 = QLabel('Completed ', self)
        self.label_8.move(740, 665)
        self.label_8.setStyleSheet('background: 2px solid green')
        self.label_8.setFont(QFont('Arial', 10))



        self.show()



    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def pro_click(self):
        print('choosen')

    def dialog(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())