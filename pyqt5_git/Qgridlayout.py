import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    for i in range(1,5):
        for j in range(1,5):
            grid.addWidget(QPushButton("b"+str(i)+str(j)), i, j)

    win.setLayout(grid)
    win.setWindowTitle("scandat studio")
    win.setGeometry(300,200,100,200)
    win.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    window()