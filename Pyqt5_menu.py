import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        RunAct = QAction(QIcon('logo5.png'), '&Run', self)
        RunAct.setShortcut('Alt+Ctrl+F10')
        RunAct.setStatusTip('Run application')
        #RunAct.triggered.connect(qApp.exec_())


        exitAct = QAction(QIcon('logo5.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Run')
        fileMenu.addAction(RunAct)
        fileMenu.addAction(exitAct)




        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Scandat studio')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()