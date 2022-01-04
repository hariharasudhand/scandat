import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class mainwindow(QMainWindow):
    count = 0

    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.MDI = QMdiArea()
        self.setCentralWidget(self.MDI)
        bar = self.menuBar()

        file = bar.addMenu("file")
        file.addAction("new")
        file.addAction("cascade")
        file.addMenu("tile")
        file.triggered[QAction].connect(self.window_action)
        self.setWindowTitle("MDI demo")

    def window_action(self, q):
        print("tiggered")

        if q.text() == "new":
            mainwindow.count = mainwindow.count+1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow" + str(mainwindow.count))
            self.MDI.addSubWindow(sub)
            sub.show()

        if q.text() == "cascade":
            self.MDI.cascadeSubWindows()

        if q.text() == " tile":
            self.MDI.tileSubWindows()


def main():
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()

