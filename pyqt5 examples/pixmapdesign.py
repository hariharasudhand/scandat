from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 631, 461))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("demo3.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.football = QtWidgets.QPushButton(self.centralwidget)
        self.football.setGeometry(QtCore.QRect(70, 520, 181, 23))
        self.football.setObjectName("football")
        self.flower = QtWidgets.QPushButton(self.centralwidget)
        self.flower.setGeometry(QtCore.QRect(324, 520, 191, 23))
        self.flower.setObjectName("flower")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.football.clicked.connect(self.football_in)
        self.flower.clicked.connect(self.flower_in)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.football.setText(_translate("MainWindow", "football"))
        self.flower.setText(_translate("MainWindow", "flower"))

    def football_in(self):
        self.photo.setPixmap(QtGui.QPixmap("demo3.jpg"))
    def flower_in(self):
        self.photo.setPixmap(QtGui.QPixmap("demo4.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
