from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo_x = QtWidgets.QComboBox(self.centralwidget)
        self.combo_x.setGeometry(QtCore.QRect(80, 180, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.combo_x.setFont(font)
        self.combo_x.setObjectName("combo_x")
        self.combo_x.addItem("")
        self.combo_x.addItem("")
        self.combo_y = QtWidgets.QComboBox(self.centralwidget)
        self.combo_y.setGeometry(QtCore.QRect(440, 180, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.combo_y.setFont(font)
        self.combo_y.setObjectName("combo_y")
        self.combo_y.addItem("")
        self.combo_y.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(290, 470, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(306, 340, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submit.clicked.connect(self.pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_x.setItemText(0, _translate("MainWindow", "0"))
        self.combo_x.setItemText(1, _translate("MainWindow", "1"))
        self.combo_y.setItemText(0, _translate("MainWindow", "0"))
        self.combo_y.setItemText(1, _translate("MainWindow", "1"))
        self.submit.setText(_translate("MainWindow", "submit"))
        self.label.setText(_translate("MainWindow", "X xor Y ="))


    def pressed(self):
        x = int(self.combo_x.currentText())
        y = int(self.combo_y.currentText())
        xor = (x and not y) or (not x and y)

        if xor == True:
            xor = 1
        else:
            xor = 0

        self.label.setText("x xor y = " + str(xor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
