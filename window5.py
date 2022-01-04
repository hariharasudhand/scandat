
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 1500, 1500)
        self.setWindowTitle("My Program")
        self.labelButtons = []  # List of all the buttons displaying labels
        self.eraseButtons = []  # List of all the buttons displaying "X"
        self.Yposition = 50
        self.initUI()

    def initUI(self):
        self.labelEntry = QLineEdit(self)
        self.labelEntry.move(50, self.Yposition)
        self.labelEntry.resize(300, 40)

        self.addLabelButton = QPushButton(self)
        self.addLabelButton.setText("Add Label")
        self.addLabelButton.move(400, self.Yposition)
        self.addLabelButton.resize(300, 40)
        self.addLabelButton.clicked.connect(self.addNewLabel)

    def addNewLabel(self):
        self.Yposition += 50
        self.newLabelName = self.labelEntry.text()
        self.labelButtons.append(self.createButtonLabel(self.newLabelName))
        self.eraseButtons.append(self.eraseButtonLabel())
        self.updatelabels()

    def createButtonLabel(self, labelname):
        self.button = QPushButton(self)
        self.button.setText(str(labelname))
        self.button.resize(300, 40)
        self.button.move(50, self.Yposition)
        self.button.clicked.connect(self.printbutton)
        return self.button

    def eraseButtonLabel(self):
        self.buttonErase = QPushButton(self)
        self.buttonErase.setText("X")
        self.buttonErase.resize(40, 40)
        self.buttonErase.move(360, self.Yposition)
        self.buttonErase.clicked.connect(self.printbutton)
        return self.buttonErase

    def updatelabels(self):
        for button in self.labelButtons:
            button.show()
        for button in self.eraseButtons:
            button.show()

    def printbutton(self):
        print(self.button.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
